#!/usr/bin/python
# -*- coding: UTF-8 -*-
from entities.report import Report


class ContractReport(Report):
    def __init__(self, working_dir_name, reportTableName, excel_sheet_name):
        super().__init__(working_dir_name, reportTableName, excel_sheet_name, None)
        self.SELECTED_COL_NAMES = ["contract_id", "money_flow"]
        self.SELECTED_COL_IDS = r'B,D'
        self.SKIP_ROWS = 1
