-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres, tv_genres WHERE tv_show_genres.genre_id = tv_genres.id AND tv_show_genres.show_id = tv_shows.id ORDER BY tv_shows.title, tv_show_genres.genre_id;
© 2020 GitHub, Inc.
