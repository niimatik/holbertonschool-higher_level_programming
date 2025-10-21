-- lists all cities contained in the database hbtn_0d_usa.
SELECT id, name
FROM cities
JOIN states ON cities.id = states.id
ORDER BY cities.id ASC;
