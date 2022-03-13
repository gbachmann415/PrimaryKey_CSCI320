from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from src.ui import back_button
from src import user


class FollowingScreen(GridLayout):
  """
  The user following screen
  """
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.username = None
    self.following_list = []

  def initialize_widget(self, username):
    """
    Initializes the widget byt setting class variables and populating the following list
    :param username: the username of the logged in user
    """
    self.username = username
    self.add_widget(back_button.BackButton())
    self.get_users_following()

  def get_users_following(self):
    """
    Gets a list of the users the logged in user is following
    """
    self.following_list = user.get_user_following(self.username)
    for following in self.following_list:
      grid_layout = GridLayout(cols=1, rows=2)
      unfollow_button = Button(text=f'Unfollow User', ids={'username': following.get('username')},
                               size_hint_y=None, height='32dp')
      unfollow_button.bind(on_press=self.unfollow_user)
      user_label = Label(text=f'{following.get("username")}\n{following.get("first_name")} {following.get("last_name")}')
      grid_layout.add_widget(user_label)
      grid_layout.add_widget(unfollow_button)
      self.children[-1].add_widget(grid_layout)

  def unfollow_user(self, button):
    """
    Unfollows a user and refreshes the component
    :param button: the button pressed
    """
    user.unfollow_user(self.username, button.ids.get('username'))
    self.remove_widget(self.children[-1])
    self.add_widget(BoxLayout(), len(self.children))
    self.get_users_following()

  def search_users(self, button):
    """
    Navigates the user to the SearchUserScreen
    :param button: the button selected
    """
    self.parent.update_child('SearchUsersScreen', self.username)

