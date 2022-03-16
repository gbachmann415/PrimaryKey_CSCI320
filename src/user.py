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
from config import DB_USERNAME, DB_PASSWORD, DB_NAME
import psycopg2
from sshtunnel import SSHTunnelForwarder


def connect_to_db():
    """
    Establish a connection to the database with username, password, and database name.
    Failed connection will result in a connection failed output to the user and program exit.

    :return: conn = connection to database
    """
    try:
        server = SSHTunnelForwarder(('starbug.cs.rit.edu', 22),
                                    ssh_username=DB_USERNAME,
                                    ssh_password=DB_PASSWORD,
                                    remote_bind_address=('localhost', 5432))
        server.start()
        # print("SSH tunnel established")
        params = {
            'database': DB_NAME,
            'user': DB_USERNAME,
            'password': DB_PASSWORD,
            'host': 'localhost',
            'port': server.local_bind_port
        }

        conn = psycopg2.connect(**params)
        # print("Database connection established")
    except:
        print("Connection failed")
        exit()

    return conn


def login_user(username, password):
    """
  logs in a user from a given username and password
  :param username: username of the user to login
  :param password: the password
  :return: the username of the logged in user or None if credentials invalid
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()


    # Save timestamp for last_access_date
    current_date = datetime.today().strftime('%Y-%m-%d')
    last_access_date = current_date

    # SQL statement to log in the user (check if creds valid)
    is_valid_login = r"""SELECT * FROM p320_21."user" 
                         WHERE username = '{}'
                         AND password = '{}' LIMIT 1;""".format(username, password)

    # Validate user login
    curs.execute(is_valid_login)
    if curs.fetchone() is None:
        return None

    # SQL statement to update the last_access_date value in the user table for the given user
    update_access_timestamp = r"""UPDATE p320_21."user" 
                                      SET last_access_date = '{}' 
                                      WHERE username = '{}';""".format(last_access_date, username)


    # Update last_access_date timestamp in user table (for user that is logging in)
    curs.execute(update_access_timestamp)
    conn.commit()

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return username


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
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # Get current datetime for creation_date and last_access_date
    current_date = datetime.today().strftime('%Y-%m-%d')

    # Create/store name_id, creation_date, and last_access_date values
    creation_date = current_date
    last_access_date = current_date

    # Defining SQL statements for validating username and inserting into name table
    is_valid_username = r"""SELECT * FROM p320_21."user" WHERE username = '{}' LIMIT 1;""".format(username)
    insert_name = r"""INSERT INTO p320_21.name(first_name, last_name) 
                      VALUES ('{}', '{}') RETURNING id;""".format(first_name, last_name)

    # Checking if desired username is valid
    curs.execute(is_valid_username)
    if curs.fetchone() is not None:
        # Close the Database Cursor and Connection
        curs.close()
        conn.close()
        return None

    # Inserting new name into the name table
    curs.execute(insert_name)
    conn.commit()

    # Saving the name_id value to use when inserting new user into user table
    name_id = curs.fetchone()[0]

    insert_user = r"""INSERT INTO p320_21."user" (username, name_id, creation_date, password, email, last_access_date)
                      VALUES ('{}', {}, '{}', '{}', '{}', '{}');""".format(username, name_id, creation_date,
                                                                             password, email, last_access_date)
    curs.execute(insert_user)
    conn.commit()

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return username


def get_user_following(username):
    """
  Gets a list of users the user is following
  :param username: the username of user to get a following list for
  :return: a list of user information
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # SQL statement to select the users the given username is following
    sql = r"SELECT following_username FROM p320_21.following WHERE username = '{}';".format(username)

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

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
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # SQL statement to insert a new following_username for the given username (following a user)
    sql = r"INSERT INTO p320_21.following (username, following_username) " \
          r"VALUES ('{}', '{}');".format(username, following_username)

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return


def unfollow_user(username, unfollowing_username):
    """
  Unfollows a user
  :param username: the username of the user that wants to unfollow another user
  :param unfollowing_username: the username of the user that is to be unfollowed
  :return:
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # SQL statement to delete the row in following table where the user is following the unfollowing_username
    sql = r"DELETE FROM p320_21.following " \
          r"WHERE username = '{}' AND following_username = '{}';".format(username, unfollowing_username)

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return


def search_user(user_email):
    """
  Searches a user by email
  :param user_email: the user email to search for
  :return: a list of users with matching emails
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # TODO would this just return a single user, or are people able to search for multiple at once?

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return [
        {'username': 'testusername1', 'first_name': 'First Name', 'last_name': 'Last Name'},
        {'username': 'testusername2', 'first_name': 'First Name 2', 'last_name': 'Last Name 2'},
    ]

# print(create_user('test', 'testpw', 'Gunnar', 'Bachmann', 'test@gmail.com'))
# print(login_user('test', 'testpw1'))