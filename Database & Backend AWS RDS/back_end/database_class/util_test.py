import database_utility_class as dbu
import car_class as cc
import print_tables

username = "admin"
password = "JenniProject2024"

dbu.initialize_connection(username,password)
reservations = dbu.get_reservations()

for x in reservations:
    print(x)
# dbu.add_car('4T1BF1FK3EU338253', 100, 50, 250.00, '7IVQ651', '1999', 'E-Class', 'Mercedes-Benz', 'Black', 'Sedan')
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
# print(car_object)

# # test for basic search function in DB class
# # should return list of cars containing all cars except Vehicle with CarID = 2
# inventory = dbu.search_database('2024-02-10','2024-02-12', 'SUV')

# for x in inventory:
    # print(x)
    
    
# print_tables.print_tables(username, password)

# dbu.update_report(1,'scratch on hood and on roof',None, None, None) #success
# print_tables.print_tables(username, password) 

# dbu.remove_report(1) #success
# print_tables.print_tables(username, password) 

# dbu.update_customer(4,None,'2003-06-23', 'nima.mona82@gmail.com') #success
# print_tables.print_tables(username, password)

# dbu.remove_customer(4) #success
# print_tables.print_tables(username, password)

# dbu.update_reservation(1, '2024-01-19', '2024-01-29', None, None, None) 
# print_tables.print_tables(username, password)
