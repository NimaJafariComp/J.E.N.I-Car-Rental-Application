import database_utility_class as dbu
import report_class as rc

class car:
    
    def __init__(self, uVin, uMileage, uMPG, uPrice, uLicensePlate, uCarYear, uModel, uMake, uColor, uCarType):
        self.vin = uVin
        self.mileage = uMileage
        self.mpg = uMPG
        self.price = uPrice
        self.license_plate = uLicensePlate
        self.car_year = uCarYear
        self.model = uModel
        self.make = uMake
        self.color = uColor
        self.car_type = uCarType
        self.reports = []
        self.reservations = []
        self.car_id = None
        

    def __repr__(self):
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
    
    def set_car_id(self, car_id):
        self.car_id = car_id
    
    def get_car_id(self):
        return self.car_id
    
    def initialize_reports(self):
        for report in dbu.get_reports(self.car_id):
            report_object = rc.report(report[1], report[2], report[3], report[4])
            report_object.set_report_id(report[0])
            self.reports.append(report_object)
    
    def add_report(self, damages, gas_amount, car_id, reservation_id):
        report_object = rc.report(damages, gas_amount, car_id, reservation_id)
        report_object.set_report_id(dbu.insert_report(damages, gas_amount, car_id, reservation_id))
        
        self.reports.append(repr(report_object))
        
        
    def add_reservation(self, reservation_id):
        self.reservation.append(reservation_id)
        
    def update_mileage(self, new_mileage):   
        # Error check
        
        if(new_mileage < self.mileage):
            print("Invalid Mileage Update")
            return
        
        self.mileage = new_mileage
        dbu.change_mileage(self.car_id, new_mileage)

    def retire_car(self):
        dbu.deactivate_car(self.car_id)