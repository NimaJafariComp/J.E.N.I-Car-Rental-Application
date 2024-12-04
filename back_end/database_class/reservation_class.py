class reservation:
    """
    Class to hold data for each reservation for a car
    
    Attributes
    ----------
    start_date: str
        The start date of the reservation
    end_date: str
        The end date of the reservation
    insurance: int
        Values 0 or 1, boolean value. Indicates if customer wants to include insurance
    customer_email: str
        Email of the customer for the invoice/confirmation email
    customer_id: int
        id of the customer
    car_id: int
        The car ID of the desired car
    cancelled: int
        0, if not cancelled. 1, if it is 
        
    Date of Creation: 10/22
    Author: Elijah Sagaran and Nima Jafari
    Updates:
        Elijah, 10/29
        Nima, 11/18
    """
    def __init__(self, start_date, end_date, insurance, customer_email, customer_id, vehicle, canceled):
        self.start_date = start_date
        self.end_date = end_date
        self.insurance = insurance
        self.customer_email = customer_email
        self.customer_id = customer_id
        self.vehicle = vehicle
        self.reservation_id = None
        self.canceled = canceled

    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id
        
        
    def __repr__(self):
        return 'Reservation ID: {}'.format(self.reservation_id)