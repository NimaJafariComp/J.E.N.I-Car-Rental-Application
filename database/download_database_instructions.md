This file will explain how to set up the database for our J.E.N.I. Car Rental Application Project

Please follow the steps accordingly

1. Install MySQL
	- If you are using Windows, use this link: https://dev.mysql.com/downloads/installer/
	- For other OSs, refer to this website: https://dev.mysql.com/doc/mysql-getting-started/en/

2. Execute MySQL downloader
	- You can download the Server or Full version, it is your choice
	- You can change the default directory. If you do, please save the directory path for later
	- MySQL will prompt the user to create a password. Please create one and save it for later
	- The password is important for connecting to the database later
	
3. Run MySQL in Command Prompt in Windows
	- This is not a necessary step, but it shows you how to access MySQL through the Command Prompt
	1. Open a Command Prompt window
	2. In the prompt, input: cd "path-to-MySQL-bin", no need to put the quotation marks with the actual path
	3. After the directory is changed, type: mysql -u "usernme" -p 
		- "username" is most likely be root if you did not change it when downloading MySQL
		- -p prompts MySQL to ask for the password for the database
	4. Enter your password and press enter
	5. The prompt "mysql>" will show if you have successfully logged into your MySQL
	6. From here, you can quit out of MySQL and exit the Command Prompt
		- To quit, simply enter: quit;

4. Download MySQL Connector for Pyton
	- For the Python code to work, you need to download the MySQL Connector Library
	1. Open up a Command Prompt window
	2. In the promp, input: cd "path-to-pip.exe"
	3. After changing the directory, type the following: pip install mysql-connector-python
	4. After downloading, you can test it by creating a test.py file with the line:
		import mysql.connector
	5. Run the file.
		- If it does not produce an error, MySQL Connector was downloaded properly
		
5. MySQL Workbench Download
	- In this folder, I have also provided the MySQL .sql file
	- If you want to create the database through MySQL script, you can use the file:
		create_database.sql 
	- To run this script, you can download MySQL Workbench. This environment displays 
		the schemas of your databases, tables, and other useful information
	- MySQL Workbench can also be used to ensure that the database was indeed created by the Python code
		as it updates real-time and will display new databases, tables, etc. on its schemas window
	1. To download, use this link: https://dev.mysql.com/downloads/workbench/
	2. Execute the download
	3. Open the MySQL Workbench
 	4. Press "Local instance MySQL80" under MySQL Connections
  	5. Enter your password and press ok	 	

6. Running the Code
	- As mentioned above, you can either use the Python files or the MySQL file that is given in the folder
	- Follow accordingly based on which one you choose to run
	
	- For Python Files:
	1. Download these files:
		create_database.py
		create_tables.py
		print_tables.put
		main_database.py
		In the same directory, in no particular order.
	2. Open the main_database.py file and input your username in the variable my_username
		and your password in the variable my_password
		- Again, note that your username will be "root" if you did not change it
			when downloading MySQL
	3. After setting your username and password, run the code 		
	4. This should give you an output, in some format, of the following:
	
		(1, '1FTWW31P95EB34134', 600, 35, Decimal('150.00'), 1, '7KJV105')
		
  		(2, '5TDKK3DC9BS182760', 532, 25, Decimal('70.00'), 1, '6IPZ437')
		
  		(3, 'JHLRE3H57AC023983', 234, 40, Decimal('80.00'), 1, '5YGW550')
		
  		(4, 'JTKDE167060163343', 124, 42, Decimal('160.00'), 1, '8CMH868')
		
  		(5, '1GNUKKE34AR110094', 942, 50, Decimal('180.00'), 1, '2LHU996')
		
  		(1, 'Elijah Sagaran', datetime.date(2000, 10, 2), 'elijahsagaran@gmail.com')
		
  		(2, 'Johnny Aguilar', datetime.date(2000, 11, 3), 'johnnyaguilar@gmail.com')
		
  		(3, 'Irma Alicon', datetime.date(2000, 12, 4), 'irmaalicon@gmail.com')
		
  		(4, 'Nima Jafari', datetime.date(2000, 9, 1), 'nimajafari@gmail.com')
		
  		(1, datetime.date(2024, 1, 19), datetime.date(2024, 2, 19), 1, 1, 2)
		
  		(2, datetime.date(2024, 10, 17), datetime.date(2024, 10, 20), 0, 2, 2)
		
  		(3, datetime.date(2024, 12, 9), datetime.date(2024, 12, 29), 1, 1, 4)
		
  		(4, datetime.date(2024, 12, 24), datetime.date(2024, 12, 29), 1, 3, 5)
		
  		(5, datetime.date(2024, 12, 28), datetime.date(2024, 12, 30), 0, 4, 1)
		
  		(1, 'Scratch on hood', 10, 1, 1)
		
  		(2, None, 11, 1, 2)
		
  		(3, 'Dent on left door', 6, 4, 2)
		
  		(4, None, 9, 5, 3)
		
  		(5, None, 12, 2, 4)
		
		This example output is from NotePad++, output from different IDE will vary.
		But as long as the data values are the same, it is fine 
		
	- For SQL File
	1. Download the file:
		create_database.sql
	2. Open the file in the MySQL Workbench
		- To do this, simply open the MySQL Workbench and locate the "Open a SQL Script File"
			button. This button should be on the top left, right below the "Edit" button
	3. Run the Script
		- To do this, click the Lightning button that is located in the toolbar right above
			the script window. 
	4. This should prompt 4 different Result Grids:
		Vehicles, Customers, Reservations, Reports
		
	- Seeing the output is confirmation that the database has been downloaded in your Computer/Laptop
	
