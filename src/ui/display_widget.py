from kivy.uix.gridlayout import GridLayout
from src.ui import login, home_screen, account_screen, collections_screen, collection, movie, search_screen


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
    self.username = None

  def update_child(self, child_name, username=None, collection_id=None, movie_id=None):
    """
    Updates the currently viewed page/screen
    :param child_name: the name of the child to switch to
    :param username: the user id of the person logged in
    :param collection_id: the collection id of the relevant collection
    :param movie_id: the movie id of the relevant movie
    """
    self.previous_screens.append(self.child)

    child = None
    if child_name == 'HomeScreen':
      child = home_screen.HomeScreen()
      child.update_user(username)
      self.username = username

    if child_name == 'AccountScreen':
      child = account_screen.AccountScreen()

    if child_name == 'CollectionsScreen':
      child = collections_screen.CollectionsScreen()
      child.initialize_widget(self.username)

    if child_name == 'Collection':
      child = collection.Collection()
      child.initialize_widget(collection_id, self.username)

    if child_name == 'Movie':
      child = movie.Movie()
      child.initialize_widget(self.username, movie_id)

    if child_name == 'SearchScreen':
      child = search_screen.SearchScreen()
      child.initialize_widget(self.username)

    if child_name == 'MoviesScreen':
      child = None

    self.clear_widgets()
    self.child = child
    self.add_widget(self.child)

  def return_to_prev_screen(self):
    """
    Returns the user to the last screen they saw
    """
    self.clear_widgets()
    self.child = self.previous_screens.pop()

    # refresh the user collections in case one has been added or deleted
    if self.child is collections_screen.CollectionsScreen:
      self.child.get_collections_for_user(self.username)

    self.add_widget(self.child)
