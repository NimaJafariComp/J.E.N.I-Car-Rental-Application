from .report_class import report as rc
from .database_utility_class import get_reports, change_mileage, deactivate_car, insert_report, insert_reservation, get_reports
from .reservation_class import reservation as rsvp
"""
Date of Creation: 10/12
Author: Elijah Sagaran
Updates: 
    Elijah, 10/12
    Elijah, 10/13
    Elijah, 10/13
    Elijah, 10/22
    Elijah, 10/22
    Elijah, 10/29
    Elijah, 11/10
    
"""
class car:
    """
    Class that lets users control car information. This includes adding, deleting, and modifying attributes that the car has.
    
    Attributes:
    -----------
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
    """

    def __init__(self, vin: str, mileage: int, mpg: int, price: float, license_plate: str, car_year: str, model: str, make: str, color: str, car_type: str):
        """
        Initializes car object wit the passed parameters
        """
        self.vin = vin
        self.mileage = mileage
        self.mpg = mpg
        self.price = price
        self.license_plate = license_plate
        self.car_year = car_year
        self.model = model
        self.make = make
        self.color = color
        self.car_type = car_type
        self.reports = []
        self.reservations = []
        self.car_id = None


    def __repr__(self) -> str:
        """
        repr Dunder method for Car object 
        
        Parameters
        ----------
        None
        
        Returns
        -------
        str
            Formatted string for printing attributes of car object
        
        """
        return 'Car Info:\n \
                Car ID: {} \n \
                VIN: {} \n \
                Mileage: {} \n \
                MPG: {} \n \
                Price: {} \n \
                License Plate: {} \n \
                Car Year: {} \n \
                Make: {} \n \
                Model: {} \n \
                Color: {} \n \
                Car Type: {} \n \
                Reports: {}'.format(self.car_id, self.vin, self.mileage, self.mpg, self.price,
                self.license_plate, self.car_year, self.make, self.model, self.color, 
                self.car_type, self.reports)

    def set_car_id(self, car_id: int) -> None:
        """
        Setter function for the car_id attribute
        
        Parameters
        ----------
        car_id: int
            The car ID value that the databse assigns to newly added cars
        
        Returns
        -------
        None
        
        """
        self.car_id = car_id

    def get_car_id(self) -> int:
        """
        Getter function for the car_id attribute
        
        Parameters
        ----------
        None
        
        Returns
        -------
        int
            The car_id of the car object
        
        """
        return self.car_id

    def initialize_reports(self) -> None:
        """
        Assigns all the reports that is associated with the car, from the database
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        
        """
        for report in get_reports(self.car_id):
            report_object = rc(report[1], report[2], report[3], report[4])
            report_object.set_report_id(report[0])
            self.reports.append(report_object)

    def add_report(self, damages: str, gas_amount: int, car_id: int, reservation_id: int) -> None:
        """
        Creates an object of type report with the passed parameters, and then adds it to the current list of reports for the car
        
        Parameters
        ----------
        damages: str
            The description for all the damages the car has when returned by the customer
        gas_amount: int
            The gas amount of the vehicle when returned by the customer 
        car_id: int
            The car ID of which the report needs to be associated with
        reservation_id: int
            The reservation ID of which the report needs to be associated with
        Returns
        -------
        None 
        """
        report_object = rc(damages, gas_amount, car_id, reservation_id)
        report_object.set_report_id(insert_report(damages, gas_amount, car_id, reservation_id))
        
        self.reports.append(repr(report_object))

    def add_reservation(self, start_date: str, end_date: str, insurance: int, customer_email: str, car_id: int) -> None:
        """
        Creates an object of the reservation type, and then adds it to the current list of reservations for the car
        
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
        
        """
        rsvp_obj = rsvp(start_date, end_date, insurance, customer_email, car_id)
        rsvp_obj.set_reservation_id(insert_reservation(start_date, end_date, insurance, customer_email, car_id))
        
        self.reservations.append(repr(rsvp_obj))

    def update_mileage(self, new_mileage: int) -> None:
        """
        Calls the change_mileage function of the database_utility_class
        
        Parameters
        ----------
        new_mileage: int
            The current mileage of the vehicle
        
        Returns
        -------
        None
        
        """
        # Error check
        
        if(new_mileage < self.mileage):
            print("Invalid Mileage Update")
            return
        
        self.mileage = new_mileage
        change_mileage(self.car_id, new_mileage)

    def retire_car(self) -> None:
        """
        Calls the deactive_car function of the database_utility_class
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        
        """
        deactivate_car(self.car_id)