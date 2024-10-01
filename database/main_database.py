import create_database
import create_tables
import print_tables

def main():
    my_username = input("Enter your MySQL username: ")
    my_password = input("Enter your MySQL password: ")
    create_database.create_database(my_username, my_password)
    create_tables.create_tables(my_username, my_password)
    print_tables.print_tables(my_username, my_password)
    
main()
