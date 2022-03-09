from kivy.uix.gridlayout import GridLayout
from src.ui import login, home_screen, account_screen, collections_screen, collection


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
    self.userid = None

  def update_child(self, child_name, userid=None, collection_id=None):
    """
    Updates the currently viewed page/screen
    :param child_name: the name of the child to switch to
    :param userid: the user id of the person logged in
    :param collection_id: the collection id of the relevant collection
    """
    self.previous_screens.append(self.child)

    child = None
    if child_name == 'HomeScreen':
      child = home_screen.HomeScreen()
      child.update_user(userid)
      self.userid = userid

    if child_name == 'AccountScreen':
      child = account_screen.AccountScreen()

    if child_name == 'CollectionsScreen':
      child = collections_screen.CollectionsScreen()
      child.initialize_widget(self.userid)

    if child_name == 'Collection':
      child = collection.Collection()
      child.initialize_widget(collection_id, self.userid)

    if child_name == 'Movie':
      return

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
      self.child.get_collections_for_user(self.userid)

    self.add_widget(self.child)
