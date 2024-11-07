class report:
    """
    A class to represent a report for a car rental, detailing damages, gas amount, 
    and associated car and reservation IDs.

    Attributes
    ----------
    report_id : int or None
        The unique identifier for the report (assigned later).
    damages : str
        Description of any damages to the car.
    gas_amount : float
        The amount of gas remaining in the car.
    car_id : int
        The ID of the car associated with this report.
    reservation_id : int
        The ID of the reservation associated with this report.

    Methods
    -------

    """

    def __init__(self, damages, gas_amount, car_id, reservation_id):
        """
        Initializes a report instance with details of damages, gas amount, car ID, and reservation ID.

        Parameters
        ----------
        damages : str
            Description of any damages to the car.
        gas_amount : float
            The amount of gas remaining in the car.
        car_id : int
            The ID of the car associated with this report.
        reservation_id : int
            The ID of the reservation associated with this report.
        """
        self.report_id = None
        self.damages = damages
        self.gas_amount = gas_amount
        self.car_id = car_id
        self.reservation_id = reservation_id 
        
    def get_car_id(self) -> int:
        """Returns the ID of the car associated with this report."""
        return self.car_id
        
    def get_damage(self) -> str:
        """Returns a description of the damages to the car."""
        return self.damages
            
    def get_gas_amount(self) -> float:
        """Returns the amount of gas remaining in the car."""
        return self.gas_amount
    
    def get_reservation_id(self) -> int:
        """Returns the ID of the reservation associated with this report."""
        return self.reservation_id
    
    def get_report_id(self):
        """Returns the unique identifier for the report, if set."""
        return self.report_id
        
    def set_report_id(self, report_id: int) -> None:
        """
        Sets the unique identifier for the report.

        Parameters
        ----------
        report_id : int
            The unique identifier to assign to this report.
        """
        self.report_id = report_id
