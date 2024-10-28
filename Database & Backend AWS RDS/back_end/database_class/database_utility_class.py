import pyodbc
    
# Error Checks might be better handled by the calling class
# Instead of this class handling it

"""
# Function: initialize_connectio(
# Input: None
# Output: None
# Description: initializes the connection to database, must be called
#               in application startup. 
"""
def initialize_connection(username: str, upassword: str) -> None:
    # username = input("Enter your SQL Server Username: ")
    # upassword = input("Enter your SQL Server Password: ")

    # Creates global variables mydb and mycursor
    # for other functions to use
    global mydb, mycursor
    
    rds_endpoint = "jenni-database.czg446yqs8iz.us-west-1.rds.amazonaws.com"
    db_name = "Jenni-Database"  # Ensure the name matches what you want to create
    port = 1433
    

    connection_string = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={rds_endpoint},{port};'
        f'DATABASE={db_name};'
        f'UID={username};PWD={upassword};'
    )

    mydb = pyodbc.connect(connection_string)
    mycursor = mydb.cursor()

"""
# Description: function to add a singular car to MySQL.
#               prints out the CarID number assigned to it by MySQL     
# Input: uVIN, a string - Car's VIN number
#        uMileage, an integer - Car's Mileage
#        uMPG, an integer - Car's miles/gallon
#        uPrice, a decimal/float - Car's price per day
#        uIsActive, 0 or 1 - If car is retired or not
#        uLicensePlate, a string - Car's license plate
# Output: None
"""
def add_car(uVIN: str, uMileage: int, uMPG: int, uPrice: float, uLicensePlate: str,
            uCarYear: int, uModel: str, uMake: str, uColor: str, uCarType: str)-> None:
    sql_insert_vehicle = "insert into Vehicles (VIN, Mileage, MPG, Price, LicensePlate, CarYear, Model, Make, Color, CarType) \
                            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    vehicle_value = (uVIN, uMileage, uMPG, uPrice, uLicensePlate, uCarYear, uModel, uMake, uColor, uCarType)
    
    mycursor.execute(sql_insert_vehicle, vehicle_value)
    mydb.commit()
    
    """ do error checks in the inventory_class itself? """

"""
# Description: function to get assigned CarID number by MySQL
# Input: uVIN, a string - Car's VIN
# Output: carID, an integer
"""
def get_car_id(uVIN: str) -> int:
    select_prompt = "select CarID from Vehicles where VIN = ?"
    mycursor.execute(select_prompt, [uVIN])
    result = mycursor.fetchone()
    
    if result:
        return result[0]
    else:
        return None

"""
# might not be needed???
# Description: function to get a car's info from MySQL through CarID
# Input: CarID, an integer
# Output: tuple of the following values:
#           CarID, VIN, Mileage, MPG, Price, IsActive, LicensePlate    
"""
def get_car_info(car_id: int) -> tuple:
    select_prompt = "select * from Vehicles where CarID = ?"
    mycursor.execute(select_prompt, [car_id])
    result = mycursor.fetchone()
    
    return result

"""
# Description: function to change Mileage
# Input: CarID, an integer
#        Mileage, an integer
# Output: None    
"""
def change_mileage(car_id: int, new_mileage: int) -> None:
    # need error check in the higher level function
    sql_update_mileage = "update Vehicles set Mileage = ? \
                        where CarId = ?"
    update_value = (new_mileage, car_id)
    
    mycursor.execute(sql_update_mileage, update_value)
    mydb.commit()

"""
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
"""
def get_inventory() -> list[tuple]:
    inventory = []
    
    sql_select_car = "select CarID, VIN, Mileage, MPG, Price, LicensePlate, CarYear, Model, Make, \
                        Color, CarType from Vehicles"
    mycursor.execute(sql_select_car)
    myresult = mycursor.fetchall()
    
    for x in myresult:
        inventory.append(x)
        
    return inventory

"""
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
"""
def get_active_inventory() -> list[tuple]:
    inventory = []
    mycursor.execute("select * from Vehicles where IsActive = 1")
    myresult = mycursor.fetchall()
    
    for x in myresult:
        inventory.append(x)
        
    return inventory

