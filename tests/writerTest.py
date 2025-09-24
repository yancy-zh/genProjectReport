import unittest
from operations.writer import Writer
import pandas as pd
import os
from operations.reader import Reader

class TestWriter(unittest.TestCase):
    @unittest.skip("version number tested")
    def test_add_version_number_to_filename(self):
        writer = Writer()
        self.assertEqual("业+数据治理台账_v1.0_2025-08-27.xlsx",
                         writer.add_version_number_to_filename(writer.get_output_table_name()))

    def test_validation_drop_down_menus(self):
        writer = Writer()
        reader = Reader()
        # get the parent folder of the script folder
        absPath = os.path.join(os.getcwd(), '..')
        reader.setCurrWorkingPath(absPath)
        df = reader.readProjectReport()
        output_filename = "testtable.xlsx"
        writer.setCurrWorkingPath(absPath)
        self.assertEqual(None, writer.writeDataframeToExcel(df, output_filename))
