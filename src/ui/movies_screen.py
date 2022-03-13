from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from src.ui import back_button


class MoviesScreen(GridLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.username = None
    self.movies = None

  def initialize_widget(self, username, movie_list):
    """
    Initializes the widget by filling in class variables and populating the list of movies
    :param username:
    :param movie_list:
    :return:
    """
    self.username = username
    self.movies = movie_list
    for movie in self.movies:
      minute = f'0{movie.get("runtimeMin")}' if movie.get(
        "runtimeMin") < 10 else f'{movie.get("runtimeMin")}'
      button_text = f'Title: {movie.get("title")}\n' + \
                    f'MPAA Rating: {movie.get("mpaa_rating")}\n' + \
                    f'Runtime: {movie.get("runtimeHr")}:{minute}\n' + \
                    f'Release Date: {movie.get("releaseDate")}\n' + \
                    f'Rating: {movie.get("rating")}\n' +\
                    f'Studio: {movie.get("studio")}\n' +\
                    f'Director: {movie.get("director")}\n' +\
                    'Cast Members: '

      for cast_member in movie.get('cast_members'):
        button_text += f'{cast_member}, '

      button_text = button_text[:-2]

      movie_button = Button(text=button_text, ids={'movie_id': movie.get('movie_id')})
      movie_button.bind(on_press=self.go_to_movie)
      self.children[-1].add_widget(movie_button)
    self.add_widget(back_button.BackButton())

  def go_to_movie(self, button):
    """
    Navigates the user to a specific movie
    :param button: the button selected
    """
    self.parent.update_child('Movie', movie_id=button.ids.get('movie_id'))
