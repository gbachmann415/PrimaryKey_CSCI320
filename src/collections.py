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
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # SQL
    change_collection_name = r"""UPDATE p320_21.collection SET name = '{}' 
                                 WHERE collection_id = {};""".format(new_name, collection_id)

    # Execute SQL
    curs.execute(change_collection_name)
    conn.commit()

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return


def delete_collection(collection_id):
    """
  Deletes the given collection
  :param collection_id: the id of the collection to delete
  :return: None
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # SQL
    del_movies_from_collection = r"""DELETE FROM p320_21.movies_in_collection 
                                     WHERE collection_id = {};""".format(collection_id)
    del_collection = r"""DELETE FROM p320_21.collection WHERE collection_id = {};""".format(collection_id)

    # Execute SQL
    curs.execute(del_movies_from_collection)
    conn.commit()
    curs.execute(del_collection)
    conn.commit()

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return


def add_collection(username, collection_name):
    """
  Adds a new collection with no movies
  :param username: the username the collection is being created for
  :param collection_name: the name of the collection to add
  :return: None
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # Check if collection name exist
    curs.execute(r"""SELECT * FROM p320_21.collection 
                     WHERE name = '{}' AND username = '{}' LIMIT 1;""".format(collection_name, username))
    if curs.fetchone() is not None:
        curs.close()
        conn.close()
        return

    # Create collection
    create_collection = r"""INSERT INTO p320_21.collection(name, username) 
                            VALUES ('{}', '{}');""".format(collection_name, username)
    curs.execute(create_collection)
    conn.commit()

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return


def delete_movie_from_collection(collection_id, movie_id):
    """
  Deletes a movie from the given collection
  :param collection_id: the id of the collection to remove the movie from
  :param movie_id: the id of the movie to remove
  :return: None
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # SQL
    del_movie_from_collection = r"""DELETE FROM p320_21.movies_in_collection 
                                         WHERE collection_id = {} AND movie_id = {};""".format(collection_id, movie_id)

    # Execute SQL
    curs.execute(del_movie_from_collection)
    conn.commit()

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return


def add_movie_to_collection(username, collection_name, movie_id):
    """
  Adds a movie to a user's collection
  :param username: The username of the currently logged in user
  :param collection_name: The name of the collection to add to
  :param movie_id: The id of the movie to add to the collection
  :return: None
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # Execute SQL
    curs.execute(r"""SELECT collection_id FROM p320_21.collection
                     WHERE name = '{}' AND username = '{}';""".format(collection_name, username))
    collection_id = curs.fetchone()[0]
    try:
        curs.execute(r"""INSERT INTO p320_21.movies_in_collection(collection_id, movie_id)
                         VALUES ({}, {});""".format(collection_id, movie_id))
        conn.commit()
    except:
        # Close the Database Cursor and Connection
        curs.close()
        conn.close()
        return

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return


def test():
    # add_collection('test1', 'testCollection1')
    # add_movie_to_collection('test1', 'testCollection1', 1)
    # add_movie_to_collection('test1', 'testCollection1', 2)
    update_collection_name(1, 'testCollection1.5')
    # delete_movie_from_collection(1, 1)
    # delete_movie_from_collection(1, 2)
    # delete_collection(1)

    return


test()
