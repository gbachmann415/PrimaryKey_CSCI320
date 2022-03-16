"""
CSCI.320 Project: Movie Domain

File: main.py

Authors: - Milo Berry
         - Gunnar Bachmann
         - Ari Wisenburn
         - Noah Pelletier

Description:
"""

from src.ui import application as ui


def main():
    """
    [Description goes here]

    :return: None
    """
    # Start the Movie Application (Launching the UI)
    ui.MovieApplication().run()

    return


if __name__ == '__main__':
    main()
