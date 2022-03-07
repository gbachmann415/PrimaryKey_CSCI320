from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class HomeScreen(GridLayout):
  """
  The home page for a logged in user
  """
  def __init__(self, **kwargs):
    super(HomeScreen, self).__init__(**kwargs)
    self.userid = None

  def update_user(self, user_id):
    """
    Updates the user id of the currently logged in user
    :param user_id: the user id to update to
    """
    self.userid = user_id
    self.add_widget(Label(text=str(self.userid)))
