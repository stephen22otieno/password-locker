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

        if __name__ ==  '__main__':
            unittest.main()