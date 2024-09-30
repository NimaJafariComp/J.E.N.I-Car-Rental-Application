import mysql.connector

def create_database(my_username, my_password):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = my_username,
        password = my_password
    )
     
    # creating instance of cursor class
    mycursor = mydb.cursor()
     
    # remove the previously made database making it possible to run the code again after modification
    mycursor.execute("DROP DATABASE IF EXISTS CarAppProject")
    
    # creating databases 
    mycursor.execute("create database carappproject")
     
    # getting a list of databases in localhost
    mycursor.execute("show databases")
     
    # prints all values in the list mycursor
    for x in mycursor:
       print(x)
