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
    def update_mileage(self, CarID, updated_mileage):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        sql_update_mileage = "update Vehicles set Mileage = %s where CarID = %s"
        update_values = (updated_mileage, CarID)
        
        mycursor.execute(sql_update_mileage, update_values)
        self.mydb.commit()
        
    
    # update an existing reservation by ReservationID
    # Input: ReservationID, an integer - ID of the reservation to update
    #        StartDate, EndDate, Insurance, CustomerID, Vehicle, optional values to update
    # Output: None
    def update_reservation(self, ReservationID, StartDate=None, EndDate=None, Insurance=None, CustomerID=None, Vehicle=None):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        update_query = "UPDATE Reservations SET "
        update_values = []
        if StartDate:
            update_query += "StartDate = %s, "
            update_values.append(StartDate)
        if EndDate:
            update_query += "EndDate = %s, "
            update_values.append(EndDate)
        if Insurance is not None:
            update_query += "Insurance = %s, "
            update_values.append(Insurance)
        if CustomerID:
            update_query += "CustomerID = %s, "
            update_values.append(CustomerID)
        if Vehicle:
            update_query += "Vehicle = %s, "
            update_values.append(Vehicle)
        
        update_query = update_query.rstrip(', ') + " WHERE ReservationID = %s"
        update_values.append(ReservationID)
        
        mycursor.execute(update_query, tuple(update_values))
        self.mydb.commit()
        print(f"Reservation {ReservationID} updated.")
        
        
    
    # remove an existing reservation
    # Input: ReservationID, an integer - ID of the reservation to remove
    # Output: None
    def remove_reservation(self, ReservationID):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        delete_query = "DELETE FROM Reservations WHERE ReservationID = %s"
        mycursor.execute(delete_query, (ReservationID,))
        self.mydb.commit()
        print(f"Reservation {ReservationID} has been removed.")
    
    
    
    # update an existing report by ReportID
    # Input: ReportID, an integer - ID of the report to update
    #        Damages, GasAmount, Vehicle, Customer, optional values to update
    # Output: None
    def update_report(self, ReportID, Damages=None, GasAmount=None, Vehicle=None, Customer=None):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        update_query = "UPDATE Reports SET "
        update_values = []
        if Damages:
            update_query += "Damages = %s, "
            update_values.append(Damages)
        if GasAmount:
            update_query += "GasAmount = %s, "
            update_values.append(GasAmount)
        if Vehicle:
            update_query += "Vehicle = %s, "
            update_values.append(Vehicle)
        if Customer:
            update_query += "Customer = %s, "
            update_values.append(Customer)
        
        update_query = update_query.rstrip(', ') + " WHERE ReportID = %s"
        update_values.append(ReportID)
        
        mycursor.execute(update_query, tuple(update_values))
        self.mydb.commit()
        print(f"Report {ReportID} updated.")
    
    
    # remove an existing report
    # Input: ReportID, an integer - ID of the report to remove
    # Output: None
    def remove_report(self, ReportID):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        delete_query = "DELETE FROM Reports WHERE ReportID = %s"
        mycursor.execute(delete_query, (ReportID,))
        self.mydb.commit()
        print(f"Report {ReportID} has been removed.")
        
    
    
    #update an existing customer by CustomerID
    # Input: CustomerID, an integer - ID of the customer to update
    #        FullName, DOB, Email, optional values to update
    # Output: None
    def update_customer(self, CustomerID, FullName=None, DOB=None, Email=None):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()
        
        update_query = "UPDATE Customers SET "
        update_values = []
        if FullName:
            update_query += "FullName = %s, "
            update_values.append(FullName)
        if DOB:
            update_query += "DOB = %s, "
            update_values.append(DOB)
        if Email:
            update_query += "Email = %s, "
            update_values.append(Email)
        
        update_query = update_query.rstrip(', ') + " WHERE CustomerID = %s"
        update_values.append(CustomerID)
        
        mycursor.execute(update_query, tuple(update_values))
        self.mydb.commit()
        print(f"Customer {CustomerID} updated.")
        
    
    # Remove an existing customer
    # Input: CustomerID, an integer - ID of the customer to remove
    # Output: None
    def remove_customer(self, CustomerID):
        self.connect_to_mysql()
        mycursor = self.mydb.cursor()

        # Delete the customer from the Customers table
        delete_customer_query = "DELETE FROM Customers WHERE CustomerID = %s"
        mycursor.execute(delete_customer_query, (CustomerID,))
        
        # Commit all the changes
        self.mydb.commit()

        # Print confirmation
        print(f"Customer {CustomerID} has been removed along with their reservations and reports.")








