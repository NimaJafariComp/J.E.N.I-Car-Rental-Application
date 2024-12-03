from .car_rental import CarRentalService 
import datetime


def test_admin_login_allgood():
    # Need username and password at the beginning
    username = 'admin'
    password = 'jenipassword'
    host = '127.0.0.1' 
    port = 3307
    # Needs to happen every single time, this is how the connection
    # to MySQL is initiated
    
    # initialize_database(self.host, self.port, self.username, self.password)
    car_rental_obj = CarRentalService(host, port, username, password)
    car_rental_obj.connect_to_mysql()
    
    user = car_rental_obj.admin_login("johnnyaguilar", "password")
    assert user.admin_id == 10
    assert user.user == "Johnny Aguilar" 
    assert user.email == "johnathan.aguilar.350@my.csun.edu"
    assert user.username == "johnnyaguilar" 
    assert user.password ==  "$2b$12$8kNIoxshbtpYRGgBqgkDt.FOG/bp9FHut.6wkPkLmFMEQS95DS1ci"
    assert user.dob is None


def test_admin_login_badpw():
    # Need username and password at the beginning
    username = 'admin'
    password = 'jenipassword'
    host = '127.0.0.1' 
    port = 3307
    # Needs to happen every single time, this is how the connection
    # to MySQL is initiated
    
    # initialize_database(self.host, self.port, self.username, self.password)
    car_rental_obj = CarRentalService(host, port, username, password)
    car_rental_obj.connect_to_mysql()
    
    user = car_rental_obj.admin_login("johnnyaguilar", "notrightpassword")
    
    assert user is None

def test_admin_login_baduser():
# Need username and password at the beginning
    username = 'admin'
    password = 'jenipassword'
    host = '127.0.0.1' 
    port = 3307
    # Needs to happen every single time, this is how the connection
    # to MySQL is initiated
    
    # initialize_database(self.host, self.port, self.username, self.password)
    car_rental_obj = CarRentalService(host, port, username, password)
    car_rental_obj.connect_to_mysql()
    
    user = car_rental_obj.admin_login("johnny", "password")

    assert user is None

def test_customer_login_allgood():
    # Need username and password at the beginning
    username = 'admin'
    password = 'jenipassword'
    host = '127.0.0.1' 
    port = 3307
    # Needs to happen every single time, this is how the connection
    # to MySQL is initiated
    
    # initialize_database(self.host, self.port, self.username, self.password)
    car_rental_obj = CarRentalService(host, port, username, password)
    car_rental_obj.connect_to_mysql()
    
    user = car_rental_obj.customer_login("cust_elijah", "password123")
    assert user.cust_id == 1
    assert user.user == "Elijah Sagaran" 
    assert user.email == "elijahsagaran@gmail.com"
    assert user.username == "cust_elijah" 
    assert user.password ==  "$2b$12$kNmpB3yAbMqBh3//SBeZR.clgYfMvK/2K6In8mvBBsSImxQWD28.i"
    check_dob = datetime.date(2000, 10, 2)
    assert user.dob == check_dob


def test_customer_login_badpw():
    # Need username and password at the beginning
    username = 'admin'
    password = 'jenipassword'
    host = '127.0.0.1' 
    port = 3307
    # Needs to happen every single time, this is how the connection
    # to MySQL is initiated
    
    # initialize_database(self.host, self.port, self.username, self.password)
    car_rental_obj = CarRentalService(host, port, username, password)
    car_rental_obj.connect_to_mysql()
    
    user = car_rental_obj.customer_login("cust_elijah", "notrightpassword")
    
    assert user is None

def test_customer_login_baduser():
# Need username and password at the beginning
    username = 'admin'
    password = 'jenipassword'
    host = '127.0.0.1' 
    port = 3307
    # Needs to happen every single time, this is how the connection
    # to MySQL is initiated
    
    # initialize_database(self.host, self.port, self.username, self.password)
    car_rental_obj = CarRentalService(host, port, username, password)
    car_rental_obj.connect_to_mysql()
    
    user = car_rental_obj.customer_login("johnny", "password123")

    assert user is None


