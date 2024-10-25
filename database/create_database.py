import mysql.connector

def create_database(my_host, my_port, my_username, my_password):
    mydb = mysql.connector.connect(
        host = my_host,
        user = my_username,
        password = my_password,
        port = my_port
    )
     
    # creating instance of cursor class
    mycursor = mydb.cursor()
     
    # remove the previously made database making it possible to run the code again after modification
    mycursor.execute("DROP DATABASE IF EXISTS CARAPP")
    
    # creating databases 
    mycursor.execute("create database CARAPP")
     
    # getting a list of databases in localhost
    # mycursor.execute("show databases")
     
    # prints all values in the list mycursor
    # for x in mycursor:
       # print(x)
