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
    self.sort_type = None
    self.sort_by = None

  def initialize_widget(self, username):
    """
    Initializes the widget by setting class variables and creating the necessary sub-widgets
    :param username: the username of the logged in user
    """
    self.username = username
    search_dropdown = DropDown()
    sort_dropdown = DropDown()
    search_by_list = ['Movie Name', 'Release Date', 'Cast Members', 'Studio', 'Genre']
    sort_by_list = ['Default', 'Movie Name', 'Studio', 'Genre', 'Released Year']
    for element in search_by_list:
      btn = Button(text=element, size_hint_y=None, height='32dp')
      btn.bind(on_release=lambda button: search_dropdown.select(button.text))
      search_dropdown.add_widget(btn)
    search_by = Button(text='Select Search Type', size_hint_y=None, height='32dp')
    search_by.bind(on_release=search_dropdown.open)
    self.search_by = search_by
    search_dropdown.bind(on_select=self.set_search_type)
    self.add_widget(search_by, 2)
    for element in sort_by_list:
      btn = Button(text=element, size_hint_y=None, height='32dp')
      btn.bind(on_release=lambda button: sort_dropdown.select(button.text))
      sort_dropdown.add_widget(btn)
    sort_by = Button(text='Select Sort Type', size_hint_y=None, height='32dp')
    sort_by.bind(on_release=sort_dropdown.open)
    self.sort_by = sort_by
    sort_dropdown.bind(on_select=self.set_sort_type)
    self.add_widget(sort_by, 2)
    self.add_widget(back_button.BackButton())

  def set_search_type(self, instance, value):
    """
    Updates the search type for the search
    :param instance: the button selected
    :param value: the value of the button selected
    """
    setattr(self.search_by, 'text', f'Search By: {value}')
    self.search_type = value

  def set_sort_type(self, instance, value):
    """
    Updates the search type for the search
    :param instance: the button selected
    :param value: the value of the button selected
    """
    setattr(self.sort_by, 'text', f'Sort By: {value}')
    self.sort_type = value

  def search(self, button):
    """
    Completes the search based on the type and navigates the user to the results page
    :param button: the button selected
    """
    if self.search_type is None or self.sort_by is None:
      return

    movie_list = []
    if self.search_type == 'Movie Name':
      movie_list = movies.search_by_name(self.search_word, self.sort_type)
    if self.search_type == 'Release Date':
      movie_list = movies.search_by_release_date(self.search_word, self.sort_type)
    if self.search_type == 'Cast Members':
      movie_list = movies.search_by_cast(self.search_word, self.sort_type)
    if self.search_type == 'Studio':
      movie_list = movies.search_by_studio(self.search_word, self.sort_type)
    if self.search_type == 'Genre':
      movie_list = movies.search_by_genre(self.search_word, self.sort_type)

    self.parent.update_child('MoviesScreen', movie_list=movie_list)
