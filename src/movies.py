"""
CSCI.320 Project: Movie Domain

File: movies.py

Authors: - Milo Berry
         - Gunnar Bachmann
         - Ari Wisenburn
         - Noah Pelletier

Description:
"""


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


def search_by_name(movie_name):
  """
  Searches for a movie by name
  :param movie_name: the name to search for
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


def search_by_release_date(release_date):
  """
  Searches for a movie by release data
  :param release_date: the release data to search for
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


def search_by_cast(cast_member):
  """
  Searches for a movie by cast member
  :param cast_member: the cast member name to search for
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


def search_by_studio(studio_name):
  """
  Searches for a movie by studio name
  :param studio_name: the studio name to search for
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


def search_by_genre(genre_name):
  """
  Searches for a movie by genre
  :param genre_name: the name of the genre to search for
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
