import car_class
import inventory_class
import class_database

username = input("Enter username: ")
password = input("Enter password: ")

inventory_object = inventory_class.inventory(username, password)
database_object = class_database.test(username,password)
# test for get_inventory()
# output should be 1, 2, 3, 4, 5
# inventory_object.get_inventory()

# test for get_inventory()
# output should be 1, 2, 3, 4, 5
# inventory_object.get_available_inventory()

inventory_object.add_car('4T1BF1FK3EU338252', 100, 50, 250.00, '7IVQ656')
database_object.retire_car(1)

# output should be 1, 2, 3, 4, 5, 6
inventory_object.get_inventory()

# output should be 2, 3, 4, 5, 6
inventory_object.get_available_inventory()


