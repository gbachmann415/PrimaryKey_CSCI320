from kivy.uix.gridlayout import GridLayout
from src.ui import login, home_screen, account_screen


class Display(GridLayout):
  """
  The parent element to display the different screens
  """
  def __init__(self, **kwargs):
    super(Display, self).__init__(**kwargs)
    self.child = login.Login()
    self.rows = 1
    self.add_widget(self.child)

  def update_child(self, child_name, userid=None):
    """
    Updates the currently viewed page/screen
    :param child_name: the name of the child to switch to
    :param userid: the user id of the person logged in
    """
    child = None
    if child_name == 'HomeScreen':
      child = home_screen.HomeScreen()
      print(userid)
      child.update_user(userid)

    if child_name == 'AccountScreen':
      child = account_screen.AccountScreen()

    self.clear_widgets()
    self.child = child
    self.add_widget(self.child)
