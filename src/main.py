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

username = DB_USERNAME
password = DB_PASSWORD
dbName = DB_NAME


def connect_to_db():
    """
    Establish a connection to the database with username, password, and database name.
    Failed connection will result in a connection failed output to the user and program exit.

    :return: conn = connection to database
    """
    try:
        print("Attempting to establish database connection...")
        with SSHTunnelForwarder(('starbug.cs.rit.edu', 22),
                                ssh_username=username,
                                ssh_password=password,
                                remote_bind_address=('localhost', 5432)) as server:
            server.start()
            print("SSH tunnel established")
            params = {
                'database': dbName,
                'user': username,
                'password': password,
                'host': 'localhost',
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            curs = conn.cursor()
            print("Database connection established")
    except:
        print("Connection failed")
        exit()

    return conn


def close_connection_to_db(conn):
    conn.close()
    return


def main():
    """
    [Description goes here]
    :return: None
    """
    # Establish connection to the Database
    # conn = connect_to_db()

    # Start the Movie Application (Launching the UI)
    ui.MovieApplication().run()

    # Close the connection to the Database
    # close_connection_to_db(conn)


if __name__ == '__main__':
    main()
