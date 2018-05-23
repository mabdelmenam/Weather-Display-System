DROP DATABASE IF EXISTS weather;

CREATE DATABASE weather;

USE weather

CREATE TABLE weather(
	state CHAR(2),
	city VARCHAR(20),
	weather VARCHAR(20),
	temp CHAR(2),
	humidity CHAR(2),
	pres DECIMAL(4,2)
);
