-- Script to create a table called first_table if it doesn't already exist
USE database_name; -- Replace 'database_name' with the actual name of the database
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
