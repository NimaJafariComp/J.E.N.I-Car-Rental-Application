from .database_class import database_utility_class as dbu
from .database_class.inventory_class import inventory as inv

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
        
        
    def make_reservation(self, start_date, end_date, insurance, customer_id, car_id):
        index = self.inv_obj.search_car(car_id)
        if index == -1:
            return
            
        self.inv_obj.get_inventory()[index].add_reservation(start_date, end_date, insurance, customer_id, car_id)
