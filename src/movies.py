"""
CSCI.320 Project: Movie Domain

File: movies.py

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


def get_movie(movie_id, username):
  """
  Gets the data for a specific movie INCLUDING the users latest watched date and current rating
  :param movie_id: the movie id to get data for
  :param username: the username of the logged in user
  """
  return {
    'title': 'Test Title',
    'mpaa_rating': 'PG-13',
    'runtimeHr': 2,
    'runtimeMin': 4,
    'releaseDate': '04-05-2020',
    'lastWatched': None,
    'rating': None
  }


def watch_movie(movie_id, username):
  """
  Marks a movie as watched by the given user
  :param movie_id: the id of the movie watched
  :param username: the username of the user that has watched the movie
  :return: None
  """
  return


def rate_movie(movie_id, username, rating):
  """
  Rates a movie from a specified user
  :param movie_id: the id of the movie to be rated
  :param username: the username of the user rating the film
  :param rating: the rating the user is giving the film
  :return: None
  """
  return

# sort_by_list = ['Default', 'Movie Name', 'Studio', 'Genre', 'Released Year']

def search_by_name(movie_name, sort_type):
  """
  Searches for a movie by name
  :param movie_name: the name to search for
  :param sort_type: the sort type for the search
  :return: A list of movies that have titles matching the search name
  """
  return [
    {
      'movie_id': 1,
      'title': 'Test Title',
      'cast_members': ['Cast Name 2', 'Cast Name 4'],
      'director': 'director name 1',
      'studio': 'studio name',
      'mpaa_rating': 'PG-13',
      'runtimeHr': 2,
      'runtimeMin': 4,
      'rating': 4.5
    },
    {
      'movie_id': 2,
      'title': 'Test Title 2',
      'cast_members': ['Cast Name 2', 'Cast Name 1'],
      'director': 'director name 2',
      'studio': 'studio name 2',
      'mpaa_rating': 'R',
      'runtimeHr': 3,
      'runtimeMin': 10,
      'rating': 3.1
    }
  ]


def search_by_release_date(release_date, sort_type):
  """
  Searches for a movie by release data
  :param release_date: the release data to search for
  :param sort_type: the sort type for the search
  :return: A list of movies that have release dates matching the search date
  """
  return [
    {
      'movie_id': 1,
      'title': 'Test Title',
      'cast_members': ['Cast Name 2', 'Cast Name 4'],
      'director': 'director name 1',
      'studio': 'studio name',
      'mpaa_rating': 'PG-13',
      'runtimeHr': 2,
      'runtimeMin': 4,
      'rating': 4.5
    },
    {
      'movie_id': 2,
      'title': 'Test Title 2',
      'cast_members': ['Cast Name 2', 'Cast Name 1'],
      'director': 'director name 2',
      'studio': 'studio name 2',
      'mpaa_rating': 'R',
      'runtimeHr': 3,
      'runtimeMin': 10,
      'rating': 3.1
    }
  ]


def search_by_cast(cast_member, sort_type):
  """
  Searches for a movie by cast member
  :param cast_member: the cast member name to search for
  :param sort_type: the sort type for the search
  :return: A list of movies that have cast members matching the search name
  """
  return [
    {
      'movie_id': 1,
      'title': 'Test Title',
      'cast_members': ['Cast Name 2', 'Cast Name 4'],
      'director': 'director name 1',
      'studio': 'studio name',
      'mpaa_rating': 'PG-13',
      'runtimeHr': 2,
      'runtimeMin': 4,
      'rating': 4.5
    },
    {
      'movie_id': 2,
      'title': 'Test Title 2',
      'cast_members': ['Cast Name 2', 'Cast Name 1'],
      'director': 'director name 2',
      'studio': 'studio name 2',
      'mpaa_rating': 'R',
      'runtimeHr': 3,
      'runtimeMin': 10,
      'rating': 3.1
    }
  ]


def search_by_studio(studio_name, sort_type):
  """
  Searches for a movie by studio name
  :param studio_name: the studio name to search for
  :param sort_type: the sort type for the search
  :return: A list of movies that have studios matching the search name
"""
  return [
    {
      'movie_id': 1,
      'title': 'Test Title',
      'cast_members': ['Cast Name 2', 'Cast Name 4'],
      'director': 'director name 1',
      'studio': 'studio name',
      'mpaa_rating': 'PG-13',
      'runtimeHr': 2,
      'runtimeMin': 4,
      'rating': 4.5
    },
    {
      'movie_id': 2,
      'title': 'Test Title 2',
      'cast_members': ['Cast Name 2', 'Cast Name 1'],
      'director': 'director name 2',
      'studio': 'studio name 2',
      'mpaa_rating': 'R',
      'runtimeHr': 3,
      'runtimeMin': 10,
      'rating': 3.1
    }
  ]


def search_by_genre(genre_name, sort_type):
  """
  Searches for a movie by genre
  :param genre_name: the name of the genre to search for
  :param sort_type: the sort type for the search
  :return: A list of movies that have genre matching the search genre
  """
  return [
    {
      'movie_id': 1,
      'title': 'Test Title',
      'cast_members': ['Cast Name 2', 'Cast Name 4'],
      'director': 'director name 1',
      'studio': 'studio name',
      'mpaa_rating': 'PG-13',
      'runtimeHr': 2,
      'runtimeMin': 4,
      'rating': 4.5
    },
    {
      'movie_id': 2,
      'title': 'Test Title 2',
      'cast_members': ['Cast Name 2', 'Cast Name 1'],
      'director': 'director name 2',
      'studio': 'studio name 2',
      'mpaa_rating': 'R',
      'runtimeHr': 3,
      'runtimeMin': 10,
      'rating': 3.1
    }
  ]
