class reservation:
    def __init__(self, start_date, end_date, insurance, customer_id, vehicle):
        self.start_date = start_date
        self.end_date = end_date
        self.insurance = insurance
        self.customer_id = customer_id
        self.vehicle = vehicle
        self.reservation_id = None

    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id
        
    def __repr__(self):
        return 'Reservation ID: {}'.format(self.reservation_id)