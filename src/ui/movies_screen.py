from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from src.ui import back_button


class MoviesScreen(GridLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.username = None
    self.movies = None

  def initialize_widget(self, username, movie_list, simple_results=False):
    """
    Initializes the widget by filling in class variables and populating the list of movies
    :param username:
    :param movie_list:
    :return:
    """
    self.username = username
    self.movies = movie_list

    if len(self.movies) == 0:
      self.children[-1].children[0].add_widget(Label(text='No Results', size_hint_y=None, height='400dp'))
    else:
      for movie in self.movies:
        if simple_results:
          minute = f'0{movie.get("runtimeMin")}' if movie.get(
            "runtimeMin") < 10 else f'{movie.get("runtimeMin")}'
          rating = "N/A" if movie.get("rating") is None else str(round(movie.get("rating"), 2))
          last_watched = "N/A" if movie.get("lastWatched") is None else movie.get("lastWatched")
          button_text = f'Title: {movie.get("title")}\n' + \
                        f'MPAA Rating: {movie.get("mpaa_rating")}\n' + \
                        f'Runtime: {movie.get("runtimeHr")}:{minute}\n' + \
                        f'Release Date: {movie.get("releaseDate")}\n' + \
                        f'Last Watched: {last_watched}\n' + \
                        f'Rating: {rating}\n'
        else:
          cast = "" if movie.get("cast_members") is None else movie.get("cast_members").replace(", ", ",\n")
          studio = "" if movie.get("studio") is None else movie.get("studio").replace(", ", ",\n")
          minute = f'0{movie.get("runtimeMin")}' if movie.get(
            "runtimeMin") < 10 else f'{movie.get("runtimeMin")}'
          rating = "N/A" if movie.get("rating") is None else str(round(movie.get("rating"), 2))
          button_text = f'Title: {movie.get("title")}\n' + \
                        f'MPAA Rating: {movie.get("mpaa_rating")}\n' + \
                        f'Runtime: {movie.get("runtimeHr")}:{minute}\n' + \
                        f'Release Date: {movie.get("releaseDate")}\n' + \
                        f'Rating: {rating}\n' +\
                        f'Director: {movie.get("director")}\n' +\
                        f'Cast Member(s): {cast}\n' +\
                        f'Studio(s): {studio}'
        movie_button = Button(text=button_text, ids={'movie_id': movie.get('movie_id')}, size_hint_y=None, height='400dp')
        movie_button.bind(on_press=self.go_to_movie)
        self.children[-1].children[0].add_widget(movie_button)

    self.add_widget(back_button.BackButton())

  def go_to_movie(self, button):
    """
    Navigates the user to a specific movie
    :param button: the button selected
    """
    print(button.ids.get('movie_id'))
    self.parent.update_child('Movie', movie_id=button.ids.get('movie_id'))
