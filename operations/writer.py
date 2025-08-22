import os

import datetime
import pandas as pd


class Writer():
    _CURR_PROJ_PATH = os.getcwd()
    _DATA_PATH = r"data/output"
    _OUTPUT_CONTRACT_TABLE_NAME = '业+数据治理台账.xlsx'
    _OUTPUT_PROJ_TABLE_NAME = '业+数据治理台账_项目.xlsx'
    _DATETIME_TO_VALIDATE = datetime.datetime(year=2025, month=8, day=15)
    _DATETIME_TODAY = datetime.datetime.today()
    _FORMAT_OF_PRINTED_DATE = "%Y-%m-%d"
    _DESIRED_COL_ORDER = ['group_id', "organization", "department", "project_id", "project_name", "nc_code", 'fin_code',
                          "project_sum", "proj_category_1",
                          "proj_category_2", "proj_type", "contract_model", "voltage_lvl", "proj_manager",
                          "proj_status", 'proj_source', "proj_regis_date", "proj_startDate", "proj_endDate",
                          "contract_id", "contract_name", "money_flow", "contract_partner", "contract_type",
                          "contract_valid_date", "contract_status", "contract_sum"
                          ]
    _NEW_COL_NAMES = {"organization": '立项单位',
                      "department": '责任部门',
                      "project_id": '项目编码',
                      "project_name": '项目名称',
                      "nc_code": '工程编码',
                      "proj_category_1": '工程大类',
                      "proj_category_2": '工程子类',
                      "proj_type": '项目类型',
                      "contract_model": '承揽模式',
                      "voltage_lvl": '电压等级',
                      "proj_manager": '项目管理人员',
                      "proj_status": '项目状态',
                      "proj_regis_date": '立项日期',
                      "proj_startDate": '计划开工日期',
                      "proj_endDate": '计划竣工日期',
                      "contract_id": '合同编码',
                      "contract_name": '合同名称',
                      "money_flow": '资金流向',
                      "contract_partner": '合同对方名称',
                      "contract_type": '合同类型',
                      "contract_valid_date": '合同生效日期',
                      "contract_status": '合同状态',
                      "contract_sum": "合同含税金额",
                      'project_sum': "项目金额",
                      'proj_source': '项目来源',
                      'fin_code': '财务管控内码',
                      'group_id': '项目序号'
                      }

    def __init__(self):
        print(f'正在写入以下日期的数据 {self._DATETIME_TO_VALIDATE.__format__(self._FORMAT_OF_PRINTED_DATE)}')

    def writeDataframeToExcel(self, df, file_name):
        print(f"运行写入台账，文件名：\n- {file_name}\n报告生成日期：{self._DATETIME_TODAY}...")
        df.to_excel(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH, file_name), index=False)
        print(f"完成写入...")

    def reorderCols(self, df):
        df_ordered = df[self._DESIRED_COL_ORDER]
        return df_ordered

    def setGroupId(self, df: pd.DataFrame):
        # index_ls = [None] * len(df)
        # counter = 1
        # df.loc[0, 'project_id'] = counter
        # for i in range(1, len(df)):
        #     if df.at[i, 'project_id'] != df.at[i-1, 'project_id']:
        #         counter+=1
        #         index_ls[i] = counter
        # df['group_id'] = index_ls
        group_id = df.groupby('project_id').ngroup()
        changes = group_id.diff() != 0
        df['group_id'] = changes.cumsum()
        df['group_id'] = df['group_id'].mask(~changes, None)
        return df

    def writeFinalContractTable(self, df):
        print(f"运行写入合同台账，文件名：\n- {self._OUTPUT_CONTRACT_TABLE_NAME}\n报告生成日期：{self._DATETIME_TODAY}...")
        df.rename(columns=self._NEW_COL_NAMES, inplace=True)
        df.to_excel(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH, self._OUTPUT_CONTRACT_TABLE_NAME),
                    index=False)._save()
        print(f"完成写入...")

    def writeFinalProjTable(self, df):
        print(f"运行写入项目台账，文件名：\n- {self._OUTPUT_PROJ_TABLE_NAME}\n报告生成日期：{self._DATETIME_TODAY}...")
        df.to_excel(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH, self._OUTPUT_PROJ_TABLE_NAME),
                    index=False)._save()
        print(f"完成写入...")

    def writeStyleFrame(self, sf):
        print(f"write styleframe，文件名：\n- styleframe.xlsx \n报告生成日期：{self._DATETIME_TODAY}...")
        sf.to_excel(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH, "styleframe.xlsx"))._save()
        print(f"完成写入...")

    def writeComments(self):
        data = {'序号': [1, 2, 3, 4, 5, 6, 7, 8, 9], '校验规则': [
            "字段顺序为工程在前，关联的合同在后",
            '前端不可修改或者不允许修改字段进行置灰',
            '进行了立项日期<计划开工日期<计划竣工日期校验，不满足条件的，计划开工日期，计划竣工日期红色高亮',
            '总包合同金额不等于项目金额的，项目金额红色高亮',
            '合同资金流向：收款：绿色高亮，付款：蓝色高亮',
            '合同未关联项目的，即项目编码为空的，项目编码一栏红色高亮',
            '标红错误的项目状态，当前日期大于计划开工日期，小于竣工日期，项目状态为以下之一：立项或在建，当前日期大于计划竣工日期，项目状态为以下之一：竣工，结算，结项',
            '第一列为项目序号，关联同一个项目的一组合同，只有第一行项目信息高亮',
            '项目来源需符合项目大类，用户工程：系统外，电网工程：系统内，不满足的项目来源一栏红色高亮'
        ]}
        df = pd.DataFrame(data)
        with pd.ExcelWriter(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH, self._OUTPUT_CONTRACT_TABLE_NAME),
                            mode='a', engine='openpyxl', if_sheet_exists='new') as writer:
            df.to_excel(writer, sheet_name="校验规则说明", index=False)
