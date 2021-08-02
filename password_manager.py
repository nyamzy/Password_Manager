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
        


  pass

class Credentials:
  '''
  Class that generates new instances of credentials for users
  '''
  pass

