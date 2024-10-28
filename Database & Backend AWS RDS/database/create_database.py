import pyodbc

def create_database(my_username, my_password):
    rds_endpoint = "jenni-database.czg446yqs8iz.us-west-1.rds.amazonaws.com"
    db_name = "Jenni-Database"  # Ensure the name matches what you want to create
    port = 1433

    # Create the connection string for SQL Server, connecting to master database
    connection_string = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={rds_endpoint},{port};'
        f'UID={my_username};PWD={my_password};'
          # Connect to the master database
    )

    # Connect to SQL Server with autocommit enabled
    mydb = pyodbc.connect(connection_string, autocommit=True)

    # Create an instance of the cursor
    mycursor = mydb.cursor()

    try:
        
        # Drop the database if it exists
        mycursor.execute(f"""
            IF EXISTS (SELECT * FROM sys.databases WHERE name = '{db_name}')
            BEGIN
                ALTER DATABASE [{db_name}] SET AUTO_CLOSE OFF;
                DECLARE @sql NVARCHAR(MAX) = 'DROP DATABASE [' + '{db_name}' + ']';
                EXEC sp_executesql @sql;
            END
        """)

        # Create the new database
        mycursor.execute(f"CREATE DATABASE [{db_name}]")

        # List and print all databases
        mycursor.execute("SELECT name FROM sys.databases")
        for x in mycursor:
            print(x[0])  # Print each database name

    except pyodbc.Error as e:
        print("Error occurred:", e)

    finally:
        # Close the cursor and connection
        mycursor.close()
        mydb.close()

# Example usage
my_username = "admin"
my_password = "JenniProject2024"
create_database(my_username, my_password)
