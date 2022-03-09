from kivy.app import App
from src.ui import display_widget as display
from kivy.lang import Builder


class MovieApplication(App):
  """
  The root UI application
  """
  def build(self):
    Builder.load_file('ui/login.kv')
    Builder.load_file('ui/home_screen.kv')
    Builder.load_file('ui/account_screen.kv')
    Builder.load_file('ui/back_button.kv')
    Builder.load_file('ui/collections_screen.kv')
    Builder.load_file('ui/collection.kv')
    Builder.load_file('ui/movie.kv')
    return display.Display()
