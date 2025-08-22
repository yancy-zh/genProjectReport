from entities.report import Report


class ProjectReport(Report):
    def __init__(self, working_dir_name, reportTableName, excel_sheet_name, header_row_num):
        super().__init__(working_dir_name, reportTableName, excel_sheet_name, header_row_num=header_row_num)
        self.SELECTED_COL_NAMES = ["project_id", "project_sum", "voltage_lvl", "proj_startDate", "proj_endDate",
                                   'proj_source', 'fin_code']
        self.SELECTED_COL_IDS = r'A,S, W, X, Y, AG, AH'
        self.SKIP_ROWS = 1
