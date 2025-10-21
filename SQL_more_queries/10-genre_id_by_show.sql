-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_shows_genre.genre_id = tv_shows.title
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
