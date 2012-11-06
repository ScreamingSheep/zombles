-- Create the database.
DROP DATABASE IF EXISTS zombles;
CREATE DATABASE zombles;
USE zombles;

-- Create the zombles user.
GRANT ALL ON zombles TO 'zombles'@'localhost';

-- A list of rooms that compose the level.
CREATE TABLE rooms (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name text NOT NULL,
    left_wall int NOT NULL,
    right_wall int NOT NULL,
    top_wall int NOT NULL,
    bottom_wall int NOT NULL
);
