from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from src.ui import back_button
from src import user, collections


class HomeScreen(GridLayout):
  """
  The home page for a logged in user
  """
  def __init__(self, **kwargs):
    super(HomeScreen, self).__init__(**kwargs)
    self.username = None
    self.following_count = 0
    self.follower_count = 0
    self.number_of_collections = 0
    self.add_widget(back_button.BackButton())

  def update_user(self, username):
    """
    Updates the user id of the currently logged in user
    :param username: the user id to update to
    """
    self.username = username
    self.following_count = user.get_following_count_for_user(self.username)
    self.follower_count = user.get_follower_count_for_user(self.username)
    self.number_of_collections = collections.get_number_of_collections_for_user(self.username)
    user_info_text = f"Following Count: {self.following_count}" \
                     f"\nFollower Count: {self.follower_count}" \
                     f"\nCollections Count: {self.number_of_collections}"
    self.add_widget(Label(text=user_info_text), len(self.children) - 1)

  def go_to_collections(self, button):
    """
    Goes to the collections page for the user
    :param button: the button selected
    """
    self.parent.update_child('CollectionsScreen', self.username)

  def go_to_following(self, button):
    """
    Goes to the user following page for the logged in user
    :param button: the button selected
    """
    self.parent.update_child('FollowingScreen', self.username)

  def search_movies(self, button):
    """
    Goes to the search movies page
    :param button: the button selected
    """
    self.parent.update_child('SearchScreen', self.username)

  def go_to_top_ten_movies(self, button):
    """
    Goes to the top 10 movies page
    :param button: the button selected
    """
    self.parent.update_child('TopTen', self.username)

  def go_to_recommended_movies(self, button):
    """
    Goes to the recommended movies page
    :param button: the button selected
    """
    self.parent.update_child('RecommendedMovies', self.username)
