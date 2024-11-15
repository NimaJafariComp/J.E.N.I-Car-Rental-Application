import mysql.connector
from datetime import datetime
    
# Error Checks might be better handled by the calling class
# Instead of this class handling it

def initialize_connection(my_host: str, my_port: str, username: str, upassword: str) -> None:
    
    """
    Initializes the connetion to database, must be called in application startup
    
    Parameters
    ----------
    my_host: str
        The hosting server for the AWS database
    my_port: int
        Port being used to connect MySQL and AWS
    username: str
        AWS Account username
    password: str
        AWS Account password    
    
    Returns
    -------
    None
    
    """
    global mydb, mycursor
    mydb = mysql.connector.connect(
        host = my_host,
        user = username,
        password = upassword,
        port = my_port,
        database = "CARAPP"
    )
    
    mycursor = mydb.cursor()


def add_car(vin: str, mileage: int, mpg: int, price: float, license_plate: str, car_year: str, car_model: str, car_make: str, car_color: str, car_type: str)-> None:
    sql_insert_vehicle = "insert into Vehicles (VIN, Mileage, MPG, Price, LicensePlate, CarYear, Model, Make, Color, CarType) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    vehicle_value = (vin, mileage, mpg, price, license_plate, car_year, car_model, car_make, car_color, car_type)
    mycursor.execute(sql_insert_vehicle, vehicle_value)
    mydb.commit()
    """
    Function to add a singular car to database
    
    Parameters
    ----------
    vin: str
        The unique VIN number of the vehicle to be added.
    mileage: int
        The current mileage of the car.
    mpg: int
        The current miles per gallon of the car.
    price: double
        The price that is assigned for the car. Unit is $/day.
    license_plate: str
        The unique license plate of the vehicle to be added 
    car_year: str
        The year of the model of the vehicle
    car_model: str
        The model of the car. i.e. Corolla, Civic, and Prius
    car_make: str
        The brand of the car. i.e. Toyota and Honda 
    car_color: str
        The color of the car. i.e. Red, Blue, and Yellow
    car_type: str
        The classification of the car. i.e. Sedan, SUV, and Truck
    
    Returns
    -------
    None
    """


def get_car_id(vin: str) -> int:
    select_prompt = "select CarID from Vehicles where VIN = %s"
    mycursor.execute(select_prompt, [vin])
    result = mycursor.fetchone()
    
    if result:
        return result[0]
    else:
        return None
    """
    Function to get assigned CarID number by database
    
    Parameters
    ----------
    vin: str
        The unique VIN number of the vehicle
    
    Returns
    -------
    int
        The car ID assigned by the database
    
    """

"""
# might not be needed???
# Description: function to get a car's info from MySQL through CarID
# Input: CarID, an integer
# Output: tuple of the following values:
#           CarID, VIN, Mileage, MPG, Price, IsActive, LicensePlate    
"""
def get_car_info(car_id: int) -> tuple:
    """
    Function to get a car's information from database through car ID
    
    Parameters
    ----------
    car_id: int
        The car ID of the car
    
    Returns
    -------
    """
    select_prompt = "select * from Vehicles where CarID = %s"
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
    sql_update_mileage = "update Vehicles set Mileage = %s \
                        where CarId = %s"
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
    sql_retire_car = "update Vehicles set IsActive = %s where CarID = %s"
    value = (0, car_id)
    
    mycursor.execute(sql_retire_car, value)
    mydb.commit()

"""
# Function: insert_report(damages, gas_amount, car_id, reservation_id)
# Input: damages, a string
#        gas_amount, an integer
#        car_id, an integer
#        reservation_id, an integer
# Output: an integer
# Description: inserts a new row into database in table Reports and 
#               returns the assigned report_id by database
"""
def insert_report(damages: str, gas_amount: int, car_id: int, reservation_id: int) -> int:
    sql_insert_report = "insert into Reports (Damages, GasAmount, Vehicle, ReservationID) \
                            values (%s, %s, %s, %s)"
    report_values = (damages, gas_amount, car_id, reservation_id)
    
    mycursor.execute(sql_insert_report, report_values)
    mydb.commit()
    
    mycursor.execute("select last_insert_id()")
    
    myresult = mycursor.fetchone()
    
    return myresult[0]


def get_reports(car_id):
    reports = []
    sql_select_reports = "select * from Reports where Vehicle = %s"
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
def update_reservation(reservation_id: int, start_date=None, end_date=None, insurance=None, customer_id=None, uVehicle=None) -> None:
    update_query = "UPDATE Reservations SET "
    update_values = []
    if start_date:
        update_query += "StartDate = %s, "
        update_values.append(start_date)
    if end_date:
        update_query += "EndDate = %s, "
        update_values.append(end_date)
    if insurance:
        update_query += "Insurance = %s, "
        update_values.append(insurance)
    if customer_id:
        update_query += "CustomerID = %s, "
        update_values.append(customer_id)
    if uVehicle:
        update_query += "Vehicle = %s, "
        update_values.append(uVehicle)
        
    update_query = update_query.rstrip(', ') + " WHERE ReservationID = %s"
    update_values.append(reservation_id)
    
    mycursor.execute(update_query, tuple(update_values))
    mydb.commit()
    
    # For testing purposes
    print(f"Reservation {reservation_id} updated.")
    
"""
# remove an existing reservation
# Input: ReservationID, an integer - ID of the reservation to remove
# Output: None        
"""
def remove_reservation(reservation_id: int) -> None:
    delete_query = "DELETE FROM Reservations WHERE ReservationID = %s"
    mycursor.execute(delete_query, (reservation_id,))
    mydb.commit()
    
    # For testing purposes
    print(f"Reservation {reservation_id} has been removed.")

