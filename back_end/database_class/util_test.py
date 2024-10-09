import database_utility_class as dbu
import car_class as cc

dbu.DBUtils.initialize_connection()
dbu.DBUtils.add_car('4T1BF1FK3EU338253', 100, 50, 250.00, '7IVQ651')
dbu.DBUtils.add_car('1FTWW31P95EB34131', 600, 35, 150.00, '7KJV101')
dbu.DBUtils.add_car('4T1BF1FK3EU338251', 100, 50, 250.00, '7IVQ653')
car1 = dbu.DBUtils.get_car_id('4T1BF1FK3EU338253')
car2 = dbu.DBUtils.get_car_id('1FTWW31P95EB34131')
car3 = dbu.DBUtils.get_car_id('4T1BF1FK3EU338251')


for x in (car1, car2, car3):
    print(x)

car_object = cc.car('4T1BF1FK3EU338253', 100, 50, 250.00, '7IVQ651')
car_object.set_car_id(6)
car_object.update_mileage(200)