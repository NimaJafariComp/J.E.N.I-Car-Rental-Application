import sys
from PyQt5.QtWidgets import *
from front_end.config.screenConfig import screen_config
from front_end.mainWindow import main_window

def main():
    run()

def run():
    screenConfig = screen_config()
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())

#    # Need username and password at the beginning
#    username = 'admin'
#    password = 'jenipassword'
#    host = 'jeni.cfeouw8igyj4.us-west-1.rds.amazonaws.com' 
#    port = 3306
#    # Needs to happen every single time, this is how the connection
#    # to MySQL is initiated
#    
#    initialize_database(host, port, username, password)
#    car_rental_obj = cr(host, port, username, password)
#    car_rental_obj.connect_to_mysql()
#    
#    """
#    # Example of adding a car
#    # Input:
#    #       First: VIN
#    #       Second: Mileage, 500 in this case 
#    #       Third: MPG, 45 in this case 
#    #       Fourth: Price, 100 in this case
#    #       Fifth: License Plate
#    #       Sixth: Car Year
#    #       Seventh: Car Model
#    #       Eight: Car Make
#    #       Ninth: Car Color
#    #       Tenth: Car Type
#    # Output: None
#    """
#    car_rental_obj.add_car('1FTPW14554KC36033', 500, 45, 100, '5XDI128',
#                        '2012', 'Land Cruiser', 'Toyota', 'Gray', 'SUV')
#    car_rental_obj.add_car('1FTPW14554KC36032', 500, 45, 100, '5XDI127',
#                        '2012', 'Land Cruiser', 'Toyota', 'Gray', 'Sedan')
#    car_rental_obj.add_car('1FTPW14554KC36032', 500, 45, 100, '5XDI127',
#                        '2022', 'Sienna', 'Toyota', 'white', 'SUV')
# 
#    """
#    # Example of "deleting" a car
#    # Input: Car ID 
#    # Output: None
#    """
#    car_rental_obj.delete_car(1)
#    
#    """
#    # Example of "deleting" multiple cars
#    # Input: List of Car ID
#    # Output: None
#    """
#    car_rental_obj.delete_multiple_cars([2, 3, 4, 5])
#
#    """
#    # Example of adding a report
#    # Input: 
#    #       First: Car ID, 1 in this case
#    #       Second: Damages, "None" in this case. A string
#    #       Third: Gas Amount, int, 10 in this case
#    #       Fourth: Reservation ID, int, 3
#    """
#    car_rental_obj.add_report(1, "None", 10, 3)
#    
#    """
#    # Example of a search, customer_search returns a list.
#    # print function is to just show what the output is and its format
#    # Input:
#    #       First: Start Date
#    #       Second: End Date
#    #       Third: Car Type 
#    # Output: List of list 
#    # Each list inside the main list is a "car"
#    # Data per index:
#    # Index 0: Car ID 
#    # Index 1: Mileage
#    # Index 2: MPG
#    # Index 3: Price
#    # Index 4: Car Year
#    # Index 5: Car Model
#    # Index 6: Car Make
#    # Index 7: Car Color
#    # Index 8: Car Type
#    """
#    # print(car_rental_obj.customer_search("2024-02-10", "2024-02-12", "Sedan"))
#    
#    """
#    # Example of making a reservation
#    # Input:
#    #       First: Start Date
#    #       Second: End Date
#    #       Third: Insurance, a boolean vaule. 0 or 1
#    #       Fourth: CustomerEmail
#    #       Fifth: Car ID
#    # Output: None
#    """
#    car_rental_obj.make_reservation("2024-02-10", "2024-02-12", 1, "elijah@somisomi.com", 7)
#    
#    print_only(host, port, username, password)
#    
#    """
#    # Example of getting all reservations
#    # Input: None
#    # Output: List of Reservations
#    #   Index 1: Reservation Id
#    #   Index 2: Start Date
#    #   Index 3: End Date
#    #   Index 4: Insurance
#    #   Index 5: CustomerEmail
#    #   Index 6: Car ID
#    """
#    print(car_rental_obj.get_reservations())
#    
#    """
#    # Example of getting all active cars for admins
#    # Input: None
#    # Output: List of lists. Each list is a car 
#    #   Index 1: Car ID
#    #   Index 2: VIN
#    #   Index 3: Mileage
#    #   Index 4: MPG
#    #   Index 5: Price
#    #   Index 6: IsActive (does not matter in your case)
#    #   Index 7: License Plate
#    #   Index 8: Car Year
#    #   Index 9: Car Model
#    #   Index 10: Car Make
#    #   Index 11: Car Color
#    #   Index 12: Car Type
#    """
#    print(car_rental_obj.get_inventory_admin())
#    
main()
