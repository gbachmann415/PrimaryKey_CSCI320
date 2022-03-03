----------------------------------------------------------------------------------
-- GENRE TABLE
----------------------------------------------------------------------------------
create table p320_21.genre
(
    genre_id int not null
        constraint genre_pk
            primary key,
    name     varchar
);

create unique index genre_genre_id_uindex
    on p320_21.genre (genre_id);
----------------------------------------------------------------------------------
-- STUDIO TABLE
----------------------------------------------------------------------------------
create table p320_21.studio
(
    studio_id int not null
        constraint studio_pk
            primary key,
    name      varchar
);

create unique index studio_studio_id_uindex
    on p320_21.studio (studio_id);
----------------------------------------------------------------------------------
-- NAME TABLE
----------------------------------------------------------------------------------
create table p320_21.name
(
    id         int not null
        constraint name_pk
            primary key,
    first_name varchar,
    last_name  varchar
);

create unique index name_id_uindex
    on p320_21.name (id);
----------------------------------------------------------------------------------
-- USER TABLE
----------------------------------------------------------------------------------
create table p320_21."user"
(
    user_id          int not null
        constraint user_pk
            primary key,
    name_id          int
        constraint user_name_id_fk
            references p320_21.name,
    creation_date    timestamp,
    password         varchar,
    email            varchar,
    last_access_date timestamp
);

create unique index user_user_id_uindex
    on p320_21."user" (user_id);
----------------------------------------------------------------------------------
-- PERSON TABLE
----------------------------------------------------------------------------------
create table p320_21.person
(
    id      int not null
        constraint person_pk
            primary key
        constraint person_name_id_fk
            references p320_21.name,
    name_id int
);

create unique index person_id_uindex
    on p320_21.person (id);
----------------------------------------------------------------------------------
-- MOVIE TABLE
----------------------------------------------------------------------------------
create table p320_21.movie
(
    movie_id     int not null
        constraint movie_pk
            primary key,
    title        varchar,
    mpaa_rating  varchar,
    runtime      interval,
    release_date date,
    director_id  int
        constraint movie_person_id_fk
            references p320_21.person
);

create unique index movie_movie_id_uindex
    on p320_21.movie (movie_id);
----------------------------------------------------------------------------------
-- MOVIE GENRE TABLE
----------------------------------------------------------------------------------
create table p320_21.movie_genre
(
    movie_id int not null
        constraint movie_genre_movie_movie_id_fk
            references p320_21.movie,
    genre_id int not null
        constraint movie_genre_genre_genre_id_fk
            references p320_21.genre,
    constraint movie_genre_pk
        primary key (movie_id, genre_id)
);
----------------------------------------------------------------------------------
--  TABLE
----------------------------------------------------------------------------------