"""
# Function: deactivate_car()
# Input: car_id, integer 
# Output: None 
# Description: sets the IsActive field in database to 0, making it not active
"""
def deactivate_car(car_id: int) -> None:
    sql_retire_car = "update Vehicles set IsActive = ? where CarID = ?"
    value = (0, car_id)
    
    mycursor.execute(sql_retire_car, value)
    mydb.commit()

"""
# Function: insert_report(uDamages, uGasAmount, uCarID, uReservation)
# Input: uDamages, a string
#        uGasAmount, an integer
#        uCarID, an integer
#        uReservation, an integer
# Output: an integer
# Description: inserts a new row into database in table Reports and 
#               returns the assigned report_id by database
"""
def insert_report(uDamages: str, uGasAmount: int, uCarID: int, uReservation: int) -> int:
    sql_insert_report = "insert into Reports (Damages, GasAmount, Vehicle, ReservationID) \
                            values (?, ?, ?, ?)"
    report_values = (uDamages, uGasAmount, uCarID, uReservation)
    
    mycursor.execute(sql_insert_report, report_values)
    mydb.commit()
    
    mycursor.execute("SELECT SCOPE_IDENTITY()")
    
    myresult = mycursor.fetchone()
    
    return myresult[0]


def get_reports(car_id):
    reports = []
    sql_select_reports = "select * from Reports where Vehicle = ?"
    mycursor.execute(sql_select_reports, [car_id])
    
    myresult = mycursor.fetchall()
    for x in myresult:
        reports.append(x)
        
    return reports

"""
# update an existing reservation by ReservationID
# Input: ReservationID, an integer - ID of the reservation to update
#        StartDate, EndDate, Insurance, CustomerID, Vehicle, optional values to update
# Output: None        
"""
def update_reservation(uReservationID: int, uStartDate=None, uEndDate=None, uInsurance=None, uCustomerID=None, uVehicle=None) -> None:
    update_query = "UPDATE Reservations SET "
    update_values = []
    updates = []  # To collect the update clauses
    
    if uStartDate is not None:  # Check for None explicitly
        updates.append("StartDate = ?")
        update_values.append(uStartDate)
    if uEndDate is not None:  # Check for None explicitly
        updates.append("EndDate = ?")
        update_values.append(uEndDate)
    if uInsurance is not None:  # Check for None explicitly
        updates.append("Insurance = ?")
        update_values.append(uInsurance)
    if uCustomerID is not None:  # Check for None explicitly
        updates.append("CustomerID = ?")
        update_values.append(uCustomerID)
    if uVehicle is not None:  # Check for None explicitly
        updates.append("Vehicle = ?")
        update_values.append(uVehicle)
    
    if updates:
        update_query += ", ".join(updates) + " WHERE ReservationID = ?"
        update_values.append(uReservationID)
        
        # Execute the query
        mycursor.execute(update_query, tuple(update_values))
        mydb.commit()
        
        # For testing purposes
        print(f"Reservation {uReservationID} updated.")
    else:
        print("No updates were provided.")
    
"""
# remove an existing reservation
# Input: ReservationID, an integer - ID of the reservation to remove
# Output: None        
"""
def remove_reservation(uReservationID: int) -> None:
    delete_query = "DELETE FROM Reservations WHERE ReservationID = ?"
    mycursor.execute(delete_query, (uReservationID,))
    mydb.commit()
    
    # For testing purposes
    print(f"Reservation {uReservationID} has been removed.")

"""
# update an existing report by ReportID
# Input: ReportID, an integer - ID of the report to update
#        Damages, GasAmount, Vehicle, Customer, optional values to update
# Output: None
"""
def update_report(uReportID: int, uDamage=None, uGasAmount=None, uVehicle=None, uReservationID=None) -> None:
    update_query = "UPDATE Reports SET "
    update_values = []
    
    if uDamage:
        update_query += "Damages = ?, "
        update_values.append(uDamage)
    if uGasAmount:
        update_query += "GasAmount = ?, "
        update_values.append(uGasAmount)
    if uVehicle:
        update_query += "Vehicle = ?, "
        update_values.append(uVehicle)
    if uReservationID:
        update_query += "Customer = ?, "
        update_values.append(uReservationID)
        
    update_query = update_query.rstrip(', ') + " WHERE ReportID = ?"
    update_values.append(uReportID)
    
    mycursor.execute(update_query, tuple(update_values))
    mydb.commit()
    
    # For testing
    print(f"Report {uReportID} updated.")

