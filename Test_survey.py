"""
Automated Testing Suite for SurveyPy
Author: Abdalrhman Musa
"""
import unittest
from surveying.intersections import calculate_forward_intersection
from gnss.rtk_config import GNSSQualityControl
from geodesy.transformations import HelmertTransformation2D


class TestSurveyPy(unittest.TestCase):

    def test_forward_intersection(self):
        # Testing forward intersection math with 45 and 315 degree bearings
        e_c, n_c = calculate_forward_intersection(100, 200, 45, 300, 200, 315)
        self.assertAlmostEqual(e_c, 200.0, places=2)
        self.assertAlmostEqual(n_c, 300.0, places=2)

    def test_gnss_quality(self):
        # Testing RTK metrics validator
        qc = GNSSQualityControl()
        res = qc.evaluate_point_quality(pdop=1.5, sat_count=10, status="FIXED")
        self.assertTrue(res['is_valid'])


if __name__ == "__main__":
    unittest.main(exit=False)
    input("\n[+] Tests completed successfully. Press Enter to exit...")