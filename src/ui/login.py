from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from src import user


class Login(GridLayout):
  """
  Displays the login page
  """
  def __init__(self, **kwargs):
    super(Login, self).__init__(**kwargs)

  def login_pressed(self, button):
    """
    Tries to log in the user based on tbe textboxes and either switches to home page or displays error message
    :param button: the button pressed
    """
    username = user.login_user(self.username.text, self.userpw.text)
    if username is not None:
      self.parent.update_child('HomeScreen', username)
    else:
      self.add_widget(Label(text='Login Unsuccessful'))

  def create_account(self, button):
    """
    Switches to account creation page if button is pressed
    :param button: the button pressed
    """
    self.parent.update_child('AccountScreen')
