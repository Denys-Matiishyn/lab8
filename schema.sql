CREATE DATABASE IF NOT EXISTS auction;
USE auction;

CREATE TABLE IF NOT EXISTS buyers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    f_name VARCHAR(50),
    s_name VARCHAR(50),
    phone_number VARCHAR(20),
    email VARCHAR(100) UNIQUE
);