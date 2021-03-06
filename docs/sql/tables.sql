----------------------------------------------------------------------------------
-- GENRE TABLE
----------------------------------------------------------------------------------
create table p320_21.genre
(
    genre_id int not null
        constraint genre_pk
            primary key,
    name     varchar not null
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
    name      varchar not null
);

create unique index studio_studio_id_uindex
    on p320_21.studio (studio_id);
----------------------------------------------------------------------------------
-- NAME TABLE
----------------------------------------------------------------------------------
create table p320_21.name
(
    id         SERIAL
        constraint name_pk
            primary key,
    first_name varchar not null,
    last_name  varchar not null
);

create unique index name_id_uindex
    on p320_21.name (id);
----------------------------------------------------------------------------------
-- USER TABLE
----------------------------------------------------------------------------------
create table p320_21."user"
(
    username        varchar not null
        constraint user_pk
            primary key,
    name_id          int not null
        constraint user_name_id_fk
            references p320_21.name,
    creation_date    date not null,
    password         varchar not null,
    email            varchar not null,
    last_access_date timestamp not null
);

create unique index user_username_uindex
    on p320_21."user" (username);
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
    name_id int not null
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
    runtime      int,
    release_date date,
    director_id  int
        constraint movie_person_id_fk
            references p320_21.person
        constraint mpaa_rating check(mpaa_rating in ('G', 'PG', 'PG-13', 'R', 'NC-17', 'NR'))
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
-- ACTS IN TABLE
----------------------------------------------------------------------------------
create table p320_21.acts_in
(
    movie_id  int not null
        constraint acts_in_movie__fk
            references p320_21.movie,
    person_id int not null
        constraint acts_in_person__fk
            references p320_21.person,
    constraint acts_in_pk
        primary key (movie_id, person_id)
);
----------------------------------------------------------------------------------
-- FUNDS TABLE
----------------------------------------------------------------------------------
create table p320_21.funds
(
    movie_id  int not null
        constraint funds_movie_movie_id_fk
            references p320_21.movie,
    studio_id int not null
        constraint funds_studio_studio_id_fk
            references p320_21.studio,
    constraint funds_pk
        primary key (movie_id, studio_id)
);
----------------------------------------------------------------------------------
-- COLLECTION TABLE
----------------------------------------------------------------------------------
create table p320_21.collection
(
    collection_id serial not null
        constraint collection_pk
            primary key,
    name          varchar not null,
    username      varchar not null
        constraint collection_user_username_fk
            references p320_21."user"
);

create unique index collection_collection_id_uindex
    on p320_21.collection (collection_id);
----------------------------------------------------------------------------------
-- MOVIES IN COLLECTION TABLE
----------------------------------------------------------------------------------
create table p320_21.movies_in_collection
(
    collection_id int not null
        constraint movies_in_collection_collection_collection_id_fk
            references p320_21.collection,
    movie_id      int not null
        constraint movies_in_collection_movie_movie_id_fk
            references p320_21.movie,
    constraint movies_in_collection_pk
        primary key (collection_id, movie_id)
);
----------------------------------------------------------------------------------
-- FOLLOWING TABLE
----------------------------------------------------------------------------------
create table p320_21.following
(
    username           varchar not null
        constraint following_user_username_fk
            references p320_21."user",
    following_username varchar not null
        constraint following_user_username_fk_2
            references p320_21."user",
    constraint following_pk
        primary key (username, following_username)
);
----------------------------------------------------------------------------------
-- WATCHED TABLE
----------------------------------------------------------------------------------
create table p320_21.watched
(
    username     varchar not null
        constraint watched_user_username_fk
            references p320_21."user",
    movie_id     int not null
        constraint watched_movie_movie_id_fk
            references p320_21.movie,
    date_watched timestamp,
    star_rating  float
        constraint watched_star_rating_check
            CHECK(star_rating >= 1 AND star_rating <= 5),
    constraint watched_pk
        primary key (username, movie_id, date_watched)
);