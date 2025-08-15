import os

import datetime


class Writer():
    _CURR_PROJ_PATH = os.getcwd()
    _DATA_PATH = r"data/output"
    _OUTPUT_FILE_NAME = '业+数据治理台账.xlsx'
    _DATETIME_TO_VALIDATE = datetime.datetime(year=2025, month=8, day=15)
    _DATETIME_TODAY = datetime.datetime.today()
    _FORMAT_OF_PRINTED_DATE = "%Y-%m-%d"
    _DESIRED_COL_ORDER = ["organization", "department", "project_id", "project_name",
                          "nc_code", "proj_category_1", "proj_category_2", "proj_type",
                          "contract_model", "voltage_lvl", "proj_manager", "proj_status",
                          "proj_regis_date", "proj_startDate", "proj_endDate", "contract_id",
                          "contract_name", "money_flow", "contract_partner", "contract_type",
                          "contract_valid_date", "contract_status", "contract_sum"]
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
                      "contract_sum": "合同含税金额"
                      }

    def __init__(self):
        print(f'正在写入以下日期的数据 {self._DATETIME_TO_VALIDATE.__format__(self._FORMAT_OF_PRINTED_DATE)}')

    def writeDataframeToExcel(self, df, file_name):
        print(f"运行写入台账，文件名：\n- {self._OUTPUT_FILE_NAME}\n报告生成日期：{self._DATETIME_TODAY}...")
        df.to_excel(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH, file_name), index=False)
        print(f"完成写入...")

    def reorderCols(self,df):
        df_ordered = df[self._DESIRED_COL_ORDER]
        return df_ordered
    def writeFinalTable(self, df):
        print(f"运行写入台账，文件名：\n- {self._OUTPUT_FILE_NAME}\n报告生成日期：{self._DATETIME_TODAY}...")
        df.rename(columns=self._NEW_COL_NAMES, inplace=True)
        df.to_excel(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH, self._OUTPUT_FILE_NAME), index=False)
        print(f"完成写入...")
