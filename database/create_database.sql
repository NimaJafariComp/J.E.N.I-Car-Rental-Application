DROP DATABASE IF EXISTS CarAppProject;
create database CarAppProject;

use CarAppProject;

create table Vehicles(
	CarID int auto_increment primary key,
    VIN varchar(255) unique not null,
    Mileage bigint not null,
    MPG int not null,
    Price decimal(7, 2) not null,
    IsActive bool,
    LicensePlate char(7) unique not null
);

create table Administrator(
    AdminID int auto_increment primary key,
    `User` varchar(255) not null,           
    Email varchar(255) not null,           
    `Password` varchar(255) not null          
);

create table Customers(
	CustomerID int auto_increment primary key,
    FullName varchar(255) not null,
    DOB date not null,
    Email varchar(255)
);

create table Reservations(
	ReservationID int auto_increment primary key,
    StartDate date not null,
    EndDate date not null,
    Insurance boolean not null,
    CustomerID int not null,
    Vehicle int not null,
    constraint FK_CustomerReservation foreign key (CustomerID)
    references Customers(CustomerID),
    constraint FK_VehicleReservation foreign key (Vehicle)
    references Vehicles(CarID)
);

create table Reports(
	ReportID int auto_increment primary key,
    Damage varchar(255),
    GasAmount int not null,
    Vehicle int not null,
    Customer int not null,
    constraint FK_VehicleReport foreign key (Vehicle)
    references Vehicles(CarID),
    constraint FK_CustomerReport foreign key (Customer)
    references Customers(CustomerID)
);


insert into Vehicles (VIN, Mileage, MPG, Price, IsActive, LicensePlate)
values
	('1FTWW31P95EB34134', 600, 35, 150.0, 1, '7KJV105'),
	('5TDKK3DC9BS182760', 532, 25, 70.0, 1, '6IPZ437'),
	('JHLRE3H57AC023983', 234, 40, 80.0, 1, '5YGW550'),
	('JTKDE167060163343', 124, 42, 160.0, 1, '8CMH868'),
	('1GNUKKE34AR110094', 942, 50, 180.0, 1, '2LHU996');
    
insert into Administrator (`User`, Email, `Password`)
values
	('Admin', 'adminJeni@gmail.com', 'Admin1234');
    
    
insert into Customers (FullName, DOB, Email)
values
	('Elijah Sagaran', '2000-10-2', 'elijahsagaran@gmail.com'),
	('Johnny Aguilar', '2000-11-3', 'johnnyaguilar@gmail.com'),
	('Irma Alicon', '2000-12-4', 'irmaalicon@gmail.com'),
	('Nima Jafari', '2000-9-1', 'nimajafari@gmail.com');
    
insert into Reservations (StartDate, EndDate, Insurance, CustomerID, Vehicle)
values 
	('2024-01-19', '2024-02-19', 1, 1, 2),
	('2024-10-17', '2024-10-20', 0, 2, 2),
	('2024-12-09', '2024-12-29', 1, 1, 4),
	('2024-12-24', '2024-12-29', 1, 3, 5),
	('2024-12-28', '2024-12-30', 0, 4, 1);

insert into Reports (Damage, GasAmount, Vehicle, Customer)
values
	('Scratch on hood', 10, 1, 1),
	('Engine rattling', 11, 1, 2),
	('Dent on left door', 6, 4, 2),
	('AC not working', 9, 5, 3),
	('Flat tire', 12, 2, 4);
    
select * from Vehicles;
select * from Administrator;
select * from Customers;
select * from Reservations;
select * from Reports;
    
    
    