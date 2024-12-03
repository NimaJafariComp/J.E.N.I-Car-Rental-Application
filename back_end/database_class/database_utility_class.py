import mysql.connector
from datetime import datetime
global mydb, mycursor
"""
Date of Creation: October 1, 2024
Author: Elijah Sagaran and Nima Jafari
"""
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
    
    Author: Elijah Sagaran, 10/1
    Updates:
    """
    global mycursor, mydb
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
    
    Author: Elijah Sagaran, 10/1
    Updates:
        Nima Jafari, 10/2
        
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
    
    Author: Elijah Sagaran, 10/1
    Updates:
        Nima Jafari, 10/2
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
    tuple:
        contains the car's information
    
    Author: Elijah Sagaran, 10/1
    Updates:
    """
    select_prompt = "select * from Vehicles where CarID = %s"
    mycursor.execute(select_prompt, [car_id])
    result = mycursor.fetchone()
    
    return result

def change_mileage(car_id: int, new_mileage: int) -> None:
    """
    Function to change the value at column Mileage for the car with id car_id
    
    Parameters
    ----------
    car_id: int
        The car ID of the car
    new_mileage: int
        The new value of mileage
    
    Returns
    -------
    None
    
    Author: Elijah Sagaran, 10/2
    Updates:
        Nima Jafari, 10/2
        Elijah Sagaran, 10/7
    """
    sql_update_mileage = "update Vehicles set Mileage = %s \
                        where CarId = %s"
    update_value = (new_mileage, car_id)
    
    mycursor.execute(sql_update_mileage, update_value)
    mydb.commit()


def get_inventory() -> list[tuple]:
    """
    Queries all rows from Vehicles table in database
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list[tuple]:
        each tuple contains all the information about a car that is stored in the database
    
    Author: Elijah Sagaran, 10/7
    Updates:
        
    """
    inventory = []
    
    sql_select_car = "select CarID, VIN, Mileage, MPG, Price, LicensePlate, CarYear, Model, Make, \
                        Color, CarType from Vehicles"
    mycursor.execute(sql_select_car)
    myresult = mycursor.fetchall()
    
    for x in myresult:
        inventory.append(x)
        
    return inventory

def get_active_inventory() -> list[tuple]:
    """
    Queries all rows that is not retired from Vehicles table in database
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list[tuple]:
        each tuple contains all the information about a car that is stored in the database
    
    Author: Elijah Sagaran, 10/7
    Updates:
        
    """
    inventory = []
    mycursor.execute("select * from Vehicles where IsActive = 1")
    myresult = mycursor.fetchall()
    
    for x in myresult:
        inventory.append(x)
        
    return inventory

def deactivate_car(car_id: int) -> None:
    """
    Sets the IsActive field in databse to 0, making the car inactive
    
    Parameters
    ----------
    car_id: int
        The ID of the car
    
    Returns
    -------
    None
    
    Author: Elijah Sagaran, 10/7
    Updates:
        
    """
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
def update_reservation(reservation_id: int, start_date=None, end_date=None, insurance=None, customer_id=None, uVehicle=None, canceled=None, total_price=None) -> None:
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
    if canceled:
        update_query += "Canceled = %s, "
        update_values.append(canceled)
    if total_price:
        update_query += "TotalPrice = %s, "
        update_values.append(total_price)
        
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
    sql_select_search = "select CarID, Mileage, MPG, Price, CarYear, Model, Make, Color, CarType, VIN from Vehicles \
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
    """
    Retrieve a list of all Vehicle Identification Numbers (VINs) from the database.

    @return list - A list of VINs.
    """
    inventory = []
    sql_select_vins = "select VIN from Vehicles"
    mycursor.execute(sql_select_vins)
    myresult = mycursor.fetchall()
    
    for x in myresult:
        inventory.append(x[0])

    return inventory 

def insert_reservation(start_date: str, end_date: str, insurance: bool, customer_email: str, car_id: int, canceled: bool, total_price: float) -> int:
    """
    Insert a new reservation into the database.

    @param start_date: str - Reservation start date in 'YYYY-MM-DD' format.
    @param end_date: str - Reservation end date in 'YYYY-MM-DD' format.
    @param insurance: bool - Indicates if insurance is included.
    @param customer_email: str - Customer's email address.
    @param car_id: int - ID of the reserved car.
    @param canceled: bool - Indicates if the reservation is canceled.
    @param total_price: float - total price for reservation, initially 0 to be calculated
    @return int - The ID of the newly created reservation.
    """

    sql_insert_reservation = "insert into Reservations (StartDate, EndDate, Insurance, CustomerEmail, Vehicle, Canceled, TotalPrice) \
                            values (%s, %s, %s, %s, %s,%s,%s)"
    reservation_values = (start_date, end_date, insurance, customer_email, car_id, canceled, total_price)
    
    mycursor.execute(sql_insert_reservation, reservation_values)
    mydb.commit()
    
    mycursor.execute("select last_insert_id()")
    
    myresult = mycursor.fetchone()
    
    return myresult[0]

def get_reports(car_id):
    """
    Retrieve all reports for a specific vehicle.

    @param car_id: int - ID of the vehicle.
    @return list: A list of reports associated with the vehicle.
    """
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
    """
    Retrieve customer information by their ID.

    @param customer_id: int - ID of the customer.
    @return dict: A dictionary containing the customer's information, or None if not found.
    """
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
    """
    Retrieve all reservations from the database.

    @return list: A list of all reservations.
    """
    reservations = []
    sql_select_reservations = "select * from Reservations"
    mycursor.execute(sql_select_reservations)
    
    myresult = mycursor.fetchall()
    for x in myresult:
        reservations.append(x)
    
    return reservations

