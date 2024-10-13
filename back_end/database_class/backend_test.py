import database_utility_class as dbu
import inventory_class as inv

dbu.initialize_connection()
inv_object = inv.inventory()
inv_object.initialize_inventory()
print(inv_object.get_inventory())

print("\n\n\n")

inv_object.add_car('4T1BF1FK3EU338253', 100, 50, 250.00, '7IVQ651', '1999', 'E-Class', 'Mercedes-Benz', 'Black', 'Sedan')
inv_object.add_car('1FTWW31P95EB34131', 600, 35, 150.00, '7KJV101', '2014', '200', 'Chrysler', 'Black', 'Sedan')
inv_object.add_car('4T1BF1FK3EU338251', 100, 50, 250.00, '7IVQ653', '2011', 'Juke', 'Nissan', 'Red', 'Hatchback')

print(inv_object.get_inventory())

