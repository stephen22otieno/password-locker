import unittest # Importing the unittest module
from password import Password # Importing the password class


class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

        # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Password("Stephen","Otieno","0746432419","stephenombiro22@gmail.com") # create password object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name,"James")
        self.assertEqual(self.new_password.last_name,"Muriuki")
        self.assertEqual(self.new_password.phone_number,"0712345678")
        self.assertEqual(self.new_password.email,"james@ms.com")


# if __name__ == '__main__':
#     unittest.main()

    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

        # if __name__ ==  '__main__':
        #     unittest.main() 


 # Items up here...

    def test_save_multiple_password(self):
        '''
        test_save_multiple_password to check if we can save multiple password
        objects to our password_list
        '''
        self.new_password.save_password()
        test_password = password("Test","user","0746432419","test@user.com") # new password
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)


        # if __name__ == '__main__':
        #     unittest.main()  

        # setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Password.password_list = []

# other test cases here
    def test_save_multiple_password(self):
        '''
        test_save_multiple_password to check if we can save multiple password
        objects to our password_list
        '''
        self.new_password.save_password()
        test_password = Password("Test","user","0746432419","test@user.com") # new password
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)

        # if __name__ == '__main__':
            # unittest.main()



# More tests above
    def test_delete_password(self):
        '''
        test_delete_password to test if we can remove a password from our password list
        '''
        self.new_password.save_password()
        test_password = Password("Test","user","0746432419","test@user.com") # new password
        test_password.save_password()

        self.new_Password.delete_password()# Deleting a password object
        self.assertEqual(len(Password.password_list),1)




    def test_find_password_by_number(self):
        '''
        test to check if we can find a password by phone number and display information
        '''

        self.new_contact.save_contact()
        test_password = Password("Test","user","0746432419","test@user.com") # new password
        test_password.save_password()

        found_password = Password.find_by_number("0746432419")

        self.assertEqual(found_password.email,test_password.email)

        if __name__ == '__main__':
            unittest.main()   


   def test_display_all_passwords(self):
        '''
        method that returns a list of all passwords saved
        '''

        self.assertEqual(Password.display_passwords(),Password.password_list)  



        import pyperclip
        ......................
    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found password
        '''

        self.new_password.save_password()
        Password.copy_email("0746432419")

        self.assertEqual(self.new_password.email,pyperclip.paste())