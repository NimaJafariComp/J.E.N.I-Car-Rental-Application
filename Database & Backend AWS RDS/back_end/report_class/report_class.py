class report:
    def __init__(self, damages, gas_amount, car_id, reservation_id):
        self.report_id = None
        self.damages = damage
        self.gas_amount = gas_amount
        self.car_id = car_id
        self.reservation_id = reservation_id 
        
    def get_car_id(self):
       return self.car_id
        
    def get_damage(self):
       return self.damage
            
    def get_gas_amount(self):
       return self.gas_amount
    
    def get_reservation_id(self):
        return self.reservation_id
    
    def get_report_id(self):
       return self.report_id
        
    def set_report_id(self, report_id):
       self.report_id = report_id