"""
# remove an existing report
# Input: ReportID, an integer - ID of the report to remove
# Output: None
"""
def remove_report(uReportID: int) -> None:
    delete_query = "DELETE FROM Reports WHERE ReportID = ?"
    mycursor.execute(delete_query, (uReportID,))
    mydb.commit()
    
    # For testing
    print(f"Report {uReportID} has been removed.")
    
"""
#update an existing customer by CustomerID
# Input: CustomerID, an integer - ID of the customer to update
#        FullName, DOB, Email, optional values to update
# Output: None
"""
def update_customer(uCustomerID: int, uFullName=None, uDOB=None, uEmail=None) -> None:
    update_query = "UPDATE Customers SET "
    update_values = []
    
    if uFullName:
        update_query += "FullName = ?, "
        update_values.append(uFullName)
    if uDOB:
        update_query += "DOB = ?, "
        update_values.append(uDOB)
    if uEmail:
        update_query += "Email = ?, "
        update_values.append(uEmail)
        
    update_query = update_query.rstrip(', ') + " WHERE CustomerID = ?"
    update_values.append(uCustomerID)
    
    mycursor.execute(update_query, tuple(update_values))
    mydb.commit()
    
    # For testing
    print(f"Customer {uCustomerID} updated.")

"""
# Remove an existing customer
# Input: CustomerID, an integer - ID of the customer to remove
# Output: None
"""
def remove_customer(uCustomerID: int) -> None:
    # Delete the customer from the Customers table
    delete_customer_query = "DELETE FROM Customers WHERE CustomerID = ?"
    mycursor.execute(delete_customer_query, (uCustomerID,))
    
    # Commit all the changes
    mydb.commit()

    # Print confirmation
    print(f"Customer {uCustomerID} has been removed along with their reservations.")
    
"""
# Function: search(startDate, endDate)
# Input: startDate, a date with format yyyy-mm-dd
#        endDate, a date with format yyyy-mm-dd
# Output: list of tuples 
# Description: returns a list that contains tuples. Tuples
# in the list contains the information about cars that are available
# during the desired reservation period
"""
def search_database(start_date: str, end_date: str, car_type: str) -> list[tuple]:
    inventory = []
    sql_select_search = "select CarID, Mileage, MPG, Price, CarYear, Model, Make, Color, CarType from Vehicles \
                        where CarType = ? and \
                        CarId not in \
                        (select Vehicle from Reservations \
                        where ? < EndDate and \
                        ? > StartDate)"
    date_values = (car_type, start_date, end_date)
    
    mycursor.execute(sql_select_search, date_values)
    myresult = mycursor.fetchall()
    
    for car in myresult:
        inventory.append(car)
        
    return inventory

def get_vins():
    inventory = []
    sql_select_vins = "select VIN from Vehicles"
    mycursor.execute(sql_select_vins)
    myresult = mycursor.fetchall()
    
    for x in myresult:
        inventory.append(x[0])

    return inventory 

def insert_reservation(start_date: str, end_date: str, insurance: int, customer_id: int, car_id: int) -> int:
    sql_insert_reservation = "insert into Reservations (StartDate, EndDate, Insurance, CustomerID, Vehicle) \
                            values (?, ?, ?, ?, ?)"
    reservation_values = (start_date, end_date, insurance, customer_id, car_id)
    
    mycursor.execute(sql_insert_reservation, reservation_values)
    mydb.commit()
    
    mycursor.execute("SELECT SCOPE_IDENTITY()")
    
    myresult = mycursor.fetchone()
    
    return myresult[0]


def get_reports(car_id):
    reports = []
    sql_select_reports = "select * from Reports where Vehicle = ?"
    mycursor.execute(sql_select_reports, [car_id])
    
    myresult = mycursor.fetchall()
    for x in myresult:
        reports.append(x)
        
    return reports











