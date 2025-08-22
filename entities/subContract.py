#!/usr/bin/python
# -*- coding: UTF-8 -*-
from entities.report import Report


class SubContract(Report):
    def __init__(self, working_dir_name, reportTableName, excel_sheet_name):
        super().__init__(working_dir_name, reportTableName, excel_sheet_name, None)
        self.SELECTED_COL_NAMES = self.SELECTED_COL_NAMES = ["organization", "department", "proj_regis_date",
                                                             "project_id", "nc_code", "project_name", "proj_category_1",
                                                             "proj_category_2", "proj_type", "contract_model",
                                                             "proj_manager", "proj_status", "contract_id",
                                                             "contract_name", "contract_partner", "contract_type",
                                                             "contract_valid_date", "contract_status", "contract_sum"
                                                             ]
        self.SELECTED_COL_IDS = r'B, D, E, F,G,I,J,K,L,O,P,Q,S, T, U,Z, AN, AP, AQ'
        self.SKIP_ROWS = 1