def get_hashed_password(login_username: int, person_type: str) -> str:
    """
    Retrieve the hashed password for a user.

    @param login_username: int - The username or ID of the user.
    @param person_type: str - The type of user ('customer' or 'admin').
    @return str: The hashed password of the user.
    """
    if(person_type.lower() == "customer"):
        sql_select_password = "select Password from Customers where Username = %s"
    elif(person_type.lower() == "admin"):
        sql_select_password = "select Password from Administrator where Username = %s"
    
    mycursor.execute(sql_select_password, [login_username])
    result = mycursor.fetchone()
    
    return result[0]

def admin_sign_up(name: str, signup_username: str, email: str, password: str, dob: str) -> None:
    """
    Register a new admin user.

    @param name: str - Name of the admin.
    @param signup_username: str - Username for the admin.
    @param email: str - Email address of the admin.
    @param password: str - Password for the admin account.
    @return None
    """

    sql_insert_admin = "insert into Administrator (User, Email, Password, Username, DOB) values (%s, %s, %s, %s, %s)"
    admin_values = (name, email, password, signup_username, dob)
    
    mycursor.execute(sql_insert_admin, admin_values)
    mydb.commit()

def customer_sign_up(name: str, signup_username: str, email: str, password: str, dob: str) -> None:
    sql_insert_customer = "insert into Customers (FullName, DOB, Email, Username, Password) values (%s, %s, %s, %s, %s)"
    customer_values = (name, dob, email, signup_username, password)
    
    mycursor.execute(sql_insert_customer, customer_values)
    mydb.commit()

def change_password(input_username: str, input_password: str, person_type: str) -> None:
    """
    Change the password for a user.

    @param input_username: str - Username of the user.
    @param input_password: str - New password for the user.
    @param person_type: str - The type of user ('customer' or 'admin').
    @return None
    """
    if(person_type.lower() == "customer"):
        sql_update = "update Customers set Password = %s where Username = %s"
    elif(person_type.lower() == "admin"):
        sql_update = "update Administrator set Password = %s where Username = %s"
    
    values = (input_password, input_username)
    mycursor.execute(sql_update, values)
    mydb.commit()
    
def cancel_reservation(reservation_id: int) -> None:
    """
    Cancel a reservation by updating its status to canceled.

    @param reservation_id: int - The ID of the reservation to be canceled.
    @return None
    """
    # Update the Canceled column in the Reservations table
    set_canceld_to_one = "UPDATE Reservations SET Canceled = 1 WHERE ReservationId = %s"
    mycursor.execute(set_canceld_to_one, (reservation_id,))
    
    # Commit all the changes
    mydb.commit()

    # Print confirmation
    print(f"Reservation {reservation_id} has been canceled.")

def confirm_reservation(reservation_id: int) -> None:
    """
    Confirm a reservation by updating its status to confirmed.
    A reservation cannot be confirmed if it is already marked as canceled.

    @param reservation_id: int - The ID of the reservation to be confirmed.
    @return None
    """

    # Check if the reservation is already canceled
    check_canceled_query = "SELECT Canceled FROM Reservations WHERE ReservationId = %s"
    mycursor.execute(check_canceled_query, (reservation_id,))
    result = mycursor.fetchone()

    if result is None:
        print(f"No reservation found with ID {reservation_id}.")
        return

    if result[0] == 1:
        print(f"Reservation {reservation_id} is canceled and cannot be confirmed.")
        return
    
    
    # Update the Canceled column in the Reservations table
    set_confirmed_to_one = "UPDATE Reservations SET Confirmed = 1 WHERE ReservationId = %s"
    mycursor.execute(set_confirmed_to_one, (reservation_id,))
    
    # Commit all the changes
    mydb.commit()

    # Print confirmation
    print(f"Reservation {reservation_id} has been confirmed.")

def get_admin_info(input_username):
    sql_select = "select * from Administrator where Username = %s"
    mycursor.execute(sql_select, [input_username])
    result = mycursor.fetchone()
    
    return result

def get_customer_info(input_username):
    sql_select = "select * from Customers where Username = %s"
    mycursor.execute(sql_select, [input_username])
    result = mycursor.fetchone()
    
    return result

def get_reservations_history(customer_email: str) -> list[tuple]:
    """
    Retrieves all reservations made by a specific customer.

    Parameters
    ----------
    customer_email: str
        The email of the customer whose reservations are to be retrieved.

    Returns
    -------
    list[tuple]:
        A list of tuples, where each tuple contains information about a reservation.

    Author: Nima Jafari
    Updates:
    """
    reservations = []
    sql_select_reservations = "SELECT * FROM Reservations WHERE CustomerEmail = %s"
    mycursor.execute(sql_select_reservations, (customer_email,))
    
    myresult = mycursor.fetchall()
    for reservation in myresult:
        reservations.append(reservation)
    
    return reservations

def get_admin_usernames():
    """
    Retrieves all admin username
    
    Parameters
    ----------
    None
    
    Returns
    -------
    
    Author: Elijah Sagaran
    Updates
    """
    usernames = []
    sql_select_usernames = "select Username from Administrator"
    mycursor.execute(sql_select_usernames)
    myresult = mycursor.fetchall()
    
    for username in myresult:
        usernames.append(username)
    
    usernames.sort()
    
    return usernames

def get_customer_usernames():
    """
    
    """
    usernames = []
    sql_select_usernames = "select Username from Customers"
    mycursor.execute(sql_select_usernames)
    myresult = mycursor.fetchall()
    
    for username in myresult:
        usernames.append(username)
        
    usernames.sort()
    
    return usernames