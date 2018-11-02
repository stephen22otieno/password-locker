import unittest # Importing the unittest module
from password_locker import Password # Importing the password class

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    #Items up here ........

    def setUp(self):
        '''
        set up to run before each test cases.
        '''
        self.new_password = Password("Stephen","Otieno","Login","1234456789") #create password objects

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name,"Stephen")
        self.assertEqual(self.new_password.last_name,"Otieno")
        self.assertEqual(self.new_password.login,"Login")
        self.assertEqual(self.new_password.password,"123456789")

        # if __name__ == '__main__':
        #     unittest.main()

        def test_save_password(self):
            '''
            test_save_password test case to test if the password is saved into
            the password list
            '''
            self.new_password.save_password() # saving the new password
            self.assertEqual(len(Password_locker.password_list),1)

            # if __name__ == '__main__':
            #     unittest.main()

            # Items up here...

        def test_save_multiple_password(self):
            '''
            test_save_multiple_password to check if we can save multiple password
            objects to our password_list
            '''
            self.new_password.save_password()
            test_password = Password("Test","user","123456789","test.password") # new password
            test_password.save_password()
            self.assertEqual(len(Password-locker.password_list),2)


        # if __name__ == '__main__':
        #     unittest.main()


  # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Password_locker.password_list = []

     # other test cases here
    def test_save_multiple_password(self):
            '''
            test_save_multiple_password to check if we can save multiple password
            objects to our password_list
            '''
            self.new_password.save_password()
            test_password = Password("Test","user","0712345678","test@user.com") # new contact
            test_password.save_password()
            self.assertEqual(len(Password_locker.password_list),2)

            # if __name__ == '__main__':
            #      unittest.main()
                
                

