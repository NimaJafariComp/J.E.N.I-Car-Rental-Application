class reservation:
    def __init__(self, start_date, end_date, insurance, customer_email, vehicle):
        self.start_date = start_date
        self.end_date = end_date
        self.insurance = insurance
        self.customer_email = customer_email
        self.vehicle = vehicle
        self.reservation_id = None

    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id
        
    def __repr__(self):
        return 'Reservation ID: {}'.format(self.reservation_id)