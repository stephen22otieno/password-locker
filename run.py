from password import Password  

def create_password(fname,lname,phone,email):
    '''
    Function to create a new password
    '''
    new_password = Password(fname,lname,phone,email)
    return new_passwword 


def save_passwords(password):
    '''
    Function to save password
    '''
    password.save_password()  


def del_password(password):
    '''
    Function to delete a password
    '''
    password.delete_password()