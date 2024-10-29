import class_database
import print_tables 

my_username = "admin"
my_password = "JenniProject2024"



database_object = class_database.test(my_username, my_password)
database_object.add_car('JNKCV51EX4M613956', 1000, 25, 60.0, 1, '9YNH255')
database_object.add_car('JNKCV51EX4M613978', 1100, 30, 70.0, 1, '8YNH230')
database_object.add_car('JNKCV51EX4M613300', 1200, 40, 90.0, 1, '8YNH300')

carID1 = database_object.get_car_id('JNKCV51EX4M613956')

database_object.get_car_info(carID1)

carID2 = database_object.get_car_id('JNKCV51EX4M613978')

database_object.get_car_info(carID2)

carID3 = database_object.get_car_id('JNKCV51EX4M613300')

database_object.get_car_info(carID3)

carID4 = database_object.get_car_id('JNKCV51EX4M613366')

database_object.get_car_info(carID4)


print_tables.print_tables(my_username, my_password)
database_object.update_reservation(1, '2024-01-19', '2024-01-29', None, None, None) #success
print_tables.print_tables(my_username, my_password)


database_object.remove_reservation(1) #success
print_tables.print_tables(my_username, my_password) 

database_object.update_report(1,'scratch on hood and on roof',None, None, None) #success
print_tables.print_tables(my_username, my_password) 

database_object.remove_report(1) #success
print_tables.print_tables(my_username, my_password) 

database_object.update_customer(4,None,'2003-06-23', 'nima.mona82@gmail.com') #success
print_tables.print_tables(my_username, my_password)

database_object.remove_customer(4) #success
print_tables.print_tables(my_username, my_password)
