class Password:
    """
    Class that generates new instances of password
    """

    password_locker = [] # Empty password list
     # Init method up here
    def save_password(self):

        '''
        save_password method saves password objects into password_list
        '''

        Password.password_list.append(self)
