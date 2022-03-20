"""
CSCI.320 Project: Movie Domain

File: movies.py

Authors: - Milo Berry
         - Gunnar Bachmann
         - Ari Wisenburn
         - Noah Pelletier

Description:
"""

from config import DB_USERNAME, DB_PASSWORD, DB_NAME
import psycopg2
from sshtunnel import SSHTunnelForwarder
from datetime import datetime


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


def get_movie(movie_id, username):
    """
  Gets the data for a specific movie INCLUDING the users latest watched date and current rating
  :param movie_id: the movie id to get data for
  :param username: the username of the logged in user
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # SQL
    query = r"""SELECT title,
                       mpaa_rating,
                       runtime / 60 AS hours,
                       runtime % 60 AS minutes,
                       release_date,
                       date_watched,
                       star_rating
                FROM p320_21.movie
                LEFT JOIN p320_21.watched ON movie.movie_id = watched.movie_id
                WHERE username = '{}' AND movie.movie_id = {};""".format(username, movie_id)

    # Execute SQL
    curs.execute(query)
    records = curs.fetchall()

    # Save query result into a list (list of dict objects)
    result_list = []
    for record in records:
      result_list.append(dict(zip(['title', 'mpaa_rating', 'runtimeHr', 'runtimeMin',
                                   'releaseDate', 'lastWatched', 'rating'], record)))

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return result_list


def watch_movie(movie_id, username):
    """
  Marks a movie as watched by the given user
  :param movie_id: the id of the movie watched
  :param username: the username of the user that has watched the movie
  :return: None
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # Get current date
    current_date = datetime.today().strftime('%Y-%m-%d')

    # SQL
    query = r"""INSERT INTO p320_21.watched(username, movie_id, date_watched)
                VALUES ('{}', {}, '{}');""".format(username, movie_id, current_date)

    # Execute SQL
    curs.execute(query)
    conn.commit()

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return


def rate_movie(movie_id, username, rating):
    """
  Rates a movie from a specified user
  :param movie_id: the id of the movie to be rated
  :param username: the username of the user rating the film
  :param rating: the rating the user is giving the film
  :return: None
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    # SQL
    query = r"""UPDATE p320_21.watched SET star_rating = {}
                WHERE username = '{}' AND movie_id = {};""".format(rating, username, movie_id)

    # Execute SQL
    curs.execute(query)
    conn.commit()

    # Close the Database Cursor and Connection
    curs.close()
    conn.close()

    return


def search_by_name(movie_name, sort_type):
    """
  Searches for a movie by name
  :param movie_name: the name to search for
  :param sort_type: the sort type for the search
  :return: A list of movies that have titles matching the search name
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    where_statement = f"WHERE movie.title LIKE '%{movie_name}%''"
    search_query = get_full_search_query(where_statement, sort_type)

    # Execute the SQL to get search results
    curs.execute(search_query)
    records = curs.fetchall()

    # Save query result into a list (list of dict objects)
    result_list = []
    for record in records:
        result_list.append(dict(zip(
            ['movie_id', 'title', 'director', 'runtimeHr', 'runtimeMin', 'studio', 'cast_members', 'mpaa_rating',
             'rating']
            , record)))

    print(result_list)
    return result_list


def search_by_release_date(release_date, sort_type):
    """
  Searches for a movie by release data
  :param release_date: the release data to search for
  :param sort_type: the sort type for the search
  :return: A list of movies that have release dates matching the search date
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    where_statement = f"WHERE to_char(movie.release_date, 'DD/MM/YYYY') LIKE '%{release_date}%''"
    search_query = get_full_search_query(where_statement, sort_type)

    # Execute the SQL to get search results
    curs.execute(search_query)
    records = curs.fetchall()

    # Save query result into a list (list of dict objects)
    result_list = []
    for record in records:
        result_list.append(dict(zip(
            ['movie_id', 'title', 'director', 'runtimeHr', 'runtimeMin', 'studio', 'cast_members', 'mpaa_rating',
             'rating']
            , record)))

    print(result_list)
    return result_list


def search_by_cast(cast_member, sort_type):
    """
  Searches for a movie by cast member
  :param cast_member: the cast member name to search for
  :param sort_type: the sort type for the search
  :return: A list of movies that have cast members matching the search name
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    where_statement = f"WHERE actors.actors_list LIKE '%{cast_member}%'"
    search_query = get_full_search_query(where_statement, sort_type)

    # Execute the SQL to get search results
    curs.execute(search_query)
    records = curs.fetchall()

    # Save query result into a list (list of dict objects)
    result_list = []
    for record in records:
        result_list.append(dict(zip(
            ['movie_id', 'title', 'director', 'runtimeHr', 'runtimeMin', 'studio', 'cast_members', 'mpaa_rating',
             'rating']
            , record)))

    print(result_list)
    return result_list