"""
# update an existing report by ReportID
# Input: ReportID, an integer - ID of the report to update
#        Damages, GasAmount, Vehicle, Customer, optional values to update
# Output: None
"""
def update_report(report_id: int, damages=None, gas_amount=None, car_id=None, reservation_id=None) -> None:
    update_query = "UPDATE Reports SET "
    update_values = []
    
    if damages:
        update_query += "Damages = %s, "
        update_values.append(damages)
    if gas_amount:
        update_query += "GasAmount = %s, "
        update_values.append(gas_amount)
    if car_id:
        update_query += "Vehicle = %s, "
        update_values.append(car_id)
    if reservation_id:
        update_query += "ReservationID = %s, "
        update_values.append(reservation_id)
        
    update_query = update_query.rstrip(', ') + " WHERE ReportID = %s"
    update_values.append(report_id)
    
    mycursor.execute(update_query, tuple(update_values))
    mydb.commit()
    
    # For testing
    print(f"Report {report_id} updated.")

"""
# remove an existing report
# Input: ReportID, an integer - ID of the report to remove
# Output: None
"""
def remove_report(report_id: int) -> None:
    delete_query = "DELETE FROM Reports WHERE ReportID = %s"
    mycursor.execute(delete_query, (report_id,))
    mydb.commit()
    
    # For testing
    print(f"Report {report_id} has been removed.")
    
"""
#update an existing customer by CustomerID
# Input: CustomerID, an integer - ID of the customer to update
#        FullName, DOB, Email, optional values to update
# Output: None
"""
def update_customer(customer_id: int, full_name=None, dob=None, email=None) -> None:
    update_query = "UPDATE Customers SET "
    update_values = []
    
    if full_name:
        update_query += "FullName = %s, "
        update_values.append(full_name)
    if dob:
        update_query += "DOB = %s, "
        update_values.append(dob)
    if email:
        update_query += "Email = %s, "
        update_values.append(email)
        
    update_query = update_query.rstrip(', ') + " WHERE CustomerID = %s"
    update_values.append(customer_id)
    
    mycursor.execute(update_query, tuple(update_values))
    mydb.commit()
    
    # For testing
    print(f"Customer {customer_id} updated.")

"""
# Remove an existing customer
# Input: CustomerID, an integer - ID of the customer to remove
# Output: None
"""
def remove_customer(customer_id: int) -> None:
    # Delete the customer from the Customers table
    delete_customer_query = "DELETE FROM Customers WHERE CustomerID = %s"
    mycursor.execute(delete_customer_query, (customer_id,))
    
    # Commit all the changes
    mydb.commit()

    # Print confirmation
    print(f"Customer {customer_id} has been removed along with their reservations.")
    
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
                        where CarType = %s and \
                        CarId not in \
                        (select Vehicle from Reservations \
                        where %s < EndDate and \
                        %s > StartDate)"
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

def insert_reservation(start_date: str, end_date: str, insurance: bool, customer_email: str, car_id: int) -> int:
    sql_insert_reservation = "insert into Reservations (StartDate, EndDate, Insurance, CustomerEmail, Vehicle) \
                            values (%s, %s, %s, %s, %s)"
    reservation_values = (start_date, end_date, insurance, customer_email, car_id)
    
    mycursor.execute(sql_insert_reservation, reservation_values)
    mydb.commit()
    
    mycursor.execute("select last_insert_id()")
    
    myresult = mycursor.fetchone()
    
    return myresult[0]


def get_reports(car_id):
    reports = []
    sql_select_reports = "select * from Reports where Vehicle = %s"
    mycursor.execute(sql_select_reports, [car_id])
    
    myresult = mycursor.fetchall()
    for x in myresult:
        reports.append(x)
        
    return reports

def calculate_days(start_date: str, end_date: str) -> int:
    
    """
    Calculate the number of days
    Args:
        start_date YYYY-MM-DD
        end_date YYYY-MM-DD
    Returns:
        Number of days between the two dates 
        Returns -1 if error
    """
    try:
        # Convert string inputs to datetime objects
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        
        # Calculate the difference in days
        delta = (end - start).days
        
        # Ensure valid date range
        if delta < 0:
            print("Error: wrong start and end date")
            return -1
        
        return delta
    
    except ValueError as e:
        print(f"Invalid date format: {e}")
        return -1

def get_customer_info(customer_id: int) -> dict:
    select_prompt = "SELECT CustomerID, FullName, DOB, Email FROM Customers WHERE CustomerID = %s"
    mycursor.execute(select_prompt, (customer_id,))
    result = mycursor.fetchone()
    
    if result:
        # Create a dictionary for the customer info
        customer_info = {
            'CustomerID': result[0],
            'FullName': result[1],
            'DOB': result[2],
            'Email': result[3]
        }
        return customer_info
    else:
        return None

def get_reservations():
    reservations = []
    sql_select_reservations = "select * from Reservations"
    mycursor.execute(sql_select_reservations)
    
    myresult = mycursor.fetchall()
    for x in myresult:
        reservations.append(x)
    
    return reservations


def get_hashed_password(login_id: int, person_type: str) -> str:
    if(person_type.lower() == "customer"):
        sql_select_password = "select Password from Customers where CustomerID = %s"
    elif(person_type.lower() == "admin"):
        sql_select_password = "select Password from Administrator where AdminID = %s"
    
    mycursor.execute(sql_select_password, [login_id])
    result = mycursor.fetchone()
    
    return result

def admin_sign_up(name: str, email: str, password: str) -> None:
    sql_insert_admin = "insert into Administrator (User, Email, Password) values (%s, %s, %s)"
    admin_values = (name, email, password)
    
    mycursor.execute(sql_insert_admin, admin_values)
    mydb.commit()