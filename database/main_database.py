from .create_database import create_database
from .create_tables import create_tables
from .print_tables import print_tables

def initialize_database(my_username, my_password):
    create_database(my_username, my_password)
    create_tables(my_username, my_password)
    print_tables(my_username, my_password)
    
