import os

from entities.subContract import SubContract
from entities.mainContract import MainContract
from entities.projectReport import ProjectReport
from entities.ContractReport import ContractReport
import datetime

class Reader():
    _CURR_PROJ_PATH = os.getcwd()
    _DATA_PATH = r"data"
    _SUB_CONTRACT_NAME = r"工程分包合同查询20250814172514.xlsx"
    _MAIN_CONTRACT_NAME = r"工程总包合同查询20250814172359.xlsx"
    _PROJ_TABLE_NAME = r"工程详情信息导出数据-2025-08-14.xlsx"
    _CONTRACT_TABLE_NAME = r"合同信息查询-20250813.xlsx"

    _SUB_CONTRACT_SHEET_NAME = "工程分包"
    _MAIN_CONTRACT_SHEET_NAME = "工程总包"
    _PROJ_REPORT_SHEET_NAME = "项目详细信息"
    _CONTRACT_REPORT_SHEET_NAME = "sheet"

    _DATETIME_TO_VALIDATE = datetime.datetime(year=2025, month=8, day=15)
    _DATETIME_TODAY = datetime.datetime.today()
    _FORMAT_OF_PRINTED_DATE = "%Y-%m-%d"
    def __init__(self):
        print(
            f'正在读取以下日期的数据 {self._DATETIME_TO_VALIDATE.__format__(self._FORMAT_OF_PRINTED_DATE)}')

    def readSubContract(self):

        print(
            f"运行读取分包合同，文件名：\n- {self._SUB_CONTRACT_NAME}\n报告生成日期：{self._DATETIME_TODAY}...")
        subContract = SubContract(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH), self._SUB_CONTRACT_NAME, self._SUB_CONTRACT_SHEET_NAME)
        df_subContract = subContract.importExcelSheet()
        print(f"完成读取...")
        return df_subContract

    def readMainContract(self):

        print(
            f"运行读取总包合同，文件名：\n- {self._MAIN_CONTRACT_NAME}\n报告生成日期：{self._DATETIME_TODAY}...")
        subContract = MainContract(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH), self._MAIN_CONTRACT_NAME, self._MAIN_CONTRACT_NAME)
        df_MainContract = subContract.importExcelSheet()
        print(f"完成读取...")
        return df_MainContract

    def readProjectReport(self):
        print(
            f"运行读取项目全量表，文件名：\n- {self._PROJ_TABLE_NAME}\n报告生成日期：{self._DATETIME_TODAY}...")
        proj_table = ProjectReport(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH), self._PROJ_TABLE_NAME,
                                   self._PROJ_REPORT_SHEET_NAME)
        df_projs = proj_table.importExcelSheet()
        print(f"完成读取...")
        return df_projs

    def readContractReport(self):
        print(
            f"运行读取合同全量表，文件名：\n- {self._CONTRACT_TABLE_NAME}\n报告生成日期：{self._DATETIME_TODAY}...")
        contracts_table = ContractReport(os.path.join(self._CURR_PROJ_PATH, self._DATA_PATH), self._CONTRACT_TABLE_NAME,
                                   self._CONTRACT_REPORT_SHEET_NAME)
        df_contracts = contracts_table.importExcelSheet()
        print(f"完成读取...")
        return df_contracts

