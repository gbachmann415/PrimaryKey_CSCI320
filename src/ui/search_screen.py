from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from src import movies
from src.ui import back_button


class SearchScreen(GridLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.username = None
    self.search_type = None
    self.search_by = None

  def initialize_widget(self, username):
    """
    Initializes the widget by setting class variables and creating the necessary sub-widgets
    :param username: the username of the logged in user
    """
    self.username = username
    dropdown = DropDown()
    search_by_list = ['Movie Name', 'Release Date', 'Cast Members', 'Studio', 'Genre']
    for element in search_by_list:
      btn = Button(text=element, size_hint_y=None, height='32dp')
      btn.bind(on_release=lambda button: dropdown.select(button.text))
      dropdown.add_widget(btn)
    search_by = Button(text='Select Search Type', size_hint_y=None, height='32dp')
    search_by.bind(on_release=dropdown.open)
    self.search_by = search_by
    dropdown.bind(on_select=self.set_search_type)
    self.add_widget(search_by, 2)
    self.add_widget(back_button.BackButton())

  def set_search_type(self, instance, value):
    """
    Updates the search type for the search
    :param instance: the button selected
    :param value: the value of the button selected
    """
    setattr(self.search_by, 'text', f'Search By: {value}')
    self.search_type = value

  def search(self, button):
    """
    Completes the search based on the type and navigates the user to the results page
    :param button: the button selected
    """
    if self.search_type is None:
      return

    movie_list = []
    if self.search_type == 'Movie Name':
      movie_list = movies.search_by_name(self.search_word)
    if self.search_type == 'Release Date':
      movie_list = movies.search_by_release_date(self.search_word)
    if self.search_type == 'Cast Members':
      movie_list = movies.search_by_cast(self.search_word)
    if self.search_type == 'Studio':
      movie_list = movies.search_by_studio(self.search_word)
    if self.search_type == 'Genre':
      movie_list = movies.search_by_genre(self.search_word)

    self.parent.update_child('MoviesScreen', movie_list=movie_list)