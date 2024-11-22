from back_end.car_rental import CarRentalService as cr

def main():
    username = 'admin'
    password = 'jenipassword'
    host = '127.0.0.1' 
    port = 3307
    car_rental_obj = cr(host, port, username, password)
    car_rental_obj.connect_to_mysql()
    
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
    # print(car_rental_obj.check_password_admin("admin_jeni", "computer123")) 
    
    """
    Test for changing passwords
    """
    # car_rental_obj.update_password_admin("admin_jeni", "computer123")

main()