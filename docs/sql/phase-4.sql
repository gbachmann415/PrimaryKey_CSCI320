---------------------------------------------------------------
-- User Profile Features
---------------------------------------------------------------

----
-- Number of collections a user has
----
SELECT COUNT(DISTINCT collection_id)
FROM p320_21.collection
WHERE username = '{}';

----
-- Number of followers
----
SELECT COUNT(DISTINCT username)
FROM p320_21.following
WHERE following_username = '{}';

----
-- Number of following
----
SELECT COUNT(DISTINCT following_username)
FROM p320_21.following
WHERE username = '{}';

----
-- Top 10 movies (by highest rating)
----
SELECT DISTINCT movie_id
FROM p320_21.watched
WHERE username = '{}'
ORDER BY star_rating DESC
LIMIT 10;
----
-- Top 10 movies (most plays)
----
SELECT DISTINCT movie_id
FROM p320_21.watched
WHERE username = '{}'
ORDER BY COUNT(movie_id) DESC
LIMIT 10;
----
-- Top 10 movies (Combination of highest rating and most plays)
----
SELECT DISTINCT movie_id
FROM p320_21.watched
WHERE username = '{}'
ORDER BY COUNT(movie_id) DESC, star_rating DESC
LIMIT 10;
---------------------------------------------------------------
-- Recommendation Features
---------------------------------------------------------------

----
-- Top 20 most popular movies in the last 90 days (rolling)
----

----
-- Top 20 most popular movies among my friends
----

----
-- Top 5 new releases of the month
----

----
-- For you: Recommend movies to watch based on your play history (e.g. genre, cast member,
--          rating) and the play history of similar users.
----