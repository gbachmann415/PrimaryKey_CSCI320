from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from src import user
from src.ui import back_button


class AccountScreen(GridLayout):
  """
  The Create Account Page
  """
  def __init__(self, **kwargs):
    super(AccountScreen, self).__init__(**kwargs)
    self.add_widget(back_button.BackButton())
    self.has_error = False

  def create_account(self, button):
    """
    Creates a new user account on button click
    :param button: the button clicked
    """
    username = user.create_user(
      self.username.text,
      self.userpw.text,
      self.firstname.text,
      self.lastname.text,
      self.email.text
    )
    if username is not None:
      self.parent.update_child('HomeScreen', username)
    else:
      if not self.has_error:
        self.add_widget(Label(text='Username is already taken', size_hint_y=None, height='32dp'), 2)
        self.has_error = True
