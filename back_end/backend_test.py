from database_class import database_utility_class as dbu
from database_class.inventory_class import inventory as inv

"""
# dbu.initialize_connection()
# inv_object = inv()
# inv_object.initialize_inventory()

# for x in inv_object.get_inventory():
    # print(x)

# print("\n\n\n")

# inv_object.add_car('4T1BF1FK3EU338253', 100, 50, 250.00, '7IVQ651', '1999', 'E-Class', 'Mercedes-Benz', 'Black', 'Sedan')
# inv_object.add_car('1FTWW31P95EB34131', 600, 35, 150.00, '7KJV101', '2014', '200', 'Chrysler', 'Black', 'Sedan')
# inv_object.add_car('4T1BF1FK3EU338251', 100, 50, 250.00, '7IVQ653', '2011', 'Juke', 'Nissan', 'Red', 'Hatchback')
# print(inv_object.get_inventory())

# returns index of car in inventory 
# index = inv_object.search_car(1)
# print(inv_object.get_inventory()[index].retire_car())

# print(inv_object.get_car_from_inventory(inv_object.search_car(1)).get_car_id())

# # how to retire car from inventory
# # 1 is the input: car_id
# inv_object.get_car_from_inventory(inv_object.search_car(1)).retire_car()

# # adding a report to a car
# inv_object.get_car_from_inventory(index).add_report("None", 10, 1, 1)
# start_date, end_date = '2024-02-10', '2024-02-12'

# inv_object.initialize_search_inventory(start_date, end_date)

# print("Customer's Search\n")
# for x in inv_object.get_inventory():
    # print(x)
"""

username = 'admin'
password = 'jenipassword'
host = '127.0.0.1' 
port = 3307

dbu.initialize_connection(host, port, username, password)
hashed_password = dbu.get_hashed_password(1, "Admin")
print(hashed_password[0])