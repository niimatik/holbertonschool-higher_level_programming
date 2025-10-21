-- a script that creates the MySQL server user user_0d_1.
INSERT INTO user (name)
VALUES ('user_0d_1')
GRANT ALL PRIVILEGES TO 'user_0d_1'@'localhost';
[IDENTIFIED BY 'user_0d_1_pwd']
