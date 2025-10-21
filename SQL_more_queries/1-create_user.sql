-- a script that creates the MySQL server user user_0d_1.
DROP USER IF EXISTS 'user_0d_1';
CREATE USER IF EXISTS 'user_0d_1'
GRANT ALL PRIVILEGES TO 'user_0d_1'@'localhost';
[IDENTIFIED BY 'user_0d_1_pwd']
