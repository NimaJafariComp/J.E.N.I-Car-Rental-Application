class report:
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