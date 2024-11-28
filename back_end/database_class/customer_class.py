class Customer:
    """
    Date of Creation: November 26, 2024
    Author: Elijah Sagaran and Nima Jafari
    
    Class that will hold informaiton about admin and the functionalities that the admin can do
    
    Attributes:
    -----------
    cust_id: int
        ID assigned by database to user
    user: str
        name of the user
    email: str
        Email of the user
    username: str
        the username of the user that will be used for logging in
    user_password: str
        the password of the user that will be used for logging in 
    dob: str
        date of birth of the user, used for authentication of resetting password
    """
    
    def __init__(self, cust_id: int, user: str, email: str, username: str, user_password:str, dob: str) -> None:
        self.cust_id = cust_id
        self.user = user
        self.email = email
        self.username = username
        self.password = user_password
        self.dob = dob
    
    def __repr__(self) -> str:
        return 'Customer Info: \n \
                Customer ID: {} \n \
                User: {} \n \
                Email: {} \n \
                Username: {} \n \
                Password: {} \n \
                DOB: {}'.format(self.cust_id, self.user, self.email, self.username, self.password, self.dob)
