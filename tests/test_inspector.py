"""
Unit tests.
"""
import unittest
from devhealth.inspector import DevInspector

class TestDevInspector(unittest.TestCase):
    def test_checks(self):
        insp = DevInspector()
        res = insp.run_all(".")
        self.assertIn("overall", res)
        self.assertIn(res["overall"], ["OK", "WARN", "FAIL", "CONFIG_ERROR"])

if __name__ == "__main__":
    unittest.main()
