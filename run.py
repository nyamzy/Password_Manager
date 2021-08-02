#!/usr/bin/env python3
from password_manager import User

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

def del_contact(user):
  '''
  Function that deletes a user
  '''
  user.delete_contact()


