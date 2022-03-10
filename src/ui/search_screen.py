from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


class SearchScreen(GridLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.username = None

  def initialize_widget(self, username):
    self.username = username
    dropdown = DropDown()
    search_by_list = ['Movie Name', 'Release Date', 'Cast Members', 'Studio', 'Genre']
    for element in search_by_list:
      print(element)
      btn = Button(text=element, size_hint_y=None, height='32dp')
      btn.bind(on_release=lambda button: dropdown.select(button.text))
      dropdown.add_widget(btn)
    search_by = Button(text='Search By', size_hint_y=None, height='32dp')
    search_by.bind(on_release=dropdown.open)
    dropdown.bind(on_select=lambda instance, x: setattr(search_by, 'text', x))
    self.children[-1].add_widget(search_by, 1)