def search_by_studio(studio_name, sort_type):
    """
  Searches for a movie by studio name
  :param studio_name: the studio name to search for
  :param sort_type: the sort type for the search
  :return: A list of movies that have studios matching the search name
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    where_statement = f"WHERE s.studios LIKE '%{studio_name}%'"
    search_query = get_full_search_query(where_statement, sort_type)

    # Execute the SQL to get search results
    curs.execute(search_query)
    records = curs.fetchall()

    # Save query result into a list (list of dict objects)
    result_list = []
    for record in records:
        result_list.append(dict(zip(
            ['movie_id', 'title', 'director', 'runtimeHr', 'runtimeMin', 'studio', 'cast_members', 'mpaa_rating',
             'rating']
            , record)))

    print(result_list)
    return result_list


def search_by_genre(genre_name, sort_type):
    """
  Searches for a movie by genre
  :param genre_name: the name of the genre to search for
  :param sort_type: the sort type for the search
  :return: A list of movies that have genre matching the search genre
  """
    # Establish Database Connection
    conn = connect_to_db()
    curs = conn.cursor()

    where_statement = f"WHERE genre.genres LIKE '%{genre_name}%'"
    search_query = get_full_search_query(where_statement, sort_type)

    # Execute the SQL to get search results
    curs.execute(search_query)
    records = curs.fetchall()

    # Save query result into a list (list of dict objects)
    result_list = []
    for record in records:
        result_list.append(dict(zip(
            ['movie_id', 'title', 'director', 'runtimeHr', 'runtimeMin', 'studio', 'cast_members', 'mpaa_rating',
             'rating']
            , record)))

    print(result_list)
    return result_list


def get_sort_type_query_from_name(sort_name):
    """
  Gets the ORDER BY statement for the query
  :param sort_name: The sort name to get the ORDER BY for
  :return: string of order by query
  """
    if sort_name == 'Default':
        return "ORDER BY movie.title, extract(YEAR from movie.release_date)"
    elif sort_name == 'Movie Name':
        return "ORDER BY movie.title"
    elif sort_name == 'Studio':
        return "ORDER BY s.studios"
    elif sort_name == 'Genre':
        return "ORDER BY genre.genres"
    elif sort_name == 'Released Year':
        return "ORDER BY extract(YEAR from movie.release_date)"
    else:
        return


def get_full_search_query(where_clause, sort_name):
    """
  Gets the entire query for the search given the where clause and the sort type
  :param where_clause: The where clause for the query
  :param sort_name: The sort type name for the query
  :return: a string of the query
  """
    sort_statement = get_sort_type_query_from_name(sort_name)
    return f"""
      select
           movie.movie_id,
           movie.title,
           concat(n.first_name, ' ', n.last_name) as director,
           movie.runtime / 60 as runtimeHr,
           movie.runtime % 60 as runtimeMin,
           s.studios as studios,
           actors.actors_list as actors,
           movie.mpaa_rating,
           avg(watched.star_rating) as rating
      from p320_21.movie
      left join p320_21.watched watched on movie.movie_id = watched.movie_id
      left join p320_21.person p on p.id = movie.director_id
      left join p320_21.name n on n.id = p.id
      left join (select funds.movie_id, string_agg(s.name, ', ') as studios
      from p320_21.funds
      left join p320_21.studio s on s.studio_id = funds.studio_id
      group by funds.movie_id) as s on movie.movie_id = s.movie_id
      left join (select acts_in.movie_id, string_agg(concat(n.first_name, ' ', n.last_name), ', ') as actors_list
      from p320_21.acts_in
      left join p320_21.person p on p.id = acts_in.person_id
      left join p320_21.name n on n.id = p.id
      group by acts_in.movie_id) as actors on movie.movie_id = actors.movie_id
      left join (select movie_genre.movie_id, string_agg(g.name, ', ') as genres
      from p320_21.movie_genre
      left join p320_21.genre g on movie_genre.genre_id = g.genre_id
      group by movie_genre.movie_id) as genre on genre.movie_id = movie.movie_id
      {where_clause}
      group by movie.movie_id, n.first_name, n.last_name, movie.title, s.studios, actors_list, movie.release_date, genre.genres
      {sort_statement};
    """
