from .create_database import create_database
from .create_tables import create_tables
from .print_tables import print_tables

def initialize_database(my_host, my_port, my_username, my_password):
    create_database(my_host, my_port, my_username, my_password)
    create_tables(my_host, my_port, my_username, my_password)
    print_tables(my_host, my_port, my_username, my_password)
    
def print_only(my_host, my_port, my_username, my_password):
    print_tables(my_host, my_port, my_username, my_password)