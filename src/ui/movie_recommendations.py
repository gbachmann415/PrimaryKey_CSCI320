from kivy.uix.gridlayout import GridLayout
from src.ui.back_button import BackButton
from src import movies


class MovieRecommendations(GridLayout):
  """
  Displays the Movie Recommendations Page
  """
  def __init__(self, **kwargs):
    super(MovieRecommendations, self).__init__(**kwargs)
    self.sort_type = None
    self.username = None

  def initialize_widget(self, username):
    self.username = username
    self.add_widget(BackButton())

  def most_popular_90_days(self, button):
    movie_list = movies.top_20_last_90_days()

    self.parent.update_child('MoviesScreen', movie_list=movie_list, simple_display=True)

  def most_popular_friends(self, button):
    movie_list = movies.top_20_among_friends(self.username)

    self.parent.update_child('MoviesScreen', movie_list=movie_list, simple_display=True)

  def new_releases(self, button):
    movie_list = movies.top_5_new_releases()

    self.parent.update_child('MoviesScreen', movie_list=movie_list, simple_display=True)

  def recommend_for_user(self, button):
    movie_list = movies.recommend_for_user(self.username)

    self.parent.update_child('MoviesScreen', movie_list=movie_list, simple_display=True)