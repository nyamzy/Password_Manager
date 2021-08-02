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
    self.new_user = User("John", "Nyamweya", "nyamzy", "johnnyamweya@gmail.com", "hello123",) #create new user object


  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name,"John")
    self.assertEqual(self.new_user.last_name,"Nyamweya")
    self.assertEqual(self.new_user.user_name,"nyamzy")
    self.assertEqual(self.new_user.email,"johnnyamweya@gmail.com")
    self.assertEqual(self.new_user.password,"hello123")

if __name__ == '__main__':
  unittest.main()