from .database_class import database_utility_class as dbu
from .database_class.inventory_class import inventory as inv
from .invoice_class.invoice_class import InvoiceSender
from .revenue_class.revenue import Revenue
from .database_class.admin_class import Administrator as admin
from .database_class.customer_class import Customer as cust
import bcrypt

class CarRentalService:
    """
    Date of Creation: October 22, 2024
    Author: Elijah Sagaran and Nima Jafari
    
    Overarching class for the backend. Contains the API calls that front end needs to call for integration.
    
    Attributes:
    -----------
    my_host: str
        The hosting server for the AWS database
    my_port: int
        Port being used to connect MySQL and AWS
    username: str
        AWS Account username
    password: str
        AWS Account password
    
    """
    def __init__(self, my_host, my_port, username, password):
        """
        Initializes the CarRentalService with host, port, username, and password
        """
        self.username = username
        self.password = password
        self.host = my_host
        self.port = my_port
        self.inv_obj = inv()
    
    def connect_to_mysql(self):
        """
        Initializes the connection to databse for future queries
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        
        Author: Elijah Sagaran, 10/22
        Updates: 
            Elijah, 10/22
            Johnny, 10/24
            Elijah, 10/31
            Elijah, 11/7
        """
        dbu.initialize_connection(self.host, self.port, self.username, self.password)
        self.inv_obj.initialize_inventory()
    
    def add_car(self, vin: str, mileage: int, mpg: int, price: float, license_plate: str, 
                car_year: str, model: str, make: str, color: str , car_type: str) -> None:
        """
        Calls the function of inventory class to add car to current inventory
        
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
        model: str
            The model of the car. i.e. Corolla, Civic, and Prius
        make: str
            The brand of the car. i.e. Toyota and Honda 
        color: str
            The color of the car. i.e. Red, Blue, and Yellow
        car_type: str
            The classification of the car. i.e. Sedan, SUV, and Truck
        
        Returns
        -------
        None
        
        Author: Elijah Sagaran, 10/22
        Updates: 
            Elijah, 10/31
            Elijah, 11/7
        """
        self.inv_obj.add_car(vin, mileage, mpg, price, license_plate, car_year, model, make, color, car_type)
    
    def delete_multiple_cars(self, car_ids: list[int]) -> None:
        """
        A loop function for delete_car to be able to delete multiple cars
        
        Parameters
        ----------
        car_ids: list[int]
            List of the Car IDs that needs to be deleted from inventory
        
        Returns
        -------
        None
        
        Author: Elijah Sagaran, 10/22
        Updates:
            Elijah, 11/7
        """
        for car_id in car_ids:
            self.delete_car(car_id)
    
    def delete_car(self, car_id: int) -> None:
        """
        Calls retire_car from car class to delete the car
        
        Parameters
        ----------
        car_id: int
            Car Id of vehicle to be deleted 
        
        Returns
        -------
        None
        
        Exception
        ---------
        Does nothing if the car_id passed is not valid
        
        Author: Elijah Sagaran, 10/22
        Updates: 
            Elijah, 10/22
            Elijah, 10/31
            Elijah, 11/7
        """
        index = self.inv_obj.search_car(car_id)
        
        # Error Check: Is car_id a valid id
        if index == -1:
            return
            
        # call to car class' retire_car() method
        self.inv_obj.get_car_from_inventory(index).retire_car()
    
    def add_report(self, car_id: int, damages: str, gas_amount: int,
                    reservation_id: int) -> None:
        """
        Calls add_report from car class to assign a report to a car
        
        Parameters
        ----------
        car_id: int
            Car ID assigned to the vehicle
        damages: str
            Description of damages that the vehicle has
        gas_amount: int
            Current gas amount of vehicle after customer returned it
        reservation_id: int
            Reservation ID that is associated with the car and return date
        
        Returns
        -------
        None
        
        Exception
        ---------
        Does nothing if the car_id passed is not valid
        
        Author: Elijah Sagaran, 10/22
        Updates:
            Elijah, 10/31
            Elijah, 11/7
        """
        index = self.inv_obj.search_car(car_id)
        
        # Error Check: Is car_id a valid id 
        if index == -1:
            return
        
        # call to car class add_report() method
        self.inv_obj.get_inventory()[index].add_report(damages, gas_amount, car_id, reservation_id)
        
        # need to call the update_mileage in this function? could be called in the add_report function in car class too
    
    def customer_search(self, start_date: str, end_date: str, car_type: str) -> list[tuple]:
        """
        Calls the search_database() method from database utility class
        
        Parameters
        ----------
        start_date: str
            The start date of the desired reservation
        end_date: str
            The end date of the desired reservation
        car_type: str
            The type of car that customer wants to see. i.e. SUV and Sedan
        
        Returns
        -------
        list[tuple]
            Each tuple in the list has all the information about the car
        
        Author: Elijah Sagaran, 10/22
        Updates: 
            Elijah, 10/22
            Elijah, 10/31
            Elijah, 11/7
        """
        return dbu.search_database(start_date, end_date, car_type)
    
    def make_reservation(self, start_date: str, end_date: str, insurance: int, customer_email: str, car_id: int) -> None:
        """
        Calls add_reservation from car class to assign a reservation to a car
        
        Parameters
        ----------
        start_date: str
            The start date of the reservation
        end_date: str
            The end date of the reservation
        insurance: int
            Values 0 or 1, boolean value. Indicates if customer wants to include insurance
        customer_email: str
            Email of the customer for the invoice/confirmation email
        car_id: int
            The car ID of the desired car
        total_price: float
            The total reservation price, initially 0 calculated for invoice
        
        Returns
        -------
        None
        
        Exception
        ---------
        Does nothing if the car_id passed is not valid
        
        Author: Elijah Sagaran, 10/22
        Updates:
            Elijah, 10/29
            Elijah, 11/7
            ELijah, 11/10
            Nima jafari, 11/26
            Nima jafari, 11/27
        """
        index = self.inv_obj.search_car(car_id)
        if index == -1:
            print("index -1")
            return
        
        car = dbu.get_car_info(car_id)
        
        if not car: #not customer or not car:
            print("Error: Unable to fetch customer or vehicle information.")
            return
            
        daily_price = car[4]
        
        total_days = dbu.calculate_days(start_date, end_date)
        
        total_price = daily_price * total_days
        
        #print(total_price)
            
        self.inv_obj.get_inventory()[index].add_reservation(start_date, end_date, insurance, customer_email, car_id, total_price)
        
        self.send_invoice(customer_email, car_id, start_date, insurance, end_date, total_price, total_days, daily_price) #send invoice after reservation is done, so we dont have to search database for reservations and then send em
    
    def send_invoice(self, customer_email: str, car_id: int, start_date: str, insurance: bool, end_date: str, total_price:float, total_days:float, daily_price:float) -> None:
        """
        Sends the invoice to customer's email after they reserve a car
        
        Parameters
        ----------
        customer_email: str
            Email of the customer that will receive the invoice/confirmation
        car_id: int
            Car ID of the vehicle that is being reserved
        start_date: str
            The start date of the reservation
        insurance: bool
            Indicates if customer wants to include insurance for the reservation
        end_date: str
            The end date of the reservation
        total_price: float
            The total price of the reservation.
        total_days: float
            The total number of rental days.
        daily_price: float
            The price per day for the car rental.
        
        Returns
        -------
        None
        
        Exception
        ---------
        Invoice cannot be sent to the customer
        
        Author: Nima Jafari, 10/28
        Updates:
            Nima, 10/28
            Elijah, 10/29
            Elijah, 11/10
            Nima, 11/26
            Nima, 11/27
        """
        
        # customer = dbu.get_customer_info(customer_id)
        car = dbu.get_car_info(car_id)
        
        if not car: #not customer or not car:
            print("Error: Unable to fetch customer or vehicle information.")
            return
        
        print(daily_price)
        print(total_days)
        print(total_price)
        
        # Prepare dynamic data for the template
        dynamic_data = {
            # "customer_name": customer['FullName'],
            "customer_email": customer_email,
            "car_model": car[9],
            "car_brand": car[8],
            "car_year": car[7],
            "daily_price": f"{(daily_price):.2f}",
            "start_date": start_date,
            "end_date": end_date,
            "total_days": (total_days),
            "total_price": f"{(total_price):.2f}",
            "insurance_status": "Yes" if insurance else "No"
        }
        
        invoice_sender = InvoiceSender()
        
        try:
            invoice_sender.send_email(customer_email, "Your Car Rental Invoice", dynamic_data)
            print("Invoice sent successfully.")
        except Exception as e:
            print(f"Error sending invoice: {e}")
    
    def get_reservations(self) -> list[tuple]:
        """
        Gets all the reservation that is in the database
        
        Parameters
        ----------
        None
        
        Returns
        -------
        list[tuple]
            Each tuple in the list contains all the information about the reservation
        
        Author: Elijah Sagaran, 10/29
        Updates:
            Elijah, 11/10
        """
        return dbu.get_reservations()
        
    
    def get_inventory_admin(self) -> list[tuple]:
        """
        Gets all the active vehicle in the database 
        
        Parameters
        ----------
        None
        
        Returns
        -------
        list[tuple]
            Each tuple in the list contains all the information about the car
        
        Author: Elijah Sagaran, 10/30
        Updates:
            Elijah, 11/10
        """
        return dbu.get_active_inventory()
    
    def check_password(self, input_username: str, input_password: str, person_type: str) -> bool:
        """
        Checks if the input password matches with the password stored in the database for the input username
        
        Parameters
        ----------
        input_username: str
            The username of the person
        input_password: str
            The password of the person
        person_type: str
            admin or customer, indicates which table we need to query the password from
        
        Return
        ------
        bool
            Retuns true, if input password matches with stored password
            Returns false, if input password does not match with stored password
        
        Author: Elijah Sagaran, 11/14
        Updates:
            Elijah, 11/16
        """
        
        hashed_password = dbu.get_hashed_password(input_username, person_type).encode('utf-8')
        return bcrypt.checkpw(input_password.encode(), hashed_password)
    
    def hash_password(self, input_password: str) -> str:
        """
        Hashes the input password from siging up
        
        Parameters
        ----------
        input_password: str
            The password that needs to be hashed
        
        Return
        ------
        str
            Hashed password
        
        Author: Elijah Sagaran, 11/16
        Updates:
        """
        return bcrypt.hashpw(input_password.encode(), bcrypt.gensalt())
    
    def create_admin(self, name: str, input_username: str, email: str, input_password: str, dob: str) -> None:
        """
        Takes in input from user and stores values in database by calling admin_sign_up function
        
        Parameters
        ----------
        name: str
            Name of the user
        input_username: str
            Chosen username of the user
        email: str
            email of the user
        input_password: str
        
        Return
        ------
        None
        
        Author: Elijah Sagaran, 11/16
        Updates:
        """
        hashed_password = self.hash_password(input_password)
        dbu.admin_sign_up(name, input_username, email, hashed_password, dob)
    
    def create_customer(self, name: str, input_username: str, email: str, input_password: str, dob: str) -> None:
        hashed_password = self.hash_password(input_password)
        dbu.customer_sign_up(name, input_username, email, hashed_password, dob)
    
    def revenue(self) -> dict:
        """
        Calculate weekly, monthly, and yearly revenue from reservations.

        Returns
        -------
        dict
            A dictionary containing weekly, monthly, and yearly revenue.
        
        Author: [Nima jafari], [11/27]
        """
        reservations = self.get_reservations()
        revenue_instance = Revenue()
        calculated_revenue = revenue_instance.revenue(reservations=reservations)
        print(calculated_revenue)
        
    def reservation_cancel_setter(self, reservation_id: int) -> None:
        """
        Function to mark a reservation as canceled in the database.

        Parameters
        ----------
        reservation_id: int
            The ID of the reservation to be canceled.

        Return
        ------
        None
        
        Author: [Nima jafari], [11/27]
        Updates:
        """
        dbu.cancel_reservation(reservation_id)
    
    def reservation_confirm_setter(self, reservation_id: int) -> None:
        """
        Function to mark a reservation as confirmed in the database.
        
        Parameters
        ----------
        reservation_id: int
            The ID of the reservation to be confirmed.
            
        Return
        ------
        None
        
        Author: [Nima jafari], [11/27]
        Updates:
        """
        dbu.confirm_reservation(reservation_id)
    
    def user_login(self, input_username, input_password, person_type):
        """
        Function to handle user login based on their role (customer or admin).
        
        Parameters
        ----------
        input_username: str
            The username of the user attempting to log in.
        input_password: str
            The password of the user attempting to log in.
        person_type: str
            The role of the user, either 'customer' or 'admin'.
        
        Returns
        -------
        admin or cust or bool
            If successful, returns the corresponding user object (admin or customer).
            If unsuccessful, returns False.
        
        Author: Elijah
        Updates:
        """
        if person_type.lower() == "customer":
            return self.customer_login(input_username, input_password)
        elif person_type.lower() == "admin":
            return self.admin_login(input_username, input_password)
    
    def user_signup(self, name: str, input_username: str, email: str, input_password: str, dob: str, person_type: str) -> None:
        """
        Function to handle user registration based on their role (customer or admin).
        
        Parameters
        ----------
        name: str
            The full name of the user.
        input_username: str
            The username chosen by the user.
        email: str
            The email address of the user.
        input_password: str
            The password chosen by the user.
        dob: str
            The date of birth of the user.
        person_type: str
            The role of the user, either 'customer' or 'admin'.
        
        Returns
        -------
        None
        
        Author: Elijah 
        Updates:
        """
        if person_type.lower() == "customer":
            self.create_customer(name, input_username, email, input_password, dob)
        elif person_type.lower() == "admin":
            self.create_admin(name, input_username, email, input_password, dob)
    
    def user_update_password(self, input_username: str, input_password: str, person_type: str) -> None:
        """
        Function to update the password of a user (customer or admin).
        
        Parameters
        ----------
        input_username: str
            The username of the user whose password needs to be updated.
        input_password: str
            The new password for the user.
        person_type: str
            The role of the user, either 'customer' or 'admin'.
        
        Returns
        -------
        None
        
        Author: Elijah
        Updates:
        """
        hashed_password = self.hash_password(input_password)
        if person_type.lower() == "customer":
            dbu.change_password(input_username, hashed_password, person_type)
        elif person_type.lower() == "admin":
            dbu.change_password(input_username, hashed_password, person_type)
    
    def admin_login(self, input_username: str, input_password: str) -> admin:
        """
        Function to authenticate an admin and retrieve their details.
        
        Parameters
        ----------
        input_username: str
            The username of the admin attempting to log in.
        input_password: str
            The password of the admin attempting to log in.
        
        Returns
        -------
        admin
            The admin object containing the admin's information if authentication is successful.
            Returns False if authentication fails.
        
        Author: Elijah
        Updates:
        """
        is_valid_login = True
        usernames = dbu.get_admin_usernames()
        
        if self.search(input_username, usernames) == -1:
            is_valid_login = False
        else:
            if not self.check_password(input_username, input_password, "admin"):
                is_valid_login = False
        
        
        if is_valid_login == True:
            info = dbu.get_admin_info(input_username)
            admin_obj = admin(info[0], info[1], info[2], info[4], info[3], info[5])
            print(admin_obj)
            return admin_obj
        else:
            return None
    
    def customer_login(self, input_username: str, input_password: str) -> cust:
        """
        Function to authenticate a customer and retrieve their details.
        
        Parameters
        ----------
        input_username: str
            The username of the customer attempting to log in.
        input_password: str
            The password of the customer attempting to log in.
        
        Returns
        -------
        cust
            The customer object containing the customer's information if authentication is successful.
            Returns False if authentication fails.
        
        Author: Elijah
        Updates:
        """
        is_valid_login = True
        usernames = dbu.get_customer_usernames()
        
        if self.search(input_username, usernames) == -1:
            is_valid_login = False
        else:
            if not self.check_password(input_username, input_password, "customer"):
                is_valid_login = False
        
        
        if is_valid_login == True:
            info = dbu.get_customer_info(input_username)
            customer_obj = cust(info[0], info[1], info[3], info[4], info[5], info[2])
            print(customer_obj)
            return customer_obj
        else:
            return None
    
    def resevation_history(self, customer_email: str) -> list[tuple]:
        """
        Function to retrieve the reservation history of a customer based on their email.
        
        Parameters
        ----------
        customer_email: str
            The email of the customer whose reservation history is to be retrieved.
        
        Returns
        -------
        list[tuple]
            A list of tuples, where each tuple contains details of a reservation made by the customer.
        
        Author: [Nima jafari], [12/01]
        Updates:
        """
        customer_history = dbu.get_reservations_history(customer_email=customer_email)
        print(customer_history)
    
    def search(self, username: str, username_list: list) -> int:
        low, high, mid = 0, len(username_list) - 1, 0
        
        while low <= high:
            mid = (high + low) // 2
            
            if username_list[mid][0] < username:
                low = mid + 1
            elif username_list[mid][0] > username:
                high = mid - 1
            else:
                return mid
        
        return -1

