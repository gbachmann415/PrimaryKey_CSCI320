"""
CSCI.320 Project: Movie Domain

File: load_test_data.py

Authors: - Milo Berry
         - Gunnar Bachmann
         - Ari Wisenburn
         - Noah Pelletier

Description: Loads test data into database
"""
from time import sleep
from random import randint
from movies import watch_movie, rate_movie
from user import create_user, follow_user
from src.collections import add_collection, add_movie_to_collection

# collections = ['Collection1', 'Collection2', 'Collection3', 'Collection4', 'Collection5']
collection1_movies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 20]
collection2_movies = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 95, 100]
collection3_movies = [105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170]
collection4_movies = [22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56]
collection5_movies = [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
collection6_movies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 20]


def main():
    # Create users
    print("Creating Users...")
    print(create_user('test1', 'test1pw', 'Gunnar', 'Bachmann', 'test1@gmail.com'))
    print(create_user('test2', 'test2pw', 'Bob', 'Dylan', 'test2@gmail.com'))
    print(create_user('test3', 'test3pw', 'Jonny', 'Appleseed', 'test3@gmail.com'))
    print(create_user('test4', 'test4pw', 'Sam', 'Hunt', 'test4@gmail.com'))
    print('Done\n')

    # Follow users
    print("Following Users...")
    follow_user('test1', 'test2')
    follow_user('test1', 'test3')
    follow_user('test1', 'test4')
    follow_user('test2', 'test1')
    follow_user('test3', 'test2')
    follow_user('test4', 'test3')
    print("Done\n")

    # Add Collections
    print("Creating Collections...")
    add_collection('test1', 'Collection1')
    add_collection('test1', 'Collection2')
    add_collection('test2', 'Collection3')
    add_collection('test3', 'Collection4')
    add_collection('test4', 'Collection5')
    add_collection('test4', 'Collection6')
    print("Done\n")

    # Add Movies to Collections
    print("Adding Movies to Collections...")
    for i in collection1_movies:
        add_movie_to_collection('test1', 'Collection1', i)
    for i in collection2_movies:
        add_movie_to_collection('test1', 'Collection2', i)
    for i in collection3_movies:
        add_movie_to_collection('test2', 'Collection3', i)
    for i in collection4_movies:
        add_movie_to_collection('test3', 'Collection4', i)
    for i in collection5_movies:
        add_movie_to_collection('test4', 'Collection5', i)
    for i in collection6_movies:
        add_movie_to_collection('test4', 'Collection6', i)
    print("Done\n")

    # Watch Movies
    print("Marking Movies as Watched...")
    for i in collection1_movies:
        watch_movie(i, 'test1')
        sleep(5)
    for i in collection2_movies:
        watch_movie(i, 'test1')
        sleep(5)
    for i in collection3_movies:
        watch_movie(i, 'test2')
        sleep(5)
    for i in collection4_movies:
        watch_movie(i, 'test3')
        sleep(5)
    for i in collection5_movies:
        watch_movie(i, 'test4')
        sleep(5)
    for i in collection6_movies:
        watch_movie(i, 'test4')
        sleep(5)
    print("Done\n")

    # Rate Movies
    print("Rating Movies...")
    for i in collection1_movies:
        rate_movie(i, 'test1', randint(1, 5))
    for i in collection2_movies:
        rate_movie(i, 'test1', randint(1, 5))
    for i in collection3_movies:
        rate_movie(i, 'test2', randint(1, 5))
    for i in collection4_movies:
        rate_movie(i, 'test3', randint(1, 5))
    for i in collection5_movies:
        rate_movie(i, 'test4', randint(1, 5))
    for i in collection6_movies:
        rate_movie(i, 'test4', randint(1, 5))
    print("Done\n")

    print("Loading test data has completed.")

    return


main()
