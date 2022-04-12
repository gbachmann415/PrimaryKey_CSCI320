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
SELECT DISTINCT watched.movie_id,
                title,
                mpaa_rating,
                runtime / 60 AS hours,
                runtime % 60 AS minutes,
                to_char(release_date, 'yyyy-MM-dd'),
                star_rating,
                to_char(MAX(date_watched), 'yyyy-MM-dd')
FROM p320_21.watched
LEFT JOIN p320_21.movie ON watched.movie_id = movie.movie_id
WHERE username = '{}' AND star_rating IS NOT NULL
GROUP BY watched.movie_id, title, mpaa_rating, hours, minutes, release_date, star_rating
ORDER BY star_rating DESC
LIMIT 10;

----
-- Top 10 movies (most plays)
----
SELECT DISTINCT watched.movie_id,
                title,
                mpaa_rating,
                runtime / 60 AS hours,
                runtime % 60 AS minutes,
                to_char(release_date, 'yyyy-MM-dd'),
                star_rating,
                to_char(MAX(date_watched), 'yyyy-MM-dd'),
                COUNT(watched.movie_id)
FROM p320_21.watched
LEFT JOIN p320_21.movie ON watched.movie_id = movie.movie_id
WHERE username = '{}' AND star_rating IS NOT NULL
GROUP BY watched.movie_id, title, mpaa_rating, hours, minutes, release_date, star_rating
ORDER BY COUNT(watched.movie_id) DESC
LIMIT 10;

----
-- Top 10 movies (Combination of highest rating and most plays)
-- NOTE: ASK ABOUT HOW HE WANTS THE COMBINATION OF THE TWO.
----
SELECT DISTINCT watched.movie_id,
                title,
                mpaa_rating,
                runtime / 60 AS hours,
                runtime % 60 AS minutes,
                to_char(release_date, 'yyyy-MM-dd'),
                star_rating,
                to_char(MAX(date_watched), 'yyyy-MM-dd'),
                COUNT(watched.movie_id)
FROM p320_21.watched
LEFT JOIN p320_21.movie ON watched.movie_id = movie.movie_id
WHERE username = '{}' AND star_rating IS NOT NULL
GROUP BY watched.movie_id, title, mpaa_rating, hours, minutes, release_date, star_rating
ORDER BY COUNT(watched.movie_id) DESC, star_rating DESC
LIMIT 10;

----
-- Top 20 most popular movies in the last 90 days (rolling)
----

SELECT watched.movie_id,
       title,
       mpaa_rating,
       runtime / 60 AS hours,
       runtime % 60 AS minutes,
       to_char(release_date, 'yyyy-MM-dd'),
       avg(star_rating),
       to_char(MAX(date_watched), 'yyyy-MM-dd'),
       COUNT(watched.movie_id)
FROM p320_21.watched
LEFT JOIN p320_21.movie ON watched.movie_id = movie.movie_id
WHERE date_watched > current_date - interval '90' day
GROUP BY watched.movie_id, title, mpaa_rating, hours, minutes, release_date
ORDER BY COUNT(watched.movie_id) DESC
LIMIT 20;

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

---------------------------------------------------------------
-- MISC
---------------------------------------------------------------

CREATE INDEX collection_username_index ON p320_21.collection (username);
CREATE INDEX genre_name_index ON p320_21.genre (name);
CREATE INDEX movie_title_index ON p320_21.movie (title);
CREATE INDEX movie_release_date_index ON p320_21.movie (release_date);
CREATE INDEX person_name_id_index ON p320_21.person (name_id);
CREATE INDEX studio_name_index ON p320_21.studio (name);
CREATE INDEX user_email_index ON p320_21."user" (email);
CREATE INDEX watched_star_rating_index ON p320_21.watched (star_rating);