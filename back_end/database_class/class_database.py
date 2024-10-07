import mysql.connector

class test:
    
    # Description: initilization function
    # Input: my_username, a string
    #        my_password, a string
    # Output: None
    def __init__(self, my_username, my_password):
        self.username = my_username
        self.password = my_password
        self.mydb = None
    
    # Description: function to connect to MySQL
    # Input: None
    # Output: None
    def connect_to_mysql(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = self.username,
            password = self.password,
            database = "carappproject"
        )
        
    # Description: function to add a singular car to MySQL.
    #               prints out the CarID number assigned to it by MySQL
    # Input: uVIN, a string - Car's VIN number
    #        uMileage, an integer - Car's Mileage
    #        uMPG, an integer - Car's miles/gallon
    #        uPrice, a decimal/float - Car's price per day
    #        uIsActive, 0 or 1 - If car is retired or not
    #        uLicensePlate, a string - Car's license plate
    # Output: None
    def add_car(self, uVIN, uMileage, uMPG, uPrice, uIsActive, uLicensePlate):
        
        existing_car_id = self.get_car_id(uVIN) #checking if car exists already
        if existing_car_id is not None: 
            print(f"Car with VIN {uVIN} already exists with CarID: {existing_car_id}.")
            return
    
        sql_insert_vehicle = "insert into Vehicles (VIN, Mileage, MPG, Price, IsActive, LicensePlate) values (%s, %s, %s, %s, %s, %s)"
        print(f"Car with VIN {uVIN} added to database with CarID: {existing_car_id}.")
        vehicle_value = (uVIN, uMileage, uMPG, uPrice, uIsActive, uLicensePlate)
        
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        mycursor.execute(sql_insert_vehicle, vehicle_value)
        self.mydb.commit()
        
        select_prompt = "select CarID from Vehicles where VIN = %s"
        adr = (uVIN, )
        mycursor.execute(select_prompt, adr)
        for x in mycursor:
            print("CarID is: ", x)
        
        
    # Description: function to get assigned CarID number by MySQL
    # Input: uVIN, a string - Car's VIN
    # Output: carID, an integer 
    def get_car_id(self, uVIN):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        select_prompt = "select CarID from Vehicles where VIN = %s"
        adr = [uVIN]
        mycursor.execute(select_prompt, adr)
        result = mycursor.fetchone()
        if result:
            print("CarID is:", result[0])
            return result[0]
        else:
            print(f"Car with VIN {uVIN} doesnt exist in database")
            return None 
        
        for x in mycursor:
            print("CarID is: ", x[0])
            carID = x[0]
            
       
    
    # Description: function to get a car's info from MySQL through CarID
    # Input: CarID, an integer
    # Output: list of the following values:
    #           CarID, VIN, Mileage, MPG, Price, IsActive, LicensePlate
    def get_car_info(self, CarID):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        select_prompt = "select * from Vehicles where CarID = %s"
        adr = [CarID]
        mycursor.execute(select_prompt, adr)
        for x in mycursor:
            print(x)
            
    
    # def add_car_type(CarYear, Model, Make, Color, CarType, CarID):
        # pass

    # Description: function to update Mileage
    # Input: CarID, an integer
    #        Mileage, an integer
    # Output: None
    def change_mileage(self, CarID, updated_mileage):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        sql_update_mileage = "update Vehicles set Mileage = %s where CarID = %s"
        update_values = (updated_mileage, CarID)
        
        mycursor.execute(sql_update_mileage, update_values)
        self.mydb.commit()

 # Function: add_vehicle_type(self, u_car_year, u_model, u_make, u_color, u_car_type)
    # Description: function to add Vehicle Type to database associated with
    #              the newly added car
    # Input: u_car_year, a year with format yyyy
    #        u_model, a string
    #        u_make, a string
    #        u_color, a string
    #        u_car_type, a string
    # Output: None
    def add_vehicle_type(self, u_car_year, u_model, u_make, u_color, u_car_type, car_id):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        sql_insert_vehicle_type = "insert into VehicleType (CarYear, Model, Make, Color, CarType, CarId) values (%s, %s, %s, %s, %s, %s)"
        vehicle_type_value = (u_car_year, u_model, u_make, u_color, u_car_type, car_id)
        
        mycursor.execute(sql_insert_vehicle_type, vehicle_type_value)
        self.mydb.commit()
        
    def get_vehicle_type(self, car_id):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        select_prompt = "select * from VehicleType where CarID = %s"
        mycursor.execute(select_prompt, [car_id])
        result = mycursor.fetchone()
        
        return result
        
    def get_inventory(self):
        inventory = []
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        mycursor.execute("select CarID, VIN, Mileage, MPG, Price, LicensePlate from Vehicles")
        myresult = mycursor.fetchall()
        
        for x in myresult:
            inventory.append(x)
        
        return inventory
        
    def get_active_inventory(self):
        inventory = []
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        mycursor.execute("select * from Vehicles where IsActive = 1")
        myresult = mycursor.fetchall()
        
        for x in myresult:
            inventory.append(x)
        
        return inventory
        
    def retire_car(self, car_id):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        sql_retire_car = "update Vehicles set IsActive = %s where CarID = %s"
        value = (0, car_id)
        
        mycursor.execute(sql_retire_car, value)
        self.mydb.commit()
