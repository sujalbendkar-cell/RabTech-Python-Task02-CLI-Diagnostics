"""
Unit tests for DevInspector.
"""

import unittest
from unittest.mock import patch
from devhealth.inspector import DevInspector

class TestDevInspector(unittest.TestCase):
    def setUp(self):
        self.inspector = DevInspector()

    def test_python_version_check(self):
        res = self.inspector.check_python_version()
        self.assertEqual(res["name"], "Python Version")
        self.assertIn(res["status"], ["OK", "FAIL"])

    def test_disk_space_valid_path(self):
        res = self.inspector.check_disk_space(".")
        self.assertIn(res["status"], ["OK", "WARN", "FAIL"])
        self.assertIn("free_gb", res)

    def test_disk_space_malformed_path(self):
        res = self.inspector.check_disk_space("/invalid_non_existent_path_xyz_123")
        self.assertEqual(res["status"], "CONFIG_ERROR")

    @patch("shutil.which")
    def test_missing_required_tool(self, mock_which):
        mock_which.return_value = None
        res = self.inspector.check_developer_tools()
        self.assertEqual(res["status"], "FAIL")
        self.assertIn("git", res["missing_required"])

    def test_full_diagnostics_structure(self):
        diag = self.inspector.run_full_diagnostics(".")
        self.assertIn("system_info", diag)
        self.assertIn("checks", diag)
        self.assertIn("overall_status", diag)

if __name__ == "__main__":
    unittest.main()