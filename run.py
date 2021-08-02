#!/usr/bin/env python3
from password_manager import User, Credentials

def create_user(fname, lname, uname, email, password):
  '''
  Function that creates a new user
  '''
  new_user = User(fname, lname, uname, email, password)
  return new_user

def save_users(user):
  '''
  Function that saves a new user
  '''
  user.save_user()

def del_user(user):
  '''
  Function that deletes a user
  '''
  user.delete_contact()

def find_user(username):
  '''
  Function that finds a user by username and returns the user
  '''
  return User.find_by_username(username)

def display_users():
  '''
  Function that returns all the saved users
  '''
  return User.display_users()

def check_existing_users(username):
  '''
  Function that checks if a user is existing and returns a Boolean
  '''
  return User.user_exist(username)



def main():
  print("Hi there. Welcome to your password manager app. Kindly let me know your name.")
  user_name = input()

  print(f"Hi {user_name}! What would you like to do today?")
  print("\n")

  while True:
    print("Use the following numbers: 1 - Create new user account, 2 - Display user accounts, 3 - Find account, 4 - Delete account, 5 - Exit")
    number = input()

    if number == '1':
      print("New User Account Creation")
      print("-"*10)

      print("First name ...")
      f_name = input()

      print("Last name ...")
      l_name = input()

      print("Username ...")
      u_name = input()

      print("Email address ...")
      e_address = input()

      print("Password ...")
      password = input()

      save_users(create_user(f_name, l_name, u_name, e_address, password)) #Create and save new user details
      print("\n")
      print(f"New User {u_name} created")

      print('\n')

    
    elif number == '2':
      if display_users():
        print("User Accounts:")
        print('\n')

        for user in display_users():
          print(f"{user.first_name} {user.last_name} {user.user_name} {user.email}")
          print('\n')
      else:
        print('\n')
        print("Please create an account")

    elif number == '3':
      print("Enter the username you want to search for:")
      search_username = input()

      if check_existing_users(search_username):
        search_user = find_user(search_username)
        print(f"{search_user.first_name} {search_user.last_name}")
        print("-"*10)
        print(f"Username....{search_user.user_name}")
        print(f"Email address....{search_user.email}")
      else:
        print("That user does not exist.")


    elif number == '5':
      print("Bye. Come again soon.")
      break

    else:
      print("Please use the correct number")


if __name__ == '__main__':
  main()

