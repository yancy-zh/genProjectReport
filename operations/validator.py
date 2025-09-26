#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import datetime


class Validator:
    _DATETIME_TODAY = datetime.datetime.today()
    _FORMAT_OF_PRINTED_DATE = "%Y-%m-%d"

    def __init__(self, df: pd.DataFrame):
        self.project_sum = None
        self.regis_date_col = None
        self.end_date_col = None
        self.start_date_col = None
        self._DEPT_NAMES = [
            "亮丽带电作业分公司",
            "市区电力工程分公司",
            "市北电力工程分公司",
            "市东电力工程分公司",
            '市南电力工程分公司',
            '高新电力工程分公司',
            '电缆工程分公司',
            '带电作业分公司',
            '第二工程分公司',
            '第三工程分公司',
            '第四工程分公司',
            '第五工程分公司',
            '第一工程分公司',
            '科技能源分公司',
            '众源工程分公司',
            '众源修试分公司',
            '本部后勤服务中心',
            '工程管理部',
            '综合管理部',
            '经营室',
            '配网室',
            '施工安装一班',
            '财务资产部',
            '领导干部',
            '配电带电作业班'
        ]
        print(f'正在处理数据校验')
        self.df = df

    def projDateValidation(self):
        self.start_date_col = pd.to_datetime(self.df["proj_startDate"])
        self.end_date_col = pd.to_datetime(self.df["proj_endDate"])
        try:
            self.regis_date_col = pd.to_datetime(self.df["proj_regis_date"], errors='coerce')
        except pd.errors.OutOfBoundsDatetime as e:
            print(f"caught an OutOfBoundsDatetime error {e}")
            print("some dates are outside of the supported dates range")
        except Exception as e:
            print(f"other errors occured: {e}")
        filtered_df_loc = self.df.loc[
            (self.start_date_col < self.regis_date_col) | (self.start_date_col > self.end_date_col)]
        return filtered_df_loc.index.tolist()

    def projDateValidation_1(self):
        self.start_date_col = pd.to_datetime(self.df["计划开始（开工）日期"])
        self.end_date_col = pd.to_datetime(self.df["计划开始（竣工）日期"])
        try:
            self.regis_date_col = pd.to_datetime(self.df["立项日期"], errors='coerce')
        except pd.errors.OutOfBoundsDatetime as e:
            print(f"caught an OutOfBoundsDatetime error {e}")
            print("some dates are outside of the supported dates range")
        except Exception as e:
            print(f"other errors occured: {e}")
        filtered_df_loc = self.df.loc[
            (self.start_date_col < self.regis_date_col) | (self.start_date_col > self.end_date_col)]
        return filtered_df_loc.index.tolist()

    def validateMainContractSum(self):
        self.project_sum = pd.to_numeric(self.df['project_sum'])
        self.mainContract_sum = pd.to_numeric(self.df['contract_sum'])
        filtered_df_loc = self.df.loc[(self.df['money_flow'] == '收款') & (self.project_sum != self.mainContract_sum)]
        return filtered_df_loc.index.tolist()

    def validateProjNull(self):
        filtered_df_loc = self.df.loc[self.df['project_id'].isna()]
        return filtered_df_loc.index.tolist()

    def getDataframe(self):
        return self.df

    def validateDeptName(self):
        filtered_df_loc = self.df.loc[~self.df['department'].isin(self._DEPT_NAMES)]
        return filtered_df_loc.index.tolist()

    def validateProjStatus(self):
        # projDateValidation_1 must be called first
        if ((self.start_date_col is None) | (self.end_date_col is None)):
            print("projDateValidation_1 must be called first")
            return
        filtered_df_loc = self.df.loc[
            ((self._DATETIME_TODAY > self.start_date_col) & (self._DATETIME_TODAY < self.end_date_col) &
             ~self.df['proj_status'].isin(['在建']))
            | ((self._DATETIME_TODAY > self.end_date_col) & (
                ~self.df['proj_status'].isin(['竣工', '结算', '结算完成', '结项'])))
            ]
        return filtered_df_loc.index.tolist()

    def validateProjNonFirstLine(self):
        filtered_df_loc = self.df.loc[self.df['group_id'].isna()]
        return filtered_df_loc.index.tolist()

    def validateProjCategory1(self):
        filtered_df_loc = self.df.loc[
            ( (  self.df['proj_category_2'].str.contains("(用户)") )& (self.df['proj_source'] != "系统外"))
            | ((  self.df['proj_category_2'].str.contains("(电网)") )& (self.df['proj_source'] != "系统内"))]
        return filtered_df_loc.index.tolist()
