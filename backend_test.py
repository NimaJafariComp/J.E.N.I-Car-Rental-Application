from back_end.car_rental import CarRentalService
from back_end import car_rental

def main():
    username = 'admin'
    password = 'jenipassword'
    host = '127.0.0.1' 
    port = 3307
    car_rental_obj = car_rental.CarRentalService(host, port, username, password)
    car_rental_obj.connect_to_mysql()
    
    #car_rental_obj.add_car("4VG7DARF4XN766527", "72", "13", "240", "7JMC420", "2007", "Vectra C", "Opel", "Grey", "Sedan")
    print(car_rental_obj.get_reservations())
    print("\n")
    car_rental_obj.resevation_history("nima.mona82@gmail.com")
    
    
    
    
    """
    Test for hash_password function
    """
    # user_password = "password"
    # hashed_password = car_rental_obj.hash_password(user_password)
    # print(hashed_password)
    
    """
    Test for create_admin function
    """
    
    # car_rental_obj.create_admin("Johnny", "admin_johnny", "johnny@gmail.com", "password123")
    
    """
    Test for password check
    """
    #print(car_rental_obj.check_password_admin("admin_jeni", "computer123","admin")) 
    
    """
    Test for changing passwords
    """
    # car_rental_obj.update_password_admin("admin_jeni", "computer123")
    
    
    #car_rental_obj.make_reservation("2025-05-10", "2025-05-12", 0,"AYOOOOOOOOOOOOOOOOOOO",7)
    #car_rental_obj.make_reservation("2024-05-04", "2024-05-08", 0,"nima.mona82@gmail.com",3)
    # car_rental_obj.reservation_cancel_setter(61)
    # car_rental_obj.reservation_confirm_setter(61)
    # print(car_rental_obj.get_reservations())
    # print("\n")
    # car_rental_obj.revenue()
    #car_rental_obj.make_reservation("2024-05-04", "2024-05-08", 0, "nima.mona82@gmail.com",5)
    #car_rental_obj.make_reservation("2024-06-04", "2024-06-08", 0, "nima.jafari.614@my.csun,edu",2)
    
    # admin = car_rental_obj.admin_login("admin_elijah", "jenipassword")
    
    #car_rental_obj.user_update_password("cust_elijah", "password123", "customer")
    
    # customer = car_rental_obj.customer_login("cust_elijah", "password123")
    
    # print(car_rental_obj.check_password("cust_elijah", "password123", "customer"))
main()