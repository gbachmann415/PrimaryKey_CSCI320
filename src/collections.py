"""
CSCI.320 Project: Movie Domain

File: collections.py

Authors: - Milo Berry
         - Gunnar Bachmann
         - Ari Wisenburn
         - Noah Pelletier

Description:
"""


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
    {'title': 'Test Title', 'mpaa_rating': 'PG-13', 'runtimeHr': 2, 'runtimeMin': 4, 'releaseDate': '04-05-2020'},
    {'title': 'Test Title 2', 'mpaa_rating': 'R', 'runtimeHr': 3, 'runtimeMin': 21, 'releaseDate': '04-09-1999'}
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
