"""
CSCI.320 Project: Movie Domain

File: user.py

Authors: - Milo Berry
         - Gunnar Bachmann
         - Ari Wisenburn
         - Noah Pelletier

Description:
"""

from datetime import datetime

#TODO Probably will need to add the DB connection as a parameter for the functions in order to run the sql statements

def login_user(username, password):
    """
  logs in a user from a given username and password
  :param username: username of the user to login
  :param password: the password
  :return: the username of the logged in user or None if credentials invalid
  """
    current_date = datetime.today().strftime('%Y-%m-%d')
    last_access_date = current_date

    # SQL statement to update the last_access_date value in the user table for the given user (ONLY IF LOGIN IS VALID)
    sql_update_access_timestamp = r"UPDATE p320_21.user SET last_access_date = '{}' " \
                                  r"WHERE username = '{}';".format(last_access_date, username)
    # SQL statement to log in the user (check if creds valid)
    sql = r"" #TODO

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
    # Get current datetime for creation_date and last_access_date
    current_date = datetime.today().strftime('%Y-%m-%d')
    # Create/store name_id, creation_date, and last_access_date values
    name_id = 123  # TODO How do we want to organize the name_id's? Could just be a count (ex: first user is 1 and so on)
    creation_date = current_date
    last_access_date = current_date
    # SQL statement to add a new user to the user table in the database
    sql = r"INSERT INTO p320_21.user (username, name_id, creation_date, password, email, last_access_date) " \
          r"VALUES ('{}', {}, '{}', '{}', '{}', '{}');".format(username, name_id, creation_date,
                                                               password, email, last_access_date)

    #TODO Return the username if valid, or return None and maybe some output if invalid
    return "test_username"


def get_user_following(username):
    """
  Gets a list of users the user is following
  :param username: the username of user to get a following list for
  :return: a list of user information
  """
    # SQL statement to select the users the given username is following
    sql = r"SELECT following_username FROM p320_21.following WHERE username = '{}';".format(username)

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
    # SQL statement to insert a new following_username for the given username (following a user)
    sql = r"INSERT INTO p320_21.following (username, following_username) " \
          r"VALUES ('{}', '{}');".format(username, following_username)

    return


def unfollow_user(username, unfollowing_username):
    """
  Unfollows a user
  :param username: the username of the user that wants to unfollow another user
  :param unfollowing_username: the username of the user that is to be unfollowed
  :return:
  """
    # SQL statement to delete the row in following table where the user is following the unfollowing_username
    sql = r"DELETE FROM p320_21.following " \
          r"WHERE username = '{}' AND following_username = '{}';".format(username, unfollowing_username)

    return


def search_user(user_email):
    """
  Searches a user by email
  :param user_email: the user email to search for
  :return: a list of users with matching emails
  """
    # TODO would this just return a single user, or are people able to search for multiple at once?
    return [
        {'username': 'testusername1', 'first_name': 'First Name', 'last_name': 'Last Name'},
        {'username': 'testusername2', 'first_name': 'First Name 2', 'last_name': 'Last Name 2'},
    ]
