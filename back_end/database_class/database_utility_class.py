import mysql.connector
    
# Error Checks might be better handled by the calling class
# Instead of this class handling it

# Function: initialize_connectio()
# Input: None
# Output: None
# Description: initializes the connection to database, must be called
#               in application startup. 

def initialize_connection():
    username = input("Enter your MySQL Username: ")
    upassword = input("Enter your MySQL Password: ")

    # Creates global variables mydb and mycursor
    # for other functions to use
    global mydb, mycursor
    mydb = mysql.connector.connect(
        host = "localhost",
        user = username,
        password = upassword,
        database = "CarAppProject"
    )

    mycursor = mydb.cursor()


# Description: function to add a singular car to MySQL.
#               prints out the CarID number assigned to it by MySQL
# Input: uVIN, a string - Car's VIN number
#        uMileage, an integer - Car's Mileage
#        uMPG, an integer - Car's miles/gallon
#        uPrice, a decimal/float - Car's price per day
#        uIsActive, 0 or 1 - If car is retired or not
#        uLicensePlate, a string - Car's license plate
# Output: None

def add_car(uVIN, uMileage, uMPG, uPrice, uLicensePlate):
    sql_insert_vehicle = "insert into Vehicles (VIN, Mileage, MPG, Price, LicensePlate) \
                            values (%s, %s, %s, %s, %s)"
    vehicle_value = (uVIN, uMileage, uMPG, uPrice, uLicensePlate)
    
    mycursor.execute(sql_insert_vehicle, vehicle_value)
    mydb.commit()
    
    # do error checks in the inventory_class itself?

# Description: function to get assigned CarID number by MySQL
# Input: uVIN, a string - Car's VIN
# Output: carID, an integer

def get_car_id(uVIN):
    select_prompt = "select CarID from Vehicles where VIN = %s"
    mycursor.execute(select_prompt, [uVIN])
    result = mycursor.fetchone()
    
    if result:
        return result[0]
    else:
        return Nones

# might not be needed???
# Description: function to get a car's info from MySQL through CarID
# Input: CarID, an integer
# Output: list of the following values:
#           CarID, VIN, Mileage, MPG, Price, IsActive, LicensePlate    

def get_car_info(car_id):
    select_prompt = "select * from Vehicles where CarID = %s"
    mycursor.execute(select_prompt, [car_id])
    result = mycursor.fetchone()
    
    return result

# Description: function to change Mileage
# Input: CarID, an integer
#        Mileage, an integer
# Output: None    

def change_mileage(car_id, new_mileage):
    # need error check in the higher level function
    sql_update_mileage = "update Vehicles set Mileage = %s \
                        where CarId = %s"
    update_value = (new_mileage, car_id)
    
    mycursor.execute(sql_update_mileage, update_value)
    mydb.commit()
    
# add_vehicle_type and get_vehicle_type removed
# needs to change database table Vehicle to contain Vehicle Type

# Function: get_inventory()
# Input: None
# Output: list of tuples, each tuple consists of different fields
#           CarID, integer
#           VIN, string
#           Mileage, integer
#           MPG, integer
#           Price, float/decimal
#           LicensePlate, stiring
# Description: queries all rows from Vehicles table in database

def get_inventory():
    inventory = []
    
    sql_select_car = "select CarID, VIN, Mileage, MPG, Price, LicensePlate \
                        from Vehicles"
    mycursor.execute(sql_select_car)
    myresult = mycursor.fetchall()
    
    for x in myresult:
        inventory.append(x)
        
    return inventory

# Function: get_active_inventory()
# Input: None
# Output: list of tuples, each tuple consists of different fields
#           CarID, integer
#           VIN, string
#           Mileage, integer
#           MPG, integer
#           Price, float/decimal
#           LicensePlate, stiring
# Description: queries all rows from Vehicles table in database
#               where IsActive == 1

def get_active_inventory():
    inventory = []
    mycursor.execute("select * from Vehicles where IsActive = 1")
    myresult = mycursor.fetchall()
    
    for x in myresult:
        inventory.append(x)
        
    return inventory

# Function: deactivate_car()
# Input: car_id, integer 
# Output: None 
# Description: sets the IsActive field in database to 0, making it not active

def deactivate_car(car_id):
    sql_retire_car = "update Vehicles set IsActive = %s where CarID = %s"
    value = (0, car_id)
    
    mycursor.execute(sql_retire_car, value)
    mydb.commit()
    
# Function: insert_report(uDamages, uGasAmount, uCarID, uReservation)
# Input: uDamages, a string
#        uGasAmount, an integer
#        uCarID, an integer
#        uReservation, an integer
# Output: an integer
# Description: inserts a new row into database in table Reports and 
#               returns the assigned report_id by database

def insert_report(uDamages, uGasAmount, uCarID, uReservation):
    sql_insert_report = "insert into Reports (Damages, GasAmount, Vehicle, ReservationID) \
                            values (%s, %s, %s, %s)"
    report_values = (uDamages, uGasAmount, uCarID, uReservation)
    
    mycursor.execute(sql_insert_report, report_values)
    mydb.cursor()
    
    mycursor.execute("select last_insert_id()")
    
    myresult = mycursor.fetchone()
    
    return myresult[0]
    
