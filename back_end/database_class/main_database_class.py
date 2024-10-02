import class_database

my_username = input("Enter your MySQL username: ")
my_password = input("Enter your MySQL password: ")

database_object = class_database.test(my_username, my_password)
# adding_car.add_car('JNKCV51EX4M613956', 1000, 25, 60.0, 1, '9YNH255')

carID = database_object.get_car_id('JNKCV51EX4M613956')

database_object.get_car_info(carID)
