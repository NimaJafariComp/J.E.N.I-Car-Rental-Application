"""
Date of Creation: October 9, 2024
Author: Elijah Sagaran
Date of Updates and Updater:
1. Elijah: 10/9


"""
class report:
    """
    Class to store information for a report that is designated to a car_id
    
    Attributes:
    -----------
    damages: str
        description of damages the car has upon customer return
    gas_amount: int
        Current gas amount of vehicle after customer returned it
    car_id: int
        Car ID assigned to the vehicle
    reservation_id: int
        Reservation ID that is associated with the car and return date
    
    """
    def __init__(self, damages, gas_amount, car_id, reservation_id):
        self.report_id = None
        self.damages = damages
        self.gas_amount = gas_amount
        self.car_id = car_id
        self.reservation_id = reservation_id

    def set_report_id(self, report_id):
        self.report_id = report_id

    def __repr__(self):
        return 'Report ID: {}'.format(self.report_id)