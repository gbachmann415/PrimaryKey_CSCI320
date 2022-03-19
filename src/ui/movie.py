from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from src.ui import back_button
from src import movies, collections


class Movie(GridLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.username = None
    self.movie_id = None
    self.movie = None
    self.collections = None

  def initialize_widget(self, username, movie_id):
    """
    Initializes the widget by setting class variables and populating the movie information
    :param username: the username of the logged in user
    :param movie_id: the id of the movie being viewed
    """
    self.movie_id = movie_id
    self.username = username
    self.get_collections_info()
    rating_dropdown = DropDown()
    collections_dropdown = DropDown()

    for index in range(1, 6):
      btn = Button(text=f'{index} {"Star" if index == 1 else "Stars"}', size_hint_y=None, height='32dp')
      btn.bind(on_release=lambda button: rating_dropdown.select(button.text))
      rating_dropdown.add_widget(btn)
    rating_dropdown.bind(on_select=self.rate_movie)
    rating_button = Button(text='Rate Movie', size_hint_y=None, height='32dp')
    rating_button.bind(on_release=rating_dropdown.open)

    for collection in self.collections:
      btn = Button(text=f'{collection.get("name")}', ids={'collection_id': collection.get("collection_id")}, size_hint_y=None, height='32dp')
      btn.bind(on_release=lambda button: collections_dropdown.select(button.text))
      collections_dropdown.add_widget(btn)
    collections_dropdown.bind(on_select=self.add_movie_to_collection)
    collections_button = Button(text='Add Movie To Collection', size_hint_y=None, height='32dp')
    collections_button.bind(on_release=collections_dropdown.open)

    self.add_widget(rating_button)
    self.add_widget(collections_button)
    self.add_widget(back_button.BackButton())
    self.get_movie_info()

  def get_collections_info(self):
    """
    Gets the collections for the logged in user
    """
    self.collections = collections.get_collections_for_user(self.username)

  def get_movie_info(self):
    """
    Gets movie information for the user and populates the data in the widget
    """
    self.movie = movies.get_movie(self.movie_id, self.username)
    minute = f'0{self.movie.get("runtimeMin")}' if self.movie.get(
      "runtimeMin") < 10 else f'{self.movie.get("runtimeMin")}'
    last_watched = "N/A" if self.movie.get("lastWatched") is None else self.movie.get("lastWatched")
    rating = "N/A" if self.movie.get("rating") is None else self.movie.get("rating")
    self.remove_widget(self.children[-1])
    self.add_widget(Label(text=
                          f'Title: {self.movie.get("title")}\n' +
                          f'MPAA Rating: {self.movie.get("mpaa_rating")}\n' +
                          f'Runtime: {self.movie.get("runtimeHr")}:{minute}\n' +
                          f'Release Date: {self.movie.get("releaseDate")}\n' +
                          f'Last Watched: {last_watched}\n' +
                          f'Rating: {rating}\n',
                          size_hint_y=None,
                          height='200dp'
                          ),
                    len(self.children))

  def rate_movie(self, dropdown, value):
    """
    Rates a movie the value selected in the dropdown
    :param dropdown: the dropdown object
    :param value: the value selected
    """
    movies.rate_movie(self.movie_id, self.username, int(value[0]))
    self.get_movie_info()

  def watch_movie(self, button):
    """
    Marks a movie as watched by a user
    :param button: the button selected
    """
    movies.watch_movie(self.movie_id, self.username)
    self.get_movie_info()

  def add_movie_to_collection(self, dropdown, value):
    """
    Adds given movie to collection
    :param dropdown: the dropdown selected
    :param value: the value of the dropdown selected
    """
    collections.add_movie_to_collection(self.username, value, self.movie_id)
