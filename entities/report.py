import pandas as pd
from pandas import DataFrame
import os
import re
import errno

class Report:
    SELECTED_COL_IDS = None
    SELECTED_COL_NAMES = None
    CONVERTERS = {}
    SKIP_ROWS = []
    def __init__(self, working_dir_name, reportTableName, excel_sheet_name):
        self.metadata_filename = os.path.join(working_dir_name, reportTableName)
        self.excel_sheet_name = excel_sheet_name

    def importExcelSheet(self):
        if not os.path.isfile(self.metadata_filename):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.metadata_filename)
        df_metadata = pd.read_excel(self.metadata_filename, header=None, skiprows=self.SKIP_ROWS,
                                    usecols=self.SELECTED_COL_IDS,
                                    names=self.SELECTED_COL_NAMES,
                                    converters=self.CONVERTERS
                                    )
        return df_metadata
