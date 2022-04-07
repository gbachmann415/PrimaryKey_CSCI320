from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from src.ui.back_button import BackButton
from src import movies


class TopTenScreen(GridLayout):
  """
  Displays the Top 10 Movies page
  """
  def __init__(self, **kwargs):
    super(TopTenScreen, self).__init__(**kwargs)
    self.sort_type = None
    self.username = None

  def initialize_widget(self, username):
    self.username = username
    sort_dropdown = DropDown()
    sort_by_list = ['Highest Rated', 'Most Watched', 'Combination']
    for element in sort_by_list:
      btn = Button(text=element, size_hint_y=None, height='32dp')
      btn.bind(on_release=lambda button: sort_dropdown.select(button.text))
      sort_dropdown.add_widget(btn)
    sort_by = Button(text='Select Sort Type', size_hint_y=None, height='32dp')
    sort_by.bind(on_release=sort_dropdown.open)
    self.sort_type = sort_by
    sort_dropdown.bind(on_select=self.set_sort_type)
    self.add_widget(sort_by, 2)
    self.add_widget(BackButton())

  def set_sort_type(self, instance, value):
    """
    Updates the sort type
    :param instance: the button selected
    :param value: the value of the button selected
    """
    setattr(self.sort_type, 'text', f'Sort By: {value}')
    self.sort_type = value

  def show_results(self, button):
    """
    Updates the screen to show the results of the sort
    :param button: the button selected
    """
    if self.sort_type is None:
      return

    movie_list = movies.top_ten_movies_for_user(self.username, self.sort_type)

    self.parent.update_child('MoviesScreen', movie_list=movie_list, simple_display=True)
