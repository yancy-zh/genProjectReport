import unittest
from operations.writer import Writer

class TestWriter(unittest.TestCase):
    def test_add_version_number_to_filename(self):
        writer= Writer()
        self.assertEqual("业+数据治理台账_v1.0_2025-08-27.xlsx",writer.add_version_number_to_filename(writer.get_output_table_name()) )
