from kivy.uix.gridlayout import GridLayout
from src.ui import back_button


class HomeScreen(GridLayout):
  """
  The home page for a logged in user
  """
  def __init__(self, **kwargs):
    super(HomeScreen, self).__init__(**kwargs)
    self.userid = None
    self.add_widget(back_button.BackButton())

  def update_user(self, user_id):
    """
    Updates the user id of the currently logged in user
    :param user_id: the user id to update to
    """
    self.userid = user_id

  def go_to_collections(self, button):
    self.parent.update_child('CollectionsScreen', self.userid)

  def go_to_following(self, button):
    return

  def search_movies(self, button):
    return
