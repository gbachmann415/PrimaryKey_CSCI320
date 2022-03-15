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
    id         SERIAL
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
    username        varchar not null
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
-- ACTS IN TABLE
----------------------------------------------------------------------------------
create table p320_21.acts_in
(
    movie_id  int
        constraint acts_in_movie__fk
            references p320_21.movie,
    person_id int
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
    movie_id  int
        constraint funds_movie_movie_id_fk
            references p320_21.movie,
    studio_id int
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
    collection_id int not null
        constraint collection_pk
            primary key,
    name          varchar,
    username      varchar
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
    collection_id int
        constraint movies_in_collection_collection_collection_id_fk
            references p320_21.collection,
    movie_id      int
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
    username           varchar
        constraint following_user_username_fk
            references p320_21."user",
    following_username varchar
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
    username     varchar
        constraint watched_user_username_fk
            references p320_21."user",
    movie_id     int
        constraint watched_movie_movie_id_fk
            references p320_21.movie,
    date_watched date,
    star_rating  float,
    constraint watched_pk
        primary key (username, movie_id, date_watched)
);