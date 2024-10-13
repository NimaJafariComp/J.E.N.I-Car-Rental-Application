import database_utility_class as dbu
import car_class

class inventory:
    """
    # initializes the inventory object
    # Input: username, a string
    #        password, a string
    # self.whole_inventory an array of car objects 
    # self.available_inventory an array of car objects where IsActive = 1
    # self.database_object is the database class object needed to access
    # the database
    """
    def __init__(self):
        self.inventory = []
        self.search_inventory = []

    def get_inventory(self):
        return self.inventory
    
    """
    # Function: add_car(uVin, uMileage, uMPG, uPrice, uLicensePlate)
    # Input: uVin, a string
    #        uMileage, an integer
    #        uMPG, an integer
    #        uPrice, a float
    #        uLicensePlate, a string
    # Output: None
    # For testing purposes, it prints out the self.whole_inventory
    # Description: adds a car to the inventory
    """
    def add_car(self, uVin: str, uMileage: int, uMPG: int, uPrice: float, uLicensePlate: str, 
                uCarYear: str, uModel: str, uMake: str, uColor: str , uCarType: str) -> None:
        current_vins = dbu.get_vins()
        
        if uVin in current_vins:
            print("VIN is a duplicate")
            return
        
        # use database module to insert car in database 
        dbu.add_car(uVin, uMileage, uMPG, uPrice, uLicensePlate, uCarYear, uModel, uMake, uColor, uCarType)
        
        # initializes a car object for the new car with the provided information
        car_object = car_class.car(uVin, uMileage, uMPG, uPrice, uLicensePlate,
                                    uCarYear, uModel, uMake, uColor, uCarType)
        
        # retrieves the assigned CarID by the database
        carID = dbu.get_car_id(uVin)
        
        # sets the CarID for the car object
        car_object.car_id = carID
        
        # inserts the car object into the inventory
        self.inventory.append(car_object)
        
        index = len(self.inventory)
        repr(self.inventory[index - 1])


    """
    # Function: get_inventory()
    # Input: None
    # Output: None
    # For testing purposes, prints out all the CarID of the car objects in whole_inventory
    # Description: gets all the information of each car from the database and stores it
    # in a car_object. And then, stores all the car_objects in an array
    """
    def initialize_inventory(self):
        
        # calls the function get_inventory() from the database class
        # it returns an array of tuples with all the information about the car
        for car in dbu.get_inventory():
            
            # creates an instance of the car class and initializes it
            # with the values returned by the database class 
            car_object = car_class.car(car[1], car[2], car[3], car[4], car[5], car[6], car[7], car[8], car[9], car[10])
            
            # sets the car_id field of the car objects with the car_id
            # provided by the database
            car_object.set_car_id(car[0])
            
            # adds each car object to the array self.whole_inventory
            self.inventory.append(car_object)
        
        # For testing purposes    
        for x in self.inventory:
            repr(x)
        
    
    """
    # Function: get_available_inventory()
    # Input: None
    # Output: None 
    # For testing purposes, prints out the car id of each car object
    # Description: gets all the information of cars with IsActive = 1
    # from the database and stores it in a car_object. 
    # And then, stores all the car_objects in an array
    # Does the same thing as get_inventory() 
    """
    def get_available_inventory(self):
        for x in self.database_object.get_active_inventory():
            car_object = car_class.car(x[1], x[2], x[3], x[4], x[5])
            car_object.set_car_id(x[0])
            self.available_inventory.append(car_object)
         
        # For testing purposes
        for x in self.available_inventory:
            print(x.get_car_id())
        
    # def get_cars_info(self):
        # for car in self.whole_inventory:
            # self.inventory_with_details.append(self.database_object.get_car_info(car))
            
        # for car in self.inventory_with_details:
            # print(car)
