"""
CSCI.320 Project: Movie Domain

File: main.py

Authors: - Milo Berry
         - Gunnar Bachmann
         - Ari Wisenburn
         - Noah Pelletier

Description:
"""

from config import DB_USERNAME, DB_PASSWORD, DB_NAME
import psycopg2
from sshtunnel import SSHTunnelForwarder
from src.ui import application as ui


def main():
    """
    [Description goes here]

    :return: None
    """
    # Start the Movie Application (Launching the UI)
    ui.MovieApplication().run()


if __name__ == '__main__':
    main()
