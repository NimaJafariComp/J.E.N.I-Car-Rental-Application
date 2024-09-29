import mysql.connector

def create_database(my_username, my_password):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = my_username,
        password = my_password
    )
     
    # creating instance of cursor class
    mycursor = mydb.cursor()
     
    # creating databases 
    mycursor.execute("create database CarAppProject")
     
    # getting a list of databases in localhost
    mycursor.execute("show databases")
     
    # prints all values in the list mycursor
    for x in mycursor:
       print(x)