from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from src import collections
from src.ui import back_button


class CollectionsScreen(GridLayout):
  """
  Displays a list of user's collections
  """
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    print(**kwargs)
    self.collections = []
    self.username = None

  def initialize_widget(self, username):
    """
    Initializes the widget by setting class variables and creating widgets for each collection
    :param username: the logged in user
    """
    self.username = username
    self.get_collections_for_user()
    self.add_widget(back_button.BackButton())

  def get_collections_for_user(self):
    """
    Gets the collections for the user and adds the widgets
    """
    self.collections = collections.get_collections_for_user(self.username)
    for collection in self.collections:
      button_text = f"{collection.get('name')}\nNumber of Movies: {collection.get('numMovies')}" +\
                    f"\nTotal Length: {collection.get('lengthHr')}:"
      if collection.get('lengthMin') < 10:
        button_text += f"0{collection.get('lengthMin')}"
      else:
        button_text += f"{collection.get('lengthMin')}"
      button = Button(text=button_text, ids={'collection_id': collection.get('collection_id')})
      button.bind(on_press=self.go_to_collection_page)
      self.children[-1].add_widget(button)

  def go_to_collection_page(self, button):
    """
    Navigates the current view to the specific collection
    :param button: the button clicked
    """
    self.parent.update_child('Collection', collection_id=button.ids.get('collection_id'))

  def add_collection(self, button):
    """
    Creates a new collection and updates the user collections
    :param button: the button clicked
    """
    collections.add_collection(self.username)
    self.newcollection.text = ''
    self.remove_widget(self.children[-1])
    self.add_widget(BoxLayout(), len(self.children))
    self.get_collections_for_user()
