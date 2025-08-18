import os
from styleframe import StyleFrame, Styler, utils
import datetime


class MyStyler():
    _CURR_PROJ_PATH = os.getcwd()
    _DATA_PATH = r"data/output"

    _DATETIME_TO_VALIDATE = datetime.datetime(year=2025, month=8, day=15)
    _DATETIME_TODAY = datetime.datetime.today()
    _FORMAT_OF_PRINTED_DATE = "%Y-%m-%d"
    _CAN_MODIFIED_COLS = []

    def __init__(self, df):
        print(f'正在为以下日期的数据处理格式 {self._DATETIME_TO_VALIDATE.__format__(self._FORMAT_OF_PRINTED_DATE)}')
        self.sf = StyleFrame(df)

    def canNotModifyCols(self):
        styler = Styler(bg_color=utils.colors.grey)
        for col in ["contract_id","contract_name", "contract_partner", "contract_type", "contract_valid_date", "project_id",
                    "nc_code", "proj_regis_date", "proj_category_1", "proj_category_2"]:
            self.sf.apply_column_style(cols_to_style=col, styler_obj=styler)

    def highlightMoneyFlowOut(self):
        self.sf.apply_style_by_indexes(indexes_to_style=self.sf[self.sf['money_flow'] == '付款'],
                                       styler_obj=self.moneyFlowStyler2(), cols_to_style=['money_flow'])

    def highlightMoneyFlowIn(self):
        self.sf.apply_style_by_indexes(indexes_to_style=self.sf[self.sf['money_flow'] == '收款'],
                                       styler_obj=self.moneyFlowStyler1(), cols_to_style=['money_flow'])
    def moneyFlowStyler1(self):
        return Styler(bg_color=utils.colors.green)

    def moneyFlowStyler2(self):
        return Styler(bg_color=utils.colors.blue)

    def getStyleFrame(self):
        return self.sf
