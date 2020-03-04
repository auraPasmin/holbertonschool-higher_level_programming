-- script that lists all cities contained in the database hbtn_0d_usa.
-- join
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows 
INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
