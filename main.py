from back_end.car_rental import CarRentalService as cr

def main():
    # username = input("Enter username: ")
    # password = input("Enter password: ")
    
    global car_rental_obj
    car_rental_obj = cr("root", "Mililani3-")
    car_rental_obj.connect_to_mysql()
    
    car_rental_obj.add_car('1FTPW14554KC36033', 500, 45, 100, '5XDI128',
                        '2012', 'Land Cruiser', 'Toyota', 'Gray', 'SUV')
    car_rental_obj.delete_multiple_cars([2, 3, 4, 5])
    car_rental_obj.add_report(1, " ", 10, 3)
    print(car_rental_obj.customer_search("2024-02-10", "2024-02-12", "Sedan"))
    car_rental_obj.make_reservation("2024-02-10", "2024-02-12", 1, 2, 7)

main()
