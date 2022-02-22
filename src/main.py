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


username = DB_USERNAME
password = DB_PASSWORD
dbName = DB_NAME

"""
Establish a connection to the database with username, password, and database name.
Failed connection will result in a connection failed output to the user.
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
        # conn.close()
except:
    print("Connection failed")
    # TODO do we want to end program if connection fails by adding an exit statement?


def main():
    """
    [Description goes here]
    :return: None
    """
    #
    # body of main function will go before the connection close call.
    #
    conn.close()  # Close the connection to the database


if __name__ == '__main__':
    main()
