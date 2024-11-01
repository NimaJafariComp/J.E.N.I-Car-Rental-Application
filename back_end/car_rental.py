from .database_class import database_utility_class as dbu
from .database_class.inventory_class import inventory as inv
from .invoice_class.invoice_class import InvoiceSender

class CarRentalService:
    
    """
    Function: Class Object Initialization
    Input: 
        my_host, string
        my_port, string
        username, string
        password, string
    """
    def __init__(self, my_host, my_port, username, password):
        self.username = username
        self.password = password
        self.host = my_host
        self.port = my_port
        self.inv_obj = inv()

    """
    Function: connect_to_mysql()
    Input: None
    Output: None
    Description: initializes the connection to database for 
                future queries
    """
    def connect_to_mysql(self):
        dbu.initialize_connection(self.host, self.port, self.username, self.password)
        self.inv_obj.initialize_inventory()

    """
    Function: add_car(vin, mileage, mpg, price, license_plate, car_year, model, make, color, car_type)
    Description: calls the function of inventory class to add car to current inventory
    """
    def add_car(self, vin: str, mileage: int, mpg: int, price: float, license_plate: str, 
                car_year: str, model: str, make: str, color: str , car_type: str) -> None:
        self.inv_obj.add_car(vin, mileage, mpg, price, license_plate, car_year, model, make, color, car_type)

    """
    Function: delete_multiple_cars(car_ids)
    Description: basically a loop function for delete_car function 
    to be able to delete multiple cars
    """
    def delete_multiple_cars(self, car_ids: list[int]) -> None:
        for car_id in car_ids:
            self.delete_car(car_id)

    """
    Function: delete_car(car_id)
    Description: calls retire_car from car class to deactive the car
    """
    def delete_car(self, car_id: int) -> None:
        index = self.inv_obj.search_car(car_id)
        
        # Error Check: Is car_id a valid id
        if index == -1:
            return
            
        # call to car class' retire_car() method
        self.inv_obj.get_car_from_inventory(index).retire_car()

    """
    Function: add_report(car_id, damages, gas_amount, reservation_id)
    Description: calls add_report from car class to assign a report to a car
    """
    def add_report(self, car_id: int, damages: str, gas_amount: int,
                    reservation_id: int):
        index = self.inv_obj.search_car(car_id)
        
        # Error Check: Is car_id a valid id 
        if index == -1:
            return
        
        # call to car class add_report() method
        self.inv_obj.get_inventory()[index].add_report(damages, gas_amount, car_id, reservation_id)

    """
    Function: customer_search(start_date, end_date, car_type)
    Description: calls the search_database() method from database utility class
    """
    def customer_search(self, start_date: str, end_date: str, car_type: str) -> list[tuple]:
        # self.inv_obj.initialize_search_inventory(start_date, end_date, car_type)
        return dbu.search_database(start_date, end_date, car_type)

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

    def get_inventory_admin(self):
        return dbu.get_active_inventory()