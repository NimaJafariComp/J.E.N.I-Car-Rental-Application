import class_database
import car_class

class inventory:
    
    # initializes the inventory object
    # Input: username, a string
    #        password, a string
    # self.whole_inventory an array of car objects 
    # self.available_inventory an array of car objects where IsActive = 1
    # self.database_object is the database class object needed to access
    # the database
    def __init__(self, username, password):
        self.whole_inventory = []
        self.available_inventory = []
        # self.inventory_with_details = []
        self.database_object = class_database.test(username, password)
       
    
    # Function: add_car(uVin, uMileage, uMPG, uPrice, uLicensePlate)
    # Input: uVin, a string
    #        uMileage, an integer
    #        uMPG, an integer
    #        uPrice, a float
    #        uLicensePlate, a string
    # Output: None
    # For testing purposes, it prints out the self.whole_inventory
    # Description: adds a car to the inventory
    def add_car(self, uVin, uMileage, uMPG, uPrice, uLicensePlate):
        
        # uses database object to insert car into the database 
        self.database_object.add_car(uVin, uMileage, uMPG, uPrice, uLicensePlate)
        
        # initializes a car object for the new car with the provided information
        car_object = car_class.car(uVin, uMileage, uMPG, uPrice, uLicensePlate)
        
        # retrieves the assigned CarID by the database
        carID = self.database_object.get_car_id(uVin)
        
        # sets the CarID for the car object
        car_object.set_car_id(carID)
        
        # inserts the car object into the whole inventory
        self.whole_inventory.append(car_object)
        
        # inserts the car object into the available inventory
        self.available_inventory.append(car_object)
        
    
    def add_car_type(self, uCarYear, uModel, uMake, uColor, uCarType, uCarID):
        pass
        
    # Function: get_inventory()
    # Input: None
    # Output: None
    # For testing purposes, prints out all the CarID of the car objects in whole_inventory
    # Description: gets all the information of each car from the database and stores it
    # in a car_object. And then, stores all the car_objects in an array
    def get_inventory(self):
        
        # calls the function get_inventory() from the database class
        # it returns an array of tuples with all the information about the car
        for x in self.database_object.get_inventory():
            
            # creates an instance of the car class and initializes it
            # with the values returned by the database class 
            car_object = car_class.car(x[1], x[2], x[3], x[4], x[5])
            
            # sets the car_id field of the car objects with the car_id
            # provided by the database
            car_object.set_car_id(x[0])
            
            # adds each car object to the array self.whole_inventory
            self.whole_inventory.append(car_object)
            
        
        # For testing purposes
        for x in self.whole_inventory:
            print(x.get_car_id())
            
        # For testing purposes    
        print("end of inventory\n")
    
    # Function: get_available_inventory()
    # Input: None
    # Output: None 
    # For testing purposes, prints out the car id of each car object
    # Description: gets all the information of cars with IsActive = 1
    # from the database and stores it in a car_object. 
    # And then, stores all the car_objects in an array
    # Does the same thing as get_inventory() 
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
