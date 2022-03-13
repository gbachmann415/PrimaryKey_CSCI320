from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from src.ui import back_button
from src import user


class SearchUsersScreen(GridLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.username = None
    self.users_list = []

  def initialize_widget(self, username):
    """
    Initializes the widget by setting the class variables and adding the back button
    :param username: the username of the logged in user
    """
    self.username = username
    self.add_widget(back_button.BackButton())

  def search(self, button):
    """
    Searches for specific user email and populates the results in the widget
    :param button: the button selected
    """
    self.remove_widget(self.children[-2])
    self.add_widget(BoxLayout(), len(self.children) - 1)
    self.users_list = user.search_user(self.search_email.text)
    for user_result in self.users_list:
      grid_layout = GridLayout(cols=1, rows=2)
      follow_button = Button(text=f'Follow User', ids={'username': user_result.get('username')},
                             size_hint_y=None, height='32dp')
      follow_button.bind(on_press=self.follow_user)
      user_label = Label(
        text=f'{user_result.get("username")}\n{user_result.get("first_name")} {user_result.get("last_name")}')
      grid_layout.add_widget(user_label)
      grid_layout.add_widget(follow_button)
      self.children[-2].add_widget(grid_layout)

  def follow_user(self, button):
    user.follow_user(self.username, button.ids.get('username'))
