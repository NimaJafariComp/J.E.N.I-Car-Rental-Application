import class_database

my_username = input("Enter your MySQL username: ")
my_password = input("Enter your MySQL password: ")

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