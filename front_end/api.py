from back_end.car_rental import CarRentalService as cr
from database.main_database import initialize_database

class api():
    '''
    A class that is used to set up an api object to connect the back end to the front end.
    '''
    def __init__(self):
        '''
        initializes the mysql info and the car rental object from the back end.
        '''
        # Need username and password at the beginning
        self.username = 'admin'
        self.password = 'jenipassword'
        self.host = '127.0.0.1' 
        self.port = 3307
        # Needs to happen every single time, this is how the connection
        # to MySQL is initiated
        
        # initialize_database(self.host, self.port, self.username, self.password)
        self.car_rental_obj = cr(self.host, self.port, self.username, self.password)
        self.car_rental_obj.connect_to_mysql()
