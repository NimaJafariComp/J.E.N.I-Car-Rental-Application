import mysql.connector

def print_tables(my_username, my_password):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = my_username,
        password = my_password,
        database = "carappproject"
    )

    mycursor = mydb.cursor()

    mycursor.execute("select * from Vehicles")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mycursor.execute("select * from VehicleType")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
        
    mycursor.execute("select * from Administrator")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
       
    mycursor.execute("select * from Customers")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
        
    mycursor.execute("select * from Reservations")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
        
    mycursor.execute("select * from Reports")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
