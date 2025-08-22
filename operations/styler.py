import os

import pandas as pd
from styleframe import StyleFrame, Styler, utils
import datetime


class MyStyler():
    _CURR_PROJ_PATH = os.getcwd()
    _DATA_PATH = r"data/output"

    _DATETIME_TO_VALIDATE = datetime.datetime(year=2025, month=8, day=15)
    _DATETIME_TODAY = datetime.datetime.today()
    _FORMAT_OF_PRINTED_DATE = "%Y-%m-%d"
    _CAN_MODIFIED_COLS = []

    def __init__(self, df: pd.DataFrame):
        print(f'正在为以下日期的数据处理格式 {self._DATETIME_TO_VALIDATE.__format__(self._FORMAT_OF_PRINTED_DATE)}')
        self.sf = StyleFrame(df)

    def canNotModifyCols(self):
        styler = Styler(bg_color=utils.colors.grey)
        for col in ["contract_id", "contract_name", "contract_partner", "contract_type", "contract_valid_date",
                    "project_id", "nc_code", "proj_regis_date", "proj_category_1"]:
            self.sf.apply_column_style(cols_to_style=col, styler_obj=styler)

    def highLightProjCategory2(self):
        self.sf.apply_column_style(styler_obj=self.redBgColorStyler(), cols_to_style=['proj_category_2'])

    def highlightMoneyFlowOut(self):
        self.sf.apply_style_by_indexes(indexes_to_style=self.sf[self.sf['money_flow'] == '付款'],
                                       styler_obj=self.blueBgColorStyler(), cols_to_style=['money_flow'])

    def highlightMoneyFlowIn(self):
        self.sf.apply_style_by_indexes(indexes_to_style=self.sf[self.sf['money_flow'] == '收款'],
                                       styler_obj=self.greenBgColorStyler(), cols_to_style=['money_flow'])

    def greenBgColorStyler(self):
        return Styler(bg_color=utils.colors.green)

    def blueBgColorStyler(self):
        return Styler(bg_color=utils.colors.blue)

    def redBgColorStyler(self):
        return Styler(bg_color=utils.colors.red)

    def greyftColorStyler(self):
        return Styler(font_color=utils.colors.grey)

    def purpleBgColorStyler(self):
        return Styler(bg_color=utils.colors.purple)

    def getStyleFrame(self):
        return self.sf

    def highLightProjectDateWrong(self, indices: list):
        self.sf.apply_style_by_indexes(indexes_to_style=indices, styler_obj=self.redBgColorStyler(),
                                       cols_to_style=["proj_startDate", "proj_endDate"])

    def highLightProjectDateWrong2(self, indices: list):
        self.sf.apply_style_by_indexes(indexes_to_style=indices, styler_obj=self.redBgColorStyler(),
                                       cols_to_style=["计划开始（开工）日期", "计划开始（竣工）日期"])

    def highLightContractSumInfoWrong(self, indices: list):
        self.sf.apply_style_by_indexes(indexes_to_style=indices, styler_obj=self.redBgColorStyler(),
                                       cols_to_style=['project_sum'])

    def highLightProjNull(self, indices: list):
        self.sf.apply_style_by_indexes(indexes_to_style=indices, styler_obj=self.redBgColorStyler(),
                                       cols_to_style=['project_id'])

    def highLightDeptRepeat(self, indices: list):
        self.sf.apply_style_by_indexes(indexes_to_style=indices, styler_obj=self.redBgColorStyler(),
                                       cols_to_style=['department'])

    def highLightProjStatusWrong(self, indices: list):
        self.sf.apply_style_by_indexes(indexes_to_style=indices, styler_obj=self.redBgColorStyler(),
                                       cols_to_style=['proj_status'])

    def canNotModifyCols2(self):
        styler = Styler(bg_color=utils.colors.grey)
        for col in ["项目编号", "工程编码", "立项日期", "工程大类", "工程子类", '财务管控内码']:
            self.sf.apply_column_style(cols_to_style=col, styler_obj=styler)

    def highlightProjFirstLine(self, indices: list):
        self.sf.apply_style_by_indexes(indexes_to_style=indices, styler_obj=self.greyftColorStyler(),
                                       cols_to_style=["organization", "department", "project_id", "project_name", "nc_code", 'fin_code',
                          "project_sum", "proj_category_1",
                          "proj_category_2", "proj_type", "contract_model", "voltage_lvl", "proj_manager",
                          "proj_status",'proj_source', "proj_regis_date", "proj_startDate", "proj_endDate"])

    def highLightProjProjSourceWrong(self, indices: list):
        self.sf.apply_style_by_indexes(indexes_to_style=indices, styler_obj=self.redBgColorStyler(),
                                       cols_to_style=['proj_source'])