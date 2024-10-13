import database_utility_class as dbu

class car:
    
    def __init__(self, uVin, uMileage, uMPG, uPrice, uLicensePlate):
        self.vin = uVin
        self.mileage = uMileage
        self.mpg = uMPG
        self.price = uPrice
        self.license_plate = uLicensePlate
        self.type = None
        self.reports = []
        self.reservations = []
        self.car_id = None
        

    def add_report(self, report_id):
        self.reports.append(report_id)
        
    def add_reservation(self, reservation_id):
        self.reservation.append(reservation_id)
        
    def update_mileage(self, new_mileage):   
        # Error check
        
        if(new_mileage < self.mileage):
            print("Invalid Mileage Update")
            return
        
        self.mileage = new_mileage
        dbu.change_mileage(self.car_id, new_mileage)