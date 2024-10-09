class report:
    def __init__(self, customer_id, car_id, damage, mileage, gas_amount):
       self.customer_id = customer_id
       self.car_id = car_id
       self.damage = damage
       self.mileage = mileage
       self.gas_amount = gas_amount
       self.report_id = None
        
    def get_customer_id(self):
       return self.customer_id
        
    def set_customer_id(self, customer_id):
       self.customer_id = customer_id
        
    def get_car_id(self):
       return self.car_id
        
    def get_damage(self):
       return self.damage
        
    def get_mileage(self):
       return self.mileage
        
    def get_gas_amount(self):
       return self.gas_amount
        
    def get_report_id(self):
       return self.report_id
        
    def set_report_id(self, report_id):
       self.report_id = report_id