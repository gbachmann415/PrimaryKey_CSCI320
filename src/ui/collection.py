from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from src import collections
from src import movies
from src.ui import back_button


class Collection(GridLayout):
  """
  Displays the movies in a single collection element and functionality related to that
  """
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.movies = []
    self.collection_id = None
    self.username = None

  def initialize_widget(self, collection_id, username):
    """
    Initializes the widget by setting class variables and creating the movie widgets
    :param collection_id: the id of the collection being displayed
    :param username: the username of the logged in user
    """
    self.collection_id = collection_id
    self.username = username
    self.get_movies_for_collection()
    self.add_widget(back_button.BackButton())

  def get_movies_for_collection(self):
    """
    Gets a list of movies in the collection and adds widgets for each
    """
    self.movies = collections.get_movies_in_collection(self.collection_id)
    for movie in self.movies:
      grid_layout = GridLayout()
      grid_layout.rows = 2
      grid_layout.cols = 1
      delete_button = Button(text=f'Delete {movie.get("title")}', ids={'movie_id': movie.get('movie_id')},
                             size_hint_y=None, height='32dp')
      delete_button.bind(on_press=self.delete_movie_from_collection)
      movie_button = Button(text=movie.get('title'), ids={'movie_id': movie.get('movie_id')})
      movie_button.bind(on_press=self.go_to_movie)
      grid_layout.add_widget(movie_button)
      grid_layout.add_widget(delete_button)
      self.children[-1].add_widget(grid_layout)

  def update_collection_name(self, button):
    """
    Updates the name of the collection
    :param button: the button clicked
    """
    collections.update_collection_name(self.collection_id, self.newcollectionname.text)
    self.newcollectionname.text = ''

  def delete_collection(self, button):
    """
    Deletes the collection and re-routes the user to the collections screen
    :param button: the button clicked
    """
    collections.delete_collection(self.collection_id)
    self.parent.update_child('CollectionsScreen')

  def delete_movie_from_collection(self, button):
    """
    Removes a movie from the collection and re-freshes the movies in the collection
    :param button: the button clicked
    """
    movie_id = button.ids.get('movie_id')
    collections.delete_movie_from_collection(self.collection_id, movie_id)
    self.remove_widget(self.children[-1])
    self.add_widget(BoxLayout(), len(self.children))
    self.get_movies_for_collection()

  def watch_collection(self, button):
    """
    Marks all the movies in the collection as watched
    :param button: the button clicked
    """
    for movie in self.movies:
      movies.watch_movie(movie.get('movie_id'), self.username)

  def go_to_movie(self, button):
    self.parent.update_child('Movie', movie_id=button.ids.get('movie_id'))

  def switch_to_search(self, button):
    """
    Switches the view to the search page
    :param button: the button clicked
    """
    return
