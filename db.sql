INSERT INTO public.actors
(name, age, gender)
VALUES('Tom', 51, 'Male');

INSERT INTO public.actors
(name, age, gender)
VALUES('jennifer', 45, 'Female');

INSERT INTO public.actors
(name, age, gender)
VALUES('The Rock', 51, 'Male');

INSERT INTO public.actors
(name, age, gender)
VALUES('kevin hart', 45, 'Male');

INSERT INTO public.movies
(title, "relaseDate")
VALUES('bad bosess', current_date);

INSERT INTO public.movies
(title, "relaseDate")
VALUES('terminal', current_date);


INSERT INTO public.movies
(title, "relaseDate")
VALUES('ride along', current_date);

INSERT INTO public.movies
(title, "relaseDate")
VALUES('fast', current_date);



INSERT INTO public.actor_movies_map
("Actor_id", "Movie_id")
VALUES(2, 1);


INSERT INTO public.actor_movies_map
("Actor_id", "Movie_id")
VALUES(1, 2);



INSERT INTO public.actor_movies_map
("Actor_id", "Movie_id")
values(4, 3);


INSERT INTO public.actor_movies_map
("Actor_id", "Movie_id")
VALUES(3, 4);