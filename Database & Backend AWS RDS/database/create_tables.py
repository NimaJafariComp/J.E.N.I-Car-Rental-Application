import pyodbc

def create_tables(my_username, my_password):
    rds_endpoint = "jenni-database.czg446yqs8iz.us-west-1.rds.amazonaws.com"
    db_name = "Jenni-Database"
    port = 1433

    # Create the connection string for SQL Server, connecting to master database
    connection_string = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={rds_endpoint},{port};'
        f'DATABASE={db_name};'
        f'UID={my_username};PWD={my_password};'
          # Connect to the master database
    )

    # Connect to SQL Server with autocommit enabled
    mydb = pyodbc.connect(connection_string)

    # creates an instance of cursor class 
    mycursor = mydb.cursor()

    """
    # creates Vehicles tables with the following data fields:
    # CarID: Automatic assignment, increments by 1 per insert of car. 
    #        Used as reference key by other tables: VehicleType, Reservation, Reports
    # VIN: String input from user
    # Mileage: Integer input from user. BIGINT type lets users store big value for Mileage
    # MPG: Integer input from user.
    # Price: Decimal/Float input from user.
    # IsActive: Boolean input. False = 0, True = any other number other than 0.
    # LicensePlate: A string input from user. Limited to 7 characters
    # CarYear: A year input. Input must be 4 characters. 
    # Model: A string input from user
    # Make: A string input from user
    # CarType: A string input from user
    # Data fields with "not null" must have an input from the user
    """
    mycursor.execute("CREATE TABLE Vehicles ( \
                        CarID INT IDENTITY(1,1) PRIMARY KEY, \
                        VIN VARCHAR(255) UNIQUE NOT NULL, \
                        Mileage BIGINT NOT NULL, \
                        MPG INT NOT NULL, \
                        Price DECIMAL(7, 2) NOT NULL, \
                        IsActive BIT DEFAULT 1, \
                        LicensePlate CHAR(7) UNIQUE NOT NULL, \
                        CarYear INT NOT NULL, \
                        Model VARCHAR(255) NOT NULL, \
                        Make VARCHAR(255) NOT NULL, \
                        Color VARCHAR(255) NOT NULL, \
                        CarType VARCHAR(255))")
    
    """
    # Create Administrator table with the following data fields:
    # AdminID: Automatic assignment. Increments by 1 per data insert.
    #           Primary key for identifying administrators uniquely.
    # User: A string input from user. Represents the username for the administrator.
    # Email: A string input from user. Represents the email address of the administrator.
    # Password: A string input from user.
    """
    mycursor.execute("CREATE TABLE Administrator ( \
                        AdminID INT IDENTITY(1,1) PRIMARY KEY, \
                        [User] VARCHAR(255) NOT NULL, \
                        Email VARCHAR(255) NOT NULL, \
                        [Password] VARCHAR(255) NOT NULL)")

    """
    # create Customers tables with the following data fields:
    # CustomerID: Automatic assignment. Increments by 1 per data insert.
    #             Reference key for Reports and Reservations
    # FullName: A string input from user
    # DOB: A date input from user. Format is: yyyy-mm-dd
    # Email: A string input from user
    """
    mycursor.execute("CREATE TABLE Customers ( \
                        CustomerID INT IDENTITY(1,1) PRIMARY KEY, \
                        FullName VARCHAR(255) NOT NULL, \
                        DOB DATE NOT NULL, \
                        Email VARCHAR(255))")

    mycursor.execute("CREATE TABLE Reservations ( \
                        ReservationID INT IDENTITY(1,1) PRIMARY KEY, \
                        StartDate DATE NOT NULL, \
                        EndDate DATE NOT NULL, \
                        Insurance BIT NOT NULL, \
                        CustomerID INT NOT NULL, \
                        Vehicle INT NOT NULL, \
                        CONSTRAINT FK_CustomerReservation FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, \
                        CONSTRAINT FK_VehicleReservation FOREIGN KEY (Vehicle) REFERENCES Vehicles(CarID) ON DELETE CASCADE)")

    mycursor.execute("CREATE TABLE Reports ( \
                        ReportID INT IDENTITY(1,1) PRIMARY KEY, \
                        Damages VARCHAR(255), \
                        GasAmount INT NOT NULL, \
                        Vehicle INT NOT NULL, \
                        ReservationID INT, \
                        CONSTRAINT FK_VehicleReport FOREIGN KEY (Vehicle) REFERENCES Vehicles(CarID) ON DELETE CASCADE, \
                        CONSTRAINT FK_ReservationReport FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID) ON DELETE NO ACTION)")

    sql_insert_vehicles = "INSERT INTO Vehicles (VIN, Mileage, MPG, Price, LicensePlate, CarYear, Model, Make, Color, CarType) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    vehicle_values = [
            ('1FTWW31P95EB34134', 600, 35, 150.0, '7KJV105', '2016', 'Camaro', 'Chevrolet', 'Red', 'Pony Car'),
            ('5TDKK3DC9BS182760', 532, 25, 70.0, '6IPZ437', '2013', 'Sentra', 'Nissan', 'Grey', 'Compact Car'),
            ('JHLRE3H57AC023983', 234, 40, 80.0, '5YGW550', '2019', 'Sorento', 'Kia', 'Black', 'SUV'),
            ('JTKDE167060163343', 124, 42, 160.0, '8CMH868', '2017', '911 Carrera 4 GTS', 'Porsche', 'White', 'Coupe'),
            ('1GNUKKE34AR110094', 942, 50, 180.0, '2LHU996', '2019', 'R8', 'Audi', 'Grey', 'Sports Car')
    ]
  
    sql_insert_admin = "INSERT INTO Administrator ([User], Email, [Password]) VALUES (?, ?, ?)"
    admin_values = [
          ('Admin', 'adminJeni@gmail.com', 'Admin1234')
    ]
    
    sql_insert_customers = "INSERT INTO Customers (FullName, DOB, Email) VALUES (?, ?, ?)"
    customer_values = [
            ('Elijah Sagaran', '2000-10-02', 'elijahsagaran@gmail.com'),
            ('Johnny Aguilar', '2000-11-03', 'johnnyaguilar@gmail.com'),
            ('Irma Alicon', '2000-12-04', 'irmaalicon@gmail.com'),
            ('Nima Jafari', '2000-09-01', 'nimajafari@gmail.com')
    ]

    sql_insert_reservations = "INSERT INTO Reservations (StartDate, EndDate, Insurance, CustomerID, Vehicle) VALUES (?, ?, ?, ?, ?)"
    reservation_values = [
            ('2024-01-19', '2024-02-19', 1, 1, 2),
            ('2024-10-17', '2024-10-20', 0, 2, 2),
            ('2024-12-09', '2024-12-29', 1, 1, 4),
            ('2024-12-24', '2024-12-29', 1, 3, 5),
            ('2024-12-28', '2024-12-30', 0, 4, 1)
    ]

    sql_insert_reports = "INSERT INTO Reports (Damages, GasAmount, Vehicle, ReservationID) VALUES (?, ?, ?, ?)"
    report_values = [
            ('Scratch on hood', 10, 1, 1),
            ('Engine rattling', 11, 1, 2),
            ('Dent on left door', 6, 4, 2),
            ('AC not working', 9, 5, 3),
            ('Flat tire', 12, 2, 4)
    ]

    mycursor.executemany(sql_insert_vehicles, vehicle_values)
    mycursor.executemany(sql_insert_customers, customer_values)
    mycursor.executemany(sql_insert_admin, admin_values)
    mycursor.executemany(sql_insert_reservations, reservation_values)
    mycursor.executemany(sql_insert_reports, report_values)
    
    mycursor.commit()
    mycursor.close()
    mydb.close()
