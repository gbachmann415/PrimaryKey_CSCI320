from datetime import datetime
from config import DB_USERNAME, DB_PASSWORD, DB_NAME
import psycopg2
from sshtunnel import SSHTunnelForwarder


def connect_to_db():
    """
    Establish a connection to the database with username, password, and database name.
    Failed connection will result in a connection failed output to the user and program exit.

    :return: conn = connection to database
    """
    try:
        server = SSHTunnelForwarder(('starbug.cs.rit.edu', 22),
                                    ssh_username=DB_USERNAME,
                                    ssh_password=DB_PASSWORD,
                                    remote_bind_address=('localhost', 5432))
        server.start()
        # print("SSH tunnel established")
        params = {
            'database': DB_NAME,
            'user': DB_USERNAME,
            'password': DB_PASSWORD,
            'host': 'localhost',
            'port': server.local_bind_port
        }

        conn = psycopg2.connect(**params)
        # print("Database connection established")
    except:
        print("Connection failed")
        exit()

    return conn


def main():
    conn = connect_to_db()
    curs = conn.cursor()

    drop_tables = """DROP TABLE p320_21.acts_in CASCADE;
                     DROP TABLE p320_21.collection CASCADE;
                     DROP TABLE p320_21.following CASCADE;
                     DROP TABLE p320_21.funds CASCADE;
                     DROP TABLE p320_21.genre CASCADE;
                     DROP TABLE p320_21.movie CASCADE;
                     DROP TABLE p320_21.movie_genre CASCADE;
                     DROP TABLE p320_21.movies_in_collection CASCADE;
                     DROP TABLE p320_21.name CASCADE;
                     DROP TABLE p320_21.person CASCADE;
                     DROP TABLE p320_21.studio CASCADE;
                     DROP TABLE p320_21."user" CASCADE;
                     DROP TABLE p320_21.watched CASCADE;"""

    tables_sql_file = open(r'../docs/sql/tables.sql')
    create_tables = tables_sql_file.read()
    add_perms_file = open('../docs/sql/permissions.sql')
    add_perms = add_perms_file.read()

    curs.execute(drop_tables)
    conn.commit()
    curs.execute(create_tables)
    conn.commit()
    curs.execute(add_perms)
    conn.commit()

    return


if __name__ == '__main__':
    main()
