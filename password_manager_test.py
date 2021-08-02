import unittest
from password_manager import User, Credentials

class TestUser(unittest.TestCase):
  '''
  Subclass for testing the cases for the user class behaviours
  '''
  def setUp(self):
    '''
    Set up method that runs before each test case
    '''
    self.new_user = User("John", "Nyamweya", "0712345678", "johnnyamweya@gmail.com", "hello123",) #create new user object
    
