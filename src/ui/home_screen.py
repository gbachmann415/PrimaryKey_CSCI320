from kivy.uix.gridlayout import GridLayout
from src.ui import back_button


class HomeScreen(GridLayout):
  """
  The home page for a logged in user
  """
  def __init__(self, **kwargs):
    super(HomeScreen, self).__init__(**kwargs)
    self.username = None
    self.add_widget(back_button.BackButton())

  def update_user(self, username):
    """
    Updates the user id of the currently logged in user
    :param username: the user id to update to
    """
    self.username = username

  def go_to_collections(self, button):
    self.parent.update_child('CollectionsScreen', self.username)

  def go_to_following(self, button):
    return

  def search_movies(self, button):
    self.parent.update_child('SearchScreen', self.username)
