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

         @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a password that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            password of person that matches the number.
        '''

        for password in cls.password_list:
            if password.phone_number == number:
                return password   



    def test_password_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the pasword.
        '''

        self.new_password.save_password()
        test_password = Password("Test","user","0746432419","test@user.com") # new password
        test_password.save_password()

        password_exists = Password.password_exist("0746432419")

        self.assertTrue(password_exists)  



    @classmethod
    def password_exist(cls,number):
        '''
        Method that checks if a password exists from the password list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the password exists
        '''
        for password in cls.password_list:
            if password.phone_number == number:
                    return True

        return False