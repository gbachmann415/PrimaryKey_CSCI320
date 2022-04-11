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
    print(create_user('test5', 'test5pw', 'Gunnar2', 'Bachmann2', 'test5@gmail.com'))
    print(create_user('test6', 'test6pw', 'Bob2', 'Dylan2', 'test6@gmail.com'))
    print(create_user('test7', 'test7pw', 'Jonny2', 'Appleseed2', 'test7@gmail.com'))
    print(create_user('test8', 'test8pw', 'Sam2', 'Hunt2', 'test8@gmail.com'))
    print('Done\n')

    # Follow users
    print("Following Users...")
    follow_user('test5', 'test6')
    follow_user('test5', 'test7')
    follow_user('test5', 'test8')
    follow_user('test6', 'test5')
    follow_user('test7', 'test6')
    follow_user('test8', 'test7')
    print("Done\n")

    # Add Collections
    print("Creating Collections...")
    add_collection('test5', 'Collection7')
    add_collection('test5', 'Collection8')
    add_collection('test6', 'Collection9')
    add_collection('test7', 'Collection10')
    add_collection('test8', 'Collection11')
    add_collection('test8', 'Collection12')
    print("Done\n")

    # Add Movies to Collections
    print("Adding Movies to Collections...")
    for i in collection1_movies:
        add_movie_to_collection('test5', 'Collection7', i)
    for i in collection2_movies:
        add_movie_to_collection('test5', 'Collection8', i)
    for i in collection3_movies:
        add_movie_to_collection('test6', 'Collection9', i)
    for i in collection4_movies:
        add_movie_to_collection('test7', 'Collection10', i)
    for i in collection5_movies:
        add_movie_to_collection('test8', 'Collection11', i)
    for i in collection6_movies:
        add_movie_to_collection('test8', 'Collection12', i)
    print("Done\n")

    # Watch Movies
    print("Marking Movies as Watched...")
    for i in collection1_movies:
        watch_movie(i, 'test5')
        sleep(5)
    for i in collection2_movies:
        watch_movie(i, 'test5')
        sleep(5)
    for i in collection3_movies:
        watch_movie(i, 'test6')
        sleep(5)
    for i in collection4_movies:
        watch_movie(i, 'test7')
        sleep(5)
    for i in collection5_movies:
        watch_movie(i, 'test8')
        sleep(5)
    for i in collection6_movies:
        watch_movie(i, 'test8')
        sleep(5)
    print("Done\n")

    # Rate Movies
    print("Rating Movies...")
    for i in collection1_movies:
        rate_movie(i, 'test5', randint(1, 5))
    for i in collection2_movies:
        rate_movie(i, 'test5', randint(1, 5))
    for i in collection3_movies:
        rate_movie(i, 'test6', randint(1, 5))
    for i in collection4_movies:
        rate_movie(i, 'test7', randint(1, 5))
    for i in collection5_movies:
        rate_movie(i, 'test8', randint(1, 5))
    for i in collection6_movies:
        rate_movie(i, 'test8', randint(1, 5))
    print("Done\n")

    print("Loading test data has completed.")

    return


main()
