import database_utility_class as dbu
import car_class as cc

dbu.initialize_connection()
dbu.add_car('4T1BF1FK3EU338253', 100, 50, 250.00, '7IVQ651', '1999', 'E-Class', 'Mercedes-Benz', 'Black', 'Sedan')
dbu.add_car('1FTWW31P95EB34131', 600, 35, 150.00, '7KJV101', '2014', '200', 'Chrysler', 'Black', 'Sedan')
dbu.add_car('4T1BF1FK3EU338251', 100, 50, 250.00, '7IVQ653', '2011', 'Juke', 'Nissan', 'Red', 'Hatchback')
car1 = dbu.get_car_id('4T1BF1FK3EU338253')
car2 = dbu.get_car_id('1FTWW31P95EB34131')
car3 = dbu.get_car_id('4T1BF1FK3EU338251')


for x in (car1, car2, car3):
    print(x)

car_object = cc.car('4T1BF1FK3EU338253', 100, 50, 250.00, '7IVQ651', '1999', 'E-Class', 'Mercedes-Benz', 'Black', 'Sedan')
car_object.set_car_id(6)
car_object.update_mileage(400)

car_object.update_mileage(700)

# test for basic search function in DB class
# should return list of cars containing all cars except Vehicle with CarID = 2
inventory = dbu.search_database('2024-02-10','2024-02-12')

for x in inventory:
    print(x)