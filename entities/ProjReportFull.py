from entities.report import Report


class ProjReportFull(Report):
    def __init__(self, working_dir_name, reportTableName, excel_sheet_name, header_row_num):
        super().__init__(working_dir_name, reportTableName, excel_sheet_name, header_row_num)
        self.SELECTED_COL_NAMES = ["project_id", "project_name", "organization", "department", 'proj_regis_date',
                                   'nc_code', 'proj_category_1', 'proj_category_2', 'proj_type', 'contract_partner',
                                   'contract_sum', 'contract_model', 'proj_manager', "voltage_lvl", "proj_startDate",
                                   "proj_endDate", 'proj_status', 'proj_source', 'fin_code']
        self.SELECTED_COL_IDS = r'A,B, D, F, G,H, L, M, N, P, S, U, V, W, X, Y, AB, AG, AH'