# def get_reports(self, car_id):

# update an existing reservation by ReservationID
# Input: ReservationID, an integer - ID of the reservation to update
#        StartDate, EndDate, Insurance, CustomerID, Vehicle, optional values to update
# Output: None        

def update_reservation(uReservationID, uStartDate=None, uEndDate=None, uInsurance=None, uCustomerID=None, uVehicle=None):
    update_query = "UPDATE Reservation SET "
    update_values = []
    if uStartDate:
        update_query += "StartDate = %s, "
        update_values.apped(uStartDate)
    if uEndDate:
        update_query += "EndDate = %s. "
        update_values.append(uEndDate)
    if uInsurance:
        update_query += "Insurance = %s, "
        update_values.append(uInsurance)
    if uCustomerID:
        update_query += "CustomerID = %s, "
        update_values.append(uCustomerID)
    if uVehicle:
        update_query += "Vehicle = %s, "
        update_values.append(uVehicle)
        
    update_query = update.query.rstrip(', ') + " WHERE ReservationID = %s"
    update_values.append(uReservationID)
    
    mycursor.execute(update_query, tuple(update_values))
    mydb.commit()
    
    # For testing purposes
    print(f"Reservation {ReservationID} updated.")
    
    
# remove an existing reservation
# Input: ReservationID, an integer - ID of the reservation to remove
# Output: None        

def remove_reservation(uReservation):
    delete_query = "DELETE FROM Reservations WHERE ReservationID = %s"
    mycursor.execute(delete_query, (uReservationID,))
    mydb.commit()
    
    # For testing purposes
    print(f"Reservation {uReservationID} has been removed.")

# update an existing report by ReportID
# Input: ReportID, an integer - ID of the report to update
#        Damages, GasAmount, Vehicle, Customer, optional values to update
# Output: None

def update_report(uReportID, uDamage=None, uGasAmount=None, uVehicle=None, uReservationID=None):
    update_query = "UPDATE Reports SET "
    update_values = []
    
    if uDamages:
        update_query += "Damages = %s, "
        update_values.append(uDamages)
    if uGasAmount:
        update_query += "GasAmount = %s, "
        update_values.append(uGasAmount)
    if uVehicle:
        update_query += "Vehicle = %s, "
        update_values.append(uVehicles)
    if uReservationID:
        update_query += "Customer = %s, "
        update_values.append(uReservationID)
        
    update_query = update_query.rstrip(', ') + " WHERE ReportID = %s"
    update_values.append(uReportID)
    
    mycursor.execute(update_query, tuple(update_values))
    mydb.commit()
    
    # For testing
    print(f"Report {uReportID} updated.")

# remove an existing report
# Input: ReportID, an integer - ID of the report to remove
# Output: None

def remove_report(uReportID):
    delete_query = "DELETE FROM Reports WHERE ReportID = %s"
    mycursor.execute(delete_query, (uReportID,))
    mydb.commit()
    
    # For testing
    print(f"Report {uReportID} has been removed.")

#update an existing customer by CustomerID
# Input: CustomerID, an integer - ID of the customer to update
#        FullName, DOB, Email, optional values to update
# Output: None

def update_customer(uCustomerID, uFullName=None, uDOB=None, uEmail=None):
    update_query = "UPDATE Customers SET "
    update_values = []
    
    if uFullName:
        update_query += "FullName = %s, "
        update_values.append(uFullName)
    if uDOB:
        update_query += "DOB = %s, "
        update_values.append(uDOB)
    if uEmail:
        update_query += "Email = %s, "
        update_values.append(uEmail)
        
    update_query = update_query.rstrip(', ') + " WHERE CustomerID = %s"
    update_values.append(uCustomerID)
    
    mycursor.execute(update_query, tuple(update_values))
    mydb.commit()
    
    # For testing
    print(f"Customer {uCustomerID} updated.")
    
# Remove an existing customer
# Input: CustomerID, an integer - ID of the customer to remove
# Output: None

def remove_customer(uCustomerID):
    # Delete the customer from the Customers table
    delete_customer_query = "DELETE FROM Customers WHERE CustomerID = %s"
    mycursor.execute(delete_customer_query, (uCustomerID,))
    
    # Commit all the changes
    mydb.commit()

    # Print confirmation
    print(f"Customer {uCustomerID} has been removed along with their reservations.")

# Function: search(startDate, endDate)
# Input: startDate, a date with format yyyy-mm-dd
#        endDate, a date with format yyyy-mm-dd
# Output: list of tuples 
# Description: returns a list that contains tuples. Tuples
# in the list contains the information about cars that are available
# during the desired reservation period

def search_database(start_date, end_date):
    inventory = []
    sql_select_search = "select * from Vehicles where CarID not in \
                        (select Vehicle from Reservations where \
                        %s < EndDate and %s > StartDate)"
    date_values = (start_date, end_date)
    
    mycursor.execute(sql_select_search, date_values)
    myresult = mycursor.fetchall()
    
    for car in myresult:
        inventory.append(car)
        
    return inventory












