from .database_class import database_utility_class as dbu
from .database_class.inventory_class import inventory as inv
from .invoice_class.invoice_class import InvoiceSender

class CarRentalService:
    
    """
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
        """
        dbu.initialize_connection(self.host, self.port, self.username, self.password)
        self.inv_obj.initialize_inventory()

    """
    Function: add_car(vin, mileage, mpg, price, license_plate, car_year, model, make, color, car_type)
    Description: calls the function of inventory class to add car to current inventory
    """
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
        
        """
        # self.inv_obj.initialize_search_inventory(start_date, end_date, car_type)
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
        
        Returns
        -------
        None
        
        Exception
        ---------
        Does nothing if the car_id passed is not valid
        
        """
        index = self.inv_obj.search_car(car_id)
        if index == -1:
            return
            
        self.inv_obj.get_inventory()[index].add_reservation(start_date, end_date, insurance, customer_email, car_id)
        
        self.send_invoice(customer_email, car_id, start_date, insurance, end_date) #send invoice after reservation is done, so we dont have to search database for reservations and then send em

    def send_invoice(self, customer_email: str, car_id: int, start_date: str, insurance: bool, end_date: str) -> None:
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
        
        Returns
        -------
        None

        Exception
        ---------
        Invoice cannot be sent to the customer
        """
        
        # customer = dbu.get_customer_info(customer_id)
        car = dbu.get_car_info(car_id)

        if not car: #not customer or not car:
            print("Error: Unable to fetch customer or vehicle information.")
            return

        daily_price = car[4]
        total_days = dbu.calculate_days(start_date, end_date)
        total_price = daily_price * total_days

        # Prepare dynamic data for the template
        dynamic_data = {
            # "customer_name": customer['FullName'],
            "customer_email": customer_email,
            "car_model": car[9],
            "car_brand": car[8],
            "car_year": car[7],
            "daily_price": f"{daily_price:.2f}",
            "start_date": start_date,
            "end_date": end_date,
            "total_days": total_days,
            "total_price": f"{total_price:.2f}",
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

        """
        return dbu.get_active_inventory()