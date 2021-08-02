class User:
  '''
  Class that generates new instances of users
  '''

  users = [] #Create empty list that will store the users


  def __init__(self, first_name, last_name, user_name, email, password):
    '''
    __init__ method that defines properties for our objects
    '''
    self.first_name = first_name
    self.last_name = last_name
    self.user_name = user_name
    self.email = email
    self.password = password
  
  def save_user(self):
    '''
    save user method that saves the users to the users list
    '''
    User.users.append(self)

  def delete_user(self):
    '''
    delete user method that deletes a user from the users list
    '''
    User.users.remove(self)

  @classmethod
  def find_by_username(cls,username):
    '''
    find by username method that takes in a username and returns a user that matches the same username
    '''
    for user in cls.users:
      if user.user_name == username:
        return user

  @classmethod
  def display_users(cls):
    '''
    display users method that returns a list of all users saved
    '''
    return cls.users

  @classmethod
  def user_exist(cls,username):
    '''
    user exists method that checks if a user exists from the users list
    '''
    for user in cls.users:
      if user.user_name == username:
        return True

    return False


  pass




class Credentials:
  '''
  Class that generates new instances of credentials for users
  '''

  accounts = []


  def __init__(self, user_name, application , password):
    '''
    __init__ method that defines properties for our objects
    '''
    self.user_name = user_name
    self.application = application
    self.password = password

  def save_credential(self):
    '''
    save credential method that saves the credentials to the credentials list
    '''
    Credentials.accounts.append(self)

  def delete_credential(self):
    '''
    delete credential method that deletes a credential from the accounts list
    '''
    Credentials.accounts.remove(self)

  @classmethod
  def display_credentials(cls):
    '''
    display credentials method that returns a list of all credentials saved
    '''
    return cls.accounts

  @classmethod
  def credential_exist(cls,username):
    '''
    credential exists method that checks if a user exists from the users list
    '''
    for credential in cls.accounts:
      if credential.user_name == username:
        return True

    return False

  pass

