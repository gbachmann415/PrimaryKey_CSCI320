-- average rating per genre of movies in collections
select g.name, ROUND(CAST(avg(star_rating) as numeric), 2) as average_rating
from p320_21.movie
         left join p320_21.movies_in_collection as mc
                   on movie.movie_id = mc.movie_id
         left join p320_21.movie_genre as mg
                   on mg.movie_id = movie.movie_id
         left join p320_21.genre as g
                   on g.genre_id = mg.genre_id
         left join p320_21.watched as w
                   on w.movie_id = movie.movie_id
where collection_id is not null
  and w.star_rating is not null
group by g.name;

--number of movies in each genre that have been added to collections
select g.name, count(mc.movie_id)
from p320_21.movie
         left join p320_21.movies_in_collection as mc
                   on movie.movie_id = mc.movie_id
         left join p320_21.movie_genre as mg
                   on mg.movie_id = movie.movie_id
         left join p320_21.genre as g
                   on g.genre_id = mg.genre_id
where collection_id is not null
group by g.name;

--average rating of top 10 actor (that have been in the most movies)'s movie
select concat(n.first_name, ' ', n.last_name), (select ROUND(cast(avg(w.star_rating) as numeric), 2)
                   from p320_21.movie
                            left join p320_21.watched as w
                                      on movie.movie_id = w.movie_id
                            left join p320_21.acts_in as a on movie.movie_id = a.movie_id
                   where w.movie_id is not null
                     and a.person_id = acts_in.person_id
                   group by person_id
) as star_avg
from p320_21.acts_in
left join p320_21.movie m on m.movie_id = acts_in.movie_id
left join p320_21.person p on acts_in.person_id = p.id
left join p320_21.name n on p.name_id = n.id
group by person_id, n.first_name, n.last_name
order by count(person_id) desc
limit 10;