import mysql.connector

def create_tables(my_username, my_password):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = my_username,
        password = my_password,
        database = "carappproject"
    )

    # creates an instance of cursor class 
    mycursor = mydb.cursor()

    # creates Vehicles tables with the following data fields:
    # CarID: Automatic assignment, increments by 1 per insert of car. 
    #        Used as reference key by other tables: VehicleType, Reservation, Reports
    # VIN: String input from user
    # Mileage: Integer input from user. BIGINT type lets users store big value for Mileage
    # MPG: Integer input from user.
    # Price: Decimal/Float input from user.
    # IsActive: Boolean input. False = 0, True = any other number other than 0.
    # LicensePlate: A string input from user. Limited to 7 characters
    # Data fields with "not null" must have an input from the user
    mycursor.execute("create table Vehicles("+
                        "CarID int auto_increment primary key," +
                        "VIN varchar(255) unique not null," +
                        "Mileage bigint not null," +
                        "MPG int not null," +
                        "Price decimal(7, 2) not null," +
                        "IsActive bool," +
                        "LicensePlate char(7) unique not null)")

    # creates VehicleType tables with the following data fields:
    # CarYear: A year input. Input must be 4 characters. 
    # Model: A string input from user
    # Make: A string input from user
    # CarType: A string input from user
    # CarID: Integer input from user. A foreign key with reference to Vehicle
    mycursor.execute("create table VehicleType("+
                         "CarYear year not null,"+
                         "Model varchar(255) not null,"+
                         "Make varchar(255) not null,"+
                         "Color varchar(255) not null,"+
                         "CarType varchar(255),"+
                         "CarID int unique not null,"+
                         "constraint FK_VehicleType foreign key (CarID) references Vehicles(CarID))")

    # create Customers tables with the following data fields:
    # CustomerID: Automatic assignment. Increments by 1 per data insert.
    #             Reference key for Reports and Reservations
    # FullName: A string input from user
    # DOB: A date input from user. Format is: yyyy-mm-dd
    # Email: A string input from user
    mycursor.execute("create table Customers(" +
                        "CustomerID int auto_increment primary key," +
                        "FullName varchar(255) not null," +
                        "DOB date not null," +
                        "Email varchar(255))")

    mycursor.execute("create table Reservations(" +
                        "ReservationID int auto_increment primary key," +
                        "StartDate date not null," +
                        "EndDate date not null," +
                        "Insurance boolean not null," +
                        "CustomerID int not null," +
                        "Vehicle int not null," +
                        "constraint FK_CustomerReservation foreign key (CustomerID) references Customers(CustomerID)," +
                        "constraint FK_VehicleReservation foreign key (Vehicle) references Vehicles(CarID))")

    mycursor.execute("create table Reports(" +
                        "ReportID int auto_increment primary key," +
                        "Damages varchar(255)," +
                        "GasAmount int not null," +
                        "Vehicle int not null," +
                        "Customer int not null," +
                        "constraint FK_VehicleReport foreign key (Vehicle) references Vehicles(CarID)," +
                        "constraint FK_CustomerReport foreign key (Customer) references Customers(CustomerID))")

    sql_insert_vehicles = "insert into Vehicles (VIN, Mileage, MPG, Price, IsActive, LicensePlate) values (%s, %s, %s, %s, %s, %s)"
    vehicle_values = [
            ('1FTWW31P95EB34134', 600, 35, 150.0, 1, '7KJV105'),
            ('5TDKK3DC9BS182760', 532, 25, 70.0, 1, '6IPZ437'),
            ('JHLRE3H57AC023983', 234, 40, 80.0, 1, '5YGW550'),
            ('JTKDE167060163343', 124, 42, 160.0, 1, '8CMH868'),
            ('1GNUKKE34AR110094', 942, 50, 180.0, 1, '2LHU996')
    ]

    sql_insert_vehicle_types = "insert into VehicleType (CarYear, Model, Make, Color, CarType, CarID) values (%s, %s, %s, %s, %s, %s)"
    vehicle_type_values = [
        ('2016', 'Camaro', 'Chevrolet', 'Red', 'Pony Car', 1),
        ('2013', 'Sentra', 'Nissan', 'Grey', 'Compact Car', 2),
        ('2019', 'Sorento', 'Kia', 'Black', 'SUV',  3),
        ('2017', '911 Carrera 4 GTS', 'Porsche', 'White', 'Coupe', 4),
        ('2019', 'R8', 'Audi', 'Grey', 'Sports Car', 5)
    ]
    
    sql_insert_customers = "insert into Customers (FullName, DOB, Email) values (%s, %s, %s)"
    customer_values = [
            ('Elijah Sagaran', '2000-10-2', 'elijahsagaran@gmail.com'),
            ('Johnny Aguilar', '2000-11-3', 'johnnyaguilar@gmail.com'),
            ('Irma Alicon', '2000-12-4', 'irmaalicon@gmail.com'),
            ('Nima Jafari', '2000-9-1', 'nimajafari@gmail.com')
    ]

    sql_insert_reservations = "insert into Reservations (StartDate, EndDate, Insurance, CustomerID, Vehicle) values (%s, %s, %s, %s, %s)"
    reservation_values = [
            ('2024-01-19', '2024-02-19', 1, 1, 2),
            ('2024-10-17', '2024-10-20', 0, 2, 2),
            ('2024-12-09', '2024-12-29', 1, 1, 4),
            ('2024-12-24', '2024-12-29', 1, 3, 5),
            ('2024-12-28', '2024-12-30', 0, 4, 1)
    ]

    sql_insert_reports = "insert into Reports (Damages, GasAmount, Vehicle, Customer) values (%s, %s, %s, %s)"
    report_values = [
            ('Scratch on hood', 10, 1, 1),
            (None, 11, 1, 2),
            ('Dent on left door', 6, 4, 2),
            (None, 9, 5, 3),
            (None, 12, 2, 4)
    ]

    mycursor.executemany(sql_insert_vehicles, vehicle_values)
    mycursor.executemany(sql_insert_vehicle_types, vehicle_type_values)
    mycursor.executemany(sql_insert_customers, customer_values)
    mycursor.executemany(sql_insert_reservations, reservation_values)
    mycursor.executemany(sql_insert_reports, report_values)
    mydb.commit()

