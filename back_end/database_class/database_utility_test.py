import database_utility_class as dbu
import unittest
from unittest.mock import MagicMock


class database_utility_test(unittest.TestCase):
    
    def setUp(self):
        
        self.mock_cursor = MagicMock()
        self.mock_db = MagicMock()

        
        dbu.mycursor = self.mock_cursor
        dbu.mydb = self.mock_db
    
    # calculate_days method
        
    def test_valid_date_range(self):
        """Test with valid start and end dates."""
        start_date = '2024-01-01'
        end_date = '2024-01-10'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, 9)  # Expecting 9 days

    def test_end_date_before_start_date(self):
        """Test where the end date is before the start date."""
        start_date = '2024-01-10'
        end_date = '2024-01-01'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, -1)  # Expecting -1 for invalid range

    def test_invalid_date_format(self):
        """Test with invalid date format."""
        start_date = '2024/01/01'  # Invalid format
        end_date = '2024-01-10'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, -1)  # Expecting -1 for invalid format

    def test_non_date_string(self):
        """Test with non-date strings."""
        start_date = 'Hello'
        end_date = 'World'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, -1)  # Expecting -1 for invalid format

    def test_same_date(self):
        """Test when both dates are the same."""
        start_date = '2024-01-01'
        end_date = '2024-01-01'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, 0)  # Expecting 0 days
        
    #validation testing
    def test_empty_start_date(self):
        """Test with an empty start date."""
        start_date = ''
        end_date = '2024-01-10'
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, -1)  # Expecting -1 for invalid input
    
    def test_empty_end_date(self):
        """Test with an empty end date."""
        start_date = '2024-01-01'
        end_date = ''
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, -1)  # Expecting -1 for invalid input
    
    def test_both_dates_empty(self):
        """Test with both start and end dates empty."""
        start_date = ''
        end_date = ''
        result = dbu.calculate_days(start_date, end_date)
        self.assertEqual(result, -1)  # Expecting -1 for invalid input

    
    # confirm_reservation method
    
    def test_confirm_reservation_success(self):
        """Test confirming a reservation successfully."""
        reservation_id = 1
        
        
        self.mock_cursor.fetchone.return_value = (0,)  
        dbu.confirm_reservation(reservation_id)
        
        
        self.mock_cursor.execute.assert_any_call(
            "SELECT Canceled FROM Reservations WHERE ReservationId = %s", 
            (reservation_id,)
        )
        
        
        self.mock_cursor.execute.assert_any_call(
            "UPDATE Reservations SET Confirmed = 1 WHERE ReservationId = %s", 
            (reservation_id,)
        )
        
        
        self.mock_db.commit.assert_called_once()
        
    def test_confirm_reservation_canceled(self):
        """Test confirming a reservation that is already canceled."""
        reservation_id = 2
        
        
        self.mock_cursor.fetchone.return_value = (1,)  # Canceled
        dbu.confirm_reservation(reservation_id)

        
        self.mock_cursor.execute.assert_any_call(
            "SELECT Canceled FROM Reservations WHERE ReservationId = %s", 
            (reservation_id,)
        )
        
        
        self.assertNotIn(
            "UPDATE Reservations SET Confirmed = 1 WHERE ReservationId = %s", 
            [call[0][0] for call in self.mock_cursor.execute.call_args_list]
        )
        
        
        self.mock_db.commit.assert_not_called()

    def test_confirm_reservation_not_found(self):
        """Test confirming a reservation that does not exist."""
        reservation_id = 3
        
        
        self.mock_cursor.fetchone.return_value = None
        dbu.confirm_reservation(reservation_id)

        
        self.mock_cursor.execute.assert_any_call(
            "SELECT Canceled FROM Reservations WHERE ReservationId = %s", 
            (reservation_id,)
        )
        
        
        self.assertNotIn(
            "UPDATE Reservations SET Confirmed = 1 WHERE ReservationId = %s", 
            [call[0][0] for call in self.mock_cursor.execute.call_args_list]
        )
        
        
        self.mock_db.commit.assert_not_called()
    
    def test_confirm_reservation_invalid_id(self): #validation testing
        """Test confirming a reservation with invalid reservation ID."""
        invalid_ids = [None, -1, -10]  # Example invalid IDs
        
        for reservation_id in invalid_ids:
            with self.subTest(reservation_id=reservation_id):
                dbu.confirm_reservation(reservation_id)
                
                
                self.mock_cursor.execute.assert_not_called()
                
                
                self.mock_db.commit.assert_not_called()
                print(f"Test passed for invalid reservation ID: {reservation_id}")


if __name__ == "__main__":
    unittest.main()
