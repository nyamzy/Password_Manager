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

  def tearDown(self):
    '''
    tearDown method that cleans up after each test has run
    '''
    User.users = []

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name,"John")
    self.assertEqual(self.new_user.last_name,"Nyamweya")
    self.assertEqual(self.new_user.user_name,"nyamzy")
    self.assertEqual(self.new_user.email,"johnnyamweya@gmail.com")
    self.assertEqual(self.new_user.password,"hello123")

  def test_save_user(self):
    '''
    test case to test if the user object is saved in the users list
    '''

    self.new_user.save_user() #Save user method
    self.assertEqual(len(User.users),1)

  def test_save_multiple_users(self):
    '''
    test case to check if we can save multiple users
    '''
    self.new_user.save_user()
    test_user = User("Test", "Two", "testy", "testy@gmail.com", "testing123")
    test_user.save_user()

    self.assertEqual(len(User.users),2)

  def test_delete_user(self):
    '''
    test case to check if we can delete a user
    '''
    self.new_user.save_user()
    test_user = User("Test", "Two", "testy", "testy@gmail.com", "testing123")
    test_user.save_user()

    self.new_user.delete_user() #Delete user method
    self.assertEqual(len(User.users),1)

  def test_find_by_username(self):
    '''
    test case to test if we can find a user by username
    '''
    self.new_user.save_user()
    test_user = User("Test", "Two", "testy", "testy@gmail.com", "testing123")
    test_user.save_user()

    found_user = User.find_by_username("testy")
    self.assertEqual(found_user.email, test_user.email)

  def test_display_users(self):
    '''
    test case that tests if we can display all users
    '''
    self.assertEqual(User.display_users(),User.users)

  def test_user_exists(self):
    '''
    test case that returns a Boolean if we cannot find a user
    '''
    self.new_user.save_user()
    test_user = User("Test", "Two", "testy", "testy@gmail.com", "testing123")
    test_user.save_user()

    user_exists = User.user_exist("testy")
    self.assertTrue(user_exists)



if __name__ == '__main__':
  unittest.main()




class TestCredentials(unittest.TestCase):
  '''
  Subclass for testing the cases for the credentials class behaviours
  '''
  def setUp(self):
    '''
    Set up method that runs before each test case
    '''
    self.new_credential = Credentials("nyamzy", "facebook", "hello123") #create new credential object

  def tearDown(self):
    '''
    tearDown method that cleans up after each test has run
    '''
    Credentials.accounts = []

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_credential.user_name,"nyamzy")
    self.assertEqual(self.new_credential.application,"facebook")
    self.assertEqual(self.new_credential.password,"hello123")

  def test_save_credential(self):
    '''
    test case to test if the credential object is saved in the accounts list
    '''

    self.new_credential.save_credential() #Save credentials method
    self.assertEqual(len(Credentials.accounts),1)

  def test_save_multiple_credentials(self):
    '''
    test case to check if we can save multiple credentials
    '''
    self.new_credential.save_credential()
    test_credential = Credentials("testy", "instagram", "testing123")
    test_credential.save_credential()

    self.assertEqual(len(Credentials.accounts),2)

  def test_delete_credential(self):
    '''
    test case to check if we can delete a credential account
    '''
    self.new_credential.save_credential()
    test_credential = Credentials("testy", "instagram", "testing123")
    test_credential.save_credential()

    self.new_credential.delete_credential() #Delete credential method
    self.assertEqual(len(Credentials.accounts),1)

  def test_display_credentials(self):
    '''
    test case that tests if we can display all credentials accounts
    '''
    self.assertEqual(Credentials.display_credentials(),Credentials.accounts)

  def test_credential_exists(self):
    '''
    test case that returns a Boolean if we cannot find a credential
    '''
    self.new_credential.save_credential()
    test_credential = Credentials("testy", "testy@gmail.com", "testing123")
    test_credential.save_credential()

    credential_exists = Credentials.credential_exist("testy")
    self.assertTrue(credential_exists)

if __name__ == '__main__':
  unittest.main()