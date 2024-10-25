from back_end.car_rental import CarRentalService as cr
from database.main_database import initialize_database

class api():
    def __init__(self):
        # Need username and password at the beginning
        self.username = 'admin'
        self.password = 'jenipassword'
        self.host = 'jeni.cfeouw8igyj4.us-west-1.rds.amazonaws.com' 
        self.port = 3306
        # Needs to happen every single time, this is how the connection
        # to MySQL is initiated
        
        initialize_database(self.host, self.port, self.username, self.password)
        self.car_rental_obj = cr(self.host, self.port, self.username, self.password)
        self.car_rental_obj.connect_to_mysql()
