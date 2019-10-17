INSERT INTO cars (VIN, Model, Years, Color)
Values ('3K096I98581DHSNUP', 'Volkswagen', 2019, 'Blue'),
	   ('ZM8G7BEUQZ97IH46V', 'Peugeot', 2019, 'Red'),
	   ('RKXVNNIHLVVZOUB4M', 'Ford', 2019, 'White'),
	   ('HKNDGS7CU31E9Z7JW', 'Toyota', 2019, 'Silver'),
	   ('DAM41UDN3CHU2WVF6', 'Volvo', 2019, 'Gray'),
	   ('DAM41UDN3CHU2WVF6', 'Volvo', 2019, 'Gray');
alter table salesperson auto_increment = 0;
drop table salesperson; 
INSERT INTO customers (Cust_ID,Name,Phone,Email,Address,City,State,Country,Zip_Code)
Values (10001, 'Pablo Picasso', '+34636176382', '-', 'Paseo de la Chopera 14', 'Madrid', 'Madrid', 'Spain', 28045),
	   (20001, 'Abraham Lincoln', '+13059077086', '-', '120 SW 8th St', 'Miami', 'Florida', 'USA', 33130),
       (30001, 'Napoleon Bonaparte', '+33179754000', '-', '40 Rue du Colisee', 'Paris', 'Ile-de-France', 'France', 75008);
       
INSERT INTO salesperson (Staff_ID,Name,Store_City)
Values  ('00001', 'Petey Cruiser', 'Madrid'),
		('00002', 'Anna Sthesia', 'Barcelona'),
		('00003', 'Paul Molive', 'Berlin'),
        ('00004', 'Gail Forcewind', 'Paris'),
		('00005', 'Paige Turner', 'Mimia'),
        ('00006', 'Bob Frapples', 'Mexico City'),
        ('00007', 'Walter Melon', 'Amsterdam'),
        ('00008', 'Shonda Leer', 'Sao Paulo');
drop table Invoice;	
INSERT INTO Invoice (Invoice_ID,Date,Car_ID,Cust_ID,Staff_ID)
Values ('852399038', '2018-08-22', 1, 2 , 4),
	   ('731166526', '2018-12-31', 4, 1 , 6),
       ('271135104', '2019-01-22', 3, 3 , 8);
	   