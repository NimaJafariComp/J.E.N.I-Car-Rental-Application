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
        
        
    # Function: set_car_id(car_id)
    # Input: car_id, an integer
    # Output: None
    # Desription: Sets the car_id for the car object
    def set_car_id(self, car_id):
        self.car_id = car_id
        

    # Function: get_car_id()
    # Input: None
    # Output: car_id, an integer
    # Description: Returns the car_id of the car object
    def get_car_id(self):
        return self.car_id
        
    # Function: get_vin()
    # Input: None
    # Output: vin, an integer
    # Description: Returns the vin of the car object
    def get_vin(self):
        return self.vin
        
    # Function: get_mileage()
    # Input: None
    # Output: mileage, an integer
    # Description: Returns the mileage of the car object
    def get_mileage(self):
        return self.mileage
        
    # Function: get_mpg()
    # Input: None
    # Output: mpg, an integer
    # Description: Returns the mpg of the car object
    def get_mpg(self):
        return self.mpg
   
    # Function: get_price()
    # Input: None
    # Output: price, a float
    # Description: Returns the price of the car object 
    def get_price(self):
        return self.price
        
    # Function: get_license_plate()
    # Input: None
    # Output: license_plate, a string
    # Description: Returns the license plate of the car object
    def get_license_plate(self):
        return self.license_plate
        
    # Function: get_type()
    # Input: None
    # Output: type, an object from car_type class
    # Description: Returns the car_type object that is associated
    #               to the car. This object will contain the car's 
    #               year, make, model, color, and type
    def get_type(self):
        return self.type

    # Function: get_reports()
    # Input: None
    # Output: reports, a list of objects from the reports class
    # Description: Return a list of reports associated to the car.
    #               The report object will contain its report id, 
    #               car damages, gas amount, customer, and vehicle
    def get_reports(self):
        return reports
        
    # Function: get_reservations()
    # Input: None
    # Output: reservations, a list of objects from the reservation class
    # Description: Return a list of reservations associated to the car
    #               The reservation object will contain the start date,
    #               end date, insurance (boolean), and reservation id.
    def get_reservations(self):
        return self.reservations

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
        dbu.DBUtils.change_mileage(self.car_id, new_mileage)