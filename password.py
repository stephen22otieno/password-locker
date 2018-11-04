class Password:
    """
    Class that generates new instances of passwords.
    """

    password_list = [] # Empty password list

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email  


    password_list = [] # Empty password list
 # Init method up here
    def save_password(self):

        '''
        save_password method saves password objects into password_list
        '''

        Password.password_list.append(self)