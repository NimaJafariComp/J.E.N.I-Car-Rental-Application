from .database_class import database_utility_class as dbu
from .database_class.inventory_class import inventory as inv
from .invoice_class.invoice_class import InvoiceSender

class CarRentalService:
    def __init__(self, my_host, my_port, username, password):
        self.username = username
        self.password = password
        self.host = my_host
        self.port = my_port
        self.inv_obj = inv()
    
    def connect_to_mysql(self):
        dbu.initialize_connection(self.host, self.port, self.username, self.password)
        self.inv_obj.initialize_inventory()

    def add_car(self, uVin: str, uMileage: int, uMPG: int, uPrice: float, uLicensePlate: str, 
                uCarYear: str, uModel: str, uMake: str, uColor: str , uCarType: str) -> None:
        self.inv_obj.add_car(uVin, uMileage, uMPG, uPrice, uLicensePlate, uCarYear, uModel, uMake, uColor, uCarType)

    def delete_multiple_cars(self, car_ids: list[int]) -> None:
        for car_id in car_ids:
            self.delete_car(car_id)

    def delete_car(self, uCarID: int) -> None:
        index = self.inv_obj.search_car(uCarID)
        if index == -1:
            return
        self.inv_obj.get_car_from_inventory(index).retire_car()

    def add_report(self, uCarID: int, uDamages: str, uGasAmount: int,
                    uReservationID: int):
        index = self.inv_obj.search_car(uCarID)
        if index == -1:
            return
        
        self.inv_obj.get_inventory()[index].add_report(uDamages, uGasAmount, uCarID, uReservationID)

    def customer_search(self, uStartDate: str, uEndDate: str, uCarType: str) -> list[tuple]:
        # self.inv_obj.initialize_search_inventory(uStartDate, uEndDate, uCarType)
        return dbu.search_database(uStartDate, uEndDate, uCarType)
        
        
    def make_reservation(self, start_date, end_date, insurance, customer_email, car_id):
        index = self.inv_obj.search_car(car_id)
        if index == -1:
            return
            
        self.inv_obj.get_inventory()[index].add_reservation(start_date, end_date, insurance, customer_email, car_id)
        
        self.send_invoice(customer_email, car_id, start_date, insurance, end_date) #send invoice after reservation is done, so we dont have to search database for reservations and then send em

    def send_invoice(self, customer_email: str, car_id: int, start_date: str, insurance: bool, end_date: str) -> None:
        # customer = dbu.get_customer_info(customer_id)
        car = dbu.get_car_info(car_id)

        if not car: #not customer or not car:
            print("Error: Unable to fetch customer or vehicle information.")
            return

        daily_price = car[4]
        total_days = dbu.calculate_days(start_date, end_date)
        total_price = daily_price * total_days

        # Prepare dynamic data for the template
        dynamic_data = {
            # "customer_name": customer['FullName'],
            "customer_email": customer_email,
            "car_model": car[9],
            "car_brand": car[8],
            "car_year": car[7],
            "daily_price": f"{daily_price:.2f}",
            "start_date": start_date,
            "end_date": end_date,
            "total_days": total_days,
            "total_price": f"{total_price:.2f}",
            "insurance_status": "Yes" if insurance else "No"
        }

        invoice_sender = InvoiceSender()

        try:
            invoice_sender.send_email(customer_email, "Your Car Rental Invoice", dynamic_data)
            print("Invoice sent successfully.")
        except Exception as e:
            print(f"Error sending invoice: {e}")

    def get_reservations(self):
        return dbu.get_reservations()