import database_utility_class as dbu

username = 'admin'
password = 'jenipassword'
host = '127.0.0.1' 
port = 3307

dbu.initialize_connection(host, port, username, password)

# dbu.admin_sign_up("Elijah", "elijah@gmail.com", "b'$2b$12$G.2H5LGAYmWCtR0eA0wzsOLmDHV8oMgjKt/LJSqx4AG0gJNLqS0NO
dbu.admin_sign_up("Verma", "admin_verma", "verma@gmail.com", "b'$2b$12$HFa7nOY3qWi1mf9AyxZ.w.BcwJgUigE3DZEcAWGvpW.rgMqKXI4P2'")

hashed_password = dbu.get_hashed_password("admin_elijah", "Admin")
print(hashed_password)

hashed_password_2 = dbu.get_hashed_password("admin_verma", "Admin")
print(hashed_password_2)

# reservations = dbu.get_reservations()

# for x in reservations:
    # print(x)

# dbu.add_car('4T1BF1FK3EU338253', 100, 50, 250.00, '7IVQ651', '1999', 'E-Class', 'Mercedes-Benz', 'Black', 'Sedan')
# print("Car Added")

# car_id = dbu.get_car_id('4T1BF1FK3EU338253')
# print("Car ID: ", car_id)

# car_info = dbu.get_car_info(car_id)
# print("Car Info: ", car_info)

# dbu.change_mileage(1, 20000)
# print("Car 1's mileage updated to 20000")

# inventory = dbu.get_inventory()
# print("Current Inventory:")
# for car in inventory:
    # print(car)

# inventory = dbu.get_active_inventory()
# print("Active Inventory:")
# for car in inventory:
    # print(car)

# dbu.deactivate_car(1)
# print("Car 1 deactivated")

# report_id = dbu.insert_report("None", 10, 1, 2)
# print("Report Inserted with Report ID: ", report_id)

# reports = dbu.get_reports(1)
# print("Reports for Car 1")
# for report in reports:
    # print(report)

# # Original values: 1, '2024-01-19', '2024-02-19', 1, 1, 2
# dbu.update_reservation(1, '2020-01-01', '2020-02-01', 0, 2, 3)
# print("Reservation updated")

# dbu.remove_reservation(6)
# print("Reservation 6 removed")

# # Original values: 1, 'Scratch on hood', 10, 1, 1s
# dbu.update_report(1, "None", 8, 2, 3)
# print("Reservation 1 updated")

# dbu.remove_report(6)
# print("Report 6 deleted")

# dbu.update_customer(1, 'Abhishek Verma', '1999-01-01', 'verma@csun.edu')
# print("Customer 1 updated")

# dbu.remove_customer(3)
# print("Customer 3 removed")

# search_inventory = dbu.search_database('2024-02-10', '2024-02-12', 'Sedan')
# print("Search Results:")
# for car in search_inventory:
    # print(car)

# vins = dbu.get_vins()
# print("VINs in Database:")
# for vin in vins:
    # print(vin)

# dbu.insert_reservation('2024-02-10', '2024-02-12', 1, 1, car_id)
# print("Reservation Made")

# reports = dbu.get_reports(1)
# print("Reports for Car 1")
# for report in reports:
    # print(report)

# dbu.add_car('1FTWW31P95EB34131', 600, 35, 150.00, '7KJV101', '2014', '200', 'Chrysler', 'Black', 'Sedan')
# dbu.add_car('4T1BF1FK3EU338251', 100, 50, 250.00, '7IVQ653', '2011', 'Juke', 'Nissan', 'Red', 'Hatchback')
# car1 = dbu.get_car_id('4T1BF1FK3EU338253')
# car2 = dbu.get_car_id('1FTWW31P95EB34131')
# car3 = dbu.get_car_id('4T1BF1FK3EU338251')


# for x in (car1, car2, car3):
    # print(x)

# car_object = cc.car('4T1BF1FK3EU338253', 100, 50, 250.00, '7IVQ651', '1999', 'E-Class', 'Mercedes-Benz', 'Black', 'Sedan')
# car_object.set_car_id(6)
# car_object.update_mileage(400)

# car_object.update_mileage(700)

# # test for basic search function in DB class
# # should return list of cars containing all cars except Vehicle with CarID = 2
# inventory = dbu.search_database('2024-02-10','2024-02-12')

# for x in inventory:
    # print(x)

