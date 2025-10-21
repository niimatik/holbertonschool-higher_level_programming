-- lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT name, id
FROM states
WHERE {
	SELECT id
	FROM cities
	WHERE name = 'California'
} ASC;
