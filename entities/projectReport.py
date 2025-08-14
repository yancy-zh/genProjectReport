from entities.report import Report


class ProjectReport(Report):
    def __init__(self, working_dir_name, reportTableName, excel_sheet_name):
        super().__init__(working_dir_name, reportTableName, excel_sheet_name)
        self.SELECTED_COL_NAMES = ["project_id", "voltage_lvl", "proj_startDate", "proj_endDate"]
        self.SELECTED_COL_IDS = r'A,W, X, Y'
        self.SKIP_ROWS = 1
