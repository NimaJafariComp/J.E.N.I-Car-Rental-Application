from .car_rental import CarRentalService 


def test_admin_login_good():
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


def test_admin_login_bad():
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
    
    assert user is False

