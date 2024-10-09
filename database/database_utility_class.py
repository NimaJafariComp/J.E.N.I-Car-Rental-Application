import mysql.connector

class DBUtils:

    @staticmethod
    def initialize_connection():
        username = input("Enter your MySQL Username: ")
        upassword = input("Enter your MySQL Password: ")

        global mydb, mycursor
        mydb = mysql.connector.connect(
            host = "localhost",
            user = username,
            password = upassword,
            database = "CarAppProject"
        )

        mycursor = mydb.cursor()
       

    @staticmethod
    def add_car(uVIN, uMileage, uMPG, uPrice, uLicensePlate):
        sql_insert_vehicle = "insert into Vehicles (VIN, Mileage, MPG, Price, LicensePlate) \
                                values (%s, %s, %s, %s, %s)"
        vehicle_value = (uVIN, uMileage, uMPG, uPrice, uLicensePlate)
        
        mycursor.execute(sql_insert_vehicle, vehicle_value)
        mydb.commit()
        
        # do error checks in the inventory_class itself?
        return mycursor.fetchone()[0]

    @staticmethod
    def get_car_id(uVIN):
        select_prompt = "select CarID from Vehicles where VIN = %s"
        mycursor.execute(select_prompt, [uVIN])
        result = mycursor.fetchone()
        
        if result:
            return result[0]
        else:
            return Nones
    
    # might not be needed???
    @staticmethod
    def get_car_info(car_id):
        select_prompt = "select * from Vehicles where CarID = %s"
        mycursor.execute(select_prompt, [car_id])
        result = mycursor.fetchone()
        
        return result
    
    @staticmethod
    def change_mileage(car_id, new_mileage):
        # need error check in the higher level function
        sql_update_mileage = "update Vehicles set Mileage = %s \
                            where CarId = %s"
        update_value = (new_mileage, car_id)
        
        mycursor.execute(sql_update_mileage, update_value)
        mydb.commit()
        
    # add_vehicle_type and get_vehicle_type removed
    # needs to change database table Vehicle to contain Vehicle Type
    
    @staticmethod
    def get_inventory():
        inventory = []
        
        sql_select_car = "select CarID, VIN, Mileage, MPG, Price, LicensePlate \
                            from Vehicles"
        mycursor.execute(sql_select_car)
        myresult = mycursor.fetchall()
        
        for x in myresult:
            inventory.append(x)
            
        return inventory

    @staticmethod
    def get_active_inventory():
        inventory = []
        mycursor.execute("select * from Vehicles where IsActive = 1")
        myresult = mycursor.fetchall()
        
        for x in myresult:
            inventory.append(x)
            
        return inventory
        
    @staticmethod
    def deactivate_car(car_id):
        sql_retire_car = "update Vehicles set IsActive = %s where CarID = %s"
        value = (0, car_id)
        
        mycursor.execute(sql_retire_car, value)
        mydb.commit()
        
    @staticmethods
    def insert_report(uDamages, uGasAmount, uCarID, uReservation):
        sql_insert_report = "insert into Reports (Damages, GasAmount, Vehicle, ReservationID) \
                                values (%s, %s, %s, %s)"
        report_values = (uDamages, uGasAmount, uCarID, uReservation)
        
        mycursor.execute(sql_insert_report, report_values)
        mydb.cursor()
        
        mycursor.execute("select last_insert_id()")
        
        myresult = mycursor.fetchone()
        
        return myresult[0]