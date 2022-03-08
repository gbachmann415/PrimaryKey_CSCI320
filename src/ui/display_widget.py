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
    self.previous_screens = []
    self.add_widget(self.child)

  def update_child(self, child_name, userid=None):
    """
    Updates the currently viewed page/screen
    :param child_name: the name of the child to switch to
    :param userid: the user id of the person logged in
    """
    self.previous_screens.append(self.child)

    child = None
    if child_name == 'HomeScreen':
      child = home_screen.HomeScreen()
      child.update_user(userid)

    if child_name == 'AccountScreen':
      child = account_screen.AccountScreen()

    self.clear_widgets()
    self.child = child
    self.add_widget(self.child)

  def return_to_prev_screen(self):
    """
    Returns the user to the last screen they saw
    """
    self.clear_widgets()
    self.child = self.previous_screens.pop()
    self.add_widget(self.child)
