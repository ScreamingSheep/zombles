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

-- Doors.
CREATE TABLE doors (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    room_id int NOT NULL REFERENCES rooms,
    wall ENUM('left', 'right', 'top', 'bottom') NOT NULL,
    position int NOT NULL
);

-- Treasures.
CREATE TABLE treasures (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    room_id int NOT NULL REFERENCES rooms,
    name text NOT NULL,
    x int NOT NULL,
    y int NOT NULL
);

-- Users.
CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name text NOT NULL,
    x int NOT NULL,
    y int NOT NULL,
    health int NOT NULL
);

-- Items.
CREATE TABLE items (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id int NOT NULL REFERENCES rooms,
    name text NOT NULL
);
