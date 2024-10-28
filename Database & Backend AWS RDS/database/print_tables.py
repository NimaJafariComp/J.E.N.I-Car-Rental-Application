import pyodbc

def print_tables(my_username, my_password):
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

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM Vehicles")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        
    mycursor.execute("SELECT * FROM Administrator")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
       
    mycursor.execute("SELECT * FROM Customers")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        
    mycursor.execute("SELECT * FROM Reservations")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        
    mycursor.execute("SELECT * FROM Reports")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    mycursor.close()
    mydb.close()
