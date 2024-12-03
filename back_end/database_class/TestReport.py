import unittest
from report_class import report

class TestReport(unittest.TestCase):
    def setUp(self):
        """Set up a report instance for testing."""
        self.report = report("Scratch on front bumper", 3.5, 101, 202)

    def test_initialization(self):
        """Test the initialization of the report object."""
        self.assertIsNone(self.report.report_id)  # report_id should be None
        self.assertEqual(self.report.damages, "Scratch on front bumper")
        self.assertEqual(self.report.gas_amount, 3.5)
        self.assertEqual(self.report.car_id, 101)
        self.assertEqual(self.report.reservation_id, 202)

    def test_get_car_id(self):
        """Test the get_car_id method."""
        self.assertEqual(self.report.get_car_id(), 101)

    def test_get_damage(self):
        """Test the get_damage method."""
        self.assertEqual(self.report.get_damage(), "Scratch on front bumper")

    def test_get_gas_amount(self):
        """Test the get_gas_amount method."""
        self.assertEqual(self.report.get_gas_amount(), 3.5)

    def test_get_reservation_id(self):
        """Test the get_reservation_id method."""
        self.assertEqual(self.report.get_reservation_id(), 202)

    def test_get_report_id(self):
        """Test the get_report_id method before and after setting it."""
        self.assertIsNone(self.report.get_report_id())  # Should be None initially
        self.report.set_report_id(1)
        self.assertEqual(self.report.get_report_id(), 1)  # Should return the assigned report_id

    def test_set_report_id(self):
        """Test the set_report_id method."""
        self.report.set_report_id(42)
        self.assertEqual(self.report.report_id, 42) # Check if the report_id is set correctly

    def test_repr(self):
        """Test the __repr__ method."""
        self.report.set_report_id(99)
        self.assertEqual(repr(self.report), 'Report ID: 99')

if __name__ == '__main__':
    unittest.main()
