from kivy.uix.button import Button


class BackButton(Button):
  """
  A button that allows the user to return to the previous page
  """
  def __init__(self, **kwargs):
    super(BackButton, self).__init__(**kwargs)

  def previous_screen(self, button):
    """
    Returns to the previous page
    :param button: the button pressed
    """
    self.parent.parent.return_to_prev_screen()
