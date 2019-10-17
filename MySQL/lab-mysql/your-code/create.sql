create database My_SQL_LAB;
use My_SQL_LAB;

drop table Cars;
drop table Invoice;
drop table SalesPerson;
drop table Customers; 

create table Cars( 
ID int auto_increment,
Car_ID VARCHAR(10),
VIN VARCHAR(17),
Model VARCHAR(20),
Years CHAR(4),
Color VARCHAR(20),
Primary Key (ID));

create table Invoice(
ID int auto_increment,
Invoice_ID VARCHAR(10),
Staff_ID int,
Date DATETIME,
Car_ID int,
Cust_ID int,
Primary Key (ID),
Foreign Key (Staff_ID) references SalesPerson(ID),
Foreign Key (Car_ID) references Cars(ID),
Foreign Key (Cust_ID) references Customers(ID));

create table SalesPerson(
ID int auto_increment,
Staff_ID VARCHAR(10), 
Name VARCHAR(40), 
Store_City VARCHAR(30),
primary key (ID));

create table Customers(
ID int auto_increment,
Cust_ID VARCHAR(10),
Name VARCHAR(40),
Phone VARCHAR(20),
Email VARCHAR(30),
Address VARCHAR(30),
City VARCHAR(20),
State VARCHAR(30),
Country VARCHAR(20),
Zip_Code CHAR(5),
primary key (ID));