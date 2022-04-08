from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from src.ui import \
  login, home_screen, \
  account_screen, collections_screen, \
  collection, movie, \
  search_screen, movies_screen, \
  following_screen, search_users_screen, \
  top_ten_screen


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

  def update_child(self, child_name, username=None, collection_id=None, movie_id=None, movie_list=None, simple_display=False):
    """
    Updates the currently viewed page/screen
    :param child_name: the name of the child to switch to
    :param username: the user id of the person logged in
    :param collection_id: the collection id of the relevant collection
    :param movie_id: the movie id of the relevant movie
    :param movie_list: a list of movies returned from the search result
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
      child = movies_screen.MoviesScreen()
      child.initialize_widget(self.username, movie_list, simple_display)

    if child_name == 'FollowingScreen':
      child = following_screen.FollowingScreen()
      child.initialize_widget(self.username)

    if child_name == 'SearchUsersScreen':
      child = search_users_screen.SearchUsersScreen()
      child.initialize_widget(self.username)

    if child_name == 'TopTen':
      child = top_ten_screen.TopTenScreen()
      child.initialize_widget(self.username)

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
    if type(self.child) is collections_screen.CollectionsScreen:
      self.child.remove_widget(self.child.children[-1])
      self.child.add_widget(BoxLayout(), len(self.child.children))
      self.child.get_collections_for_user()

    # refresh the movies in collection in case one has been added or deleted
    if type(self.child) is collection.Collection:
      self.child.remove_widget(self.child.children[-1])
      self.child.add_widget(BoxLayout(), len(self.child.children))
      self.child.get_movies_for_collection()

    # refresh the user's following list in case user was followed or unfollowed
    if type(self.child) is following_screen.FollowingScreen:
      self.child.remove_widget(self.child.children[-1])
      self.child.add_widget(BoxLayout(), len(self.child.children))
      self.child.get_users_following()

    self.add_widget(self.child)
