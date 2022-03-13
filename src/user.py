"""
CSCI.320 Project: Movie Domain

File: user.py

Authors: - Milo Berry
         - Gunnar Bachmann
         - Ari Wisenburn
         - Noah Pelletier

Description:
"""


def login_user(username, password):
  """
  logs in a user from a given username and password
  :param username: username of the user to login
  :param password: the password
  :return: the username of the logged in user or None if credentials invalid
  """
  return "test_username"


def create_user(username, password, first_name, last_name, email):
  """
  Creates a new user with the given information
  :param username: the username of the new user
  :param password: the password of the new user
  :param first_name: first name of the new user
  :param last_name: last name of the new user
  :param email: email of the new user
  :return: the username of the new user or None if username already taken
  """
  return "test_username"


def get_user_following(username):
  """
  Gets a list of users the user is following
  :param username: the username of user to get a following list for
  :return: a list of user information
  """
  return [
    {'username': 'testusername1', 'first_name': 'First Name', 'last_name': 'Last Name'},
    {'username': 'testusername2', 'first_name': 'First Name 2', 'last_name': 'Last Name 2'},
  ]


def follow_user(username, following_username):
  """
  Follows another user
  :param username: the username of the user that wants to follow another user
  :param following_username: the username of the user that is to be followed
  :return: None
  """
  return


def unfollow_user(username, unfollowing_username):
  """
  Unfollows a user
  :param username: the username of the user that wants to unfollow another user
  :param unfollowing_username: the username of the user that is to be unfollowed
  :return:
  """
  return


def search_user(user_email):
  """
  Searches a user by email
  :param user_email: the user email to search for
  :return: a list of users with matching emails
  """
  return [
    {'username': 'testusername1', 'first_name': 'First Name', 'last_name': 'Last Name'},
    {'username': 'testusername2', 'first_name': 'First Name 2', 'last_name': 'Last Name 2'},
  ]
