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
  return {
    'title': 'Test Title',
    'mpaa_rating': 'PG-13',
    'runtimeHr': 2,
    'runtimeMin': 4,
    'releaseDate': '04-05-2020',
    'lastWatched': '04-05-2020',
    'rating': 3
  }


def rate_movie(movie_id, username, rating):
  print(rating)
  return {
    'title': 'Test Title',
    'mpaa_rating': 'PG-13',
    'runtimeHr': 2,
    'runtimeMin': 4,
    'releaseDate': '04-05-2020',
    'lastWatched': '04-05-2020',
    'rating': 3
  }


