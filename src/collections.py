"""
CSCI.320 Project: Movie Domain

File: collections.py

Authors: - Milo Berry
         - Gunnar Bachmann
         - Ari Wisenburn
         - Noah Pelletier

Description:
"""

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


def get_collections_for_user(username):
  """
  Gets a list of collections for given user
  :param username: the username of the user to get collections for
  """
  return [
    {'collection_id': 1, 'name': 'Test Name', 'numMovies': 2, 'lengthHr': 3, 'lengthMin': 48},
    {'collection_id': 2, 'name': 'Test Name 2', 'numMovies': 8, 'lengthHr': 18, 'lengthMin': 5}
  ]


def get_movies_in_collection(collection_id):
  """
  Gets a list of movies in a given collection
  :param collection_id: the collection id of the collection to get movies for
  """
  return [
    {'movie_id': 1, 'title': 'Test Title'},
    {'movie_id': 2, 'title': 'Test Title 2'}
  ]


def update_collection_name(collection_id, new_name):
  """
  Updates the name of the collection
  :param collection_id: the id of the collection to update
  :param new_name: the new name of the collection
  :return: None
  """
  return


def delete_collection(collection_id):
  """
  Deletes the given collection
  :param collection_id: the id of the collection to delete
  :return: None
  """
  return


def add_collection(collection_name):
  """
  Adds a new collection with no movies
  :param collection_name: the name of the collection to add
  :return: None
  """
  return


def delete_movie_from_collection(collection_id, movie_id):
  """
  Deletes a movie from the given collection
  :param collection_id: the id of the collection to remove the movie from
  :param movie_id: the id of the movie to remove
  :return: None
  """
  return


def add_movie_to_collection(username, collection_name, movie_id):
  """
  Adds a movie to a user's collection
  :param username: The username of the currently logged in user
  :param collection_name: The name of the collection to add to
  :param movie_id: The id of the movie to add to the collection
  :return: None
  """
  return