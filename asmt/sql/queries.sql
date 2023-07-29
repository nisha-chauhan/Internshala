-- Create a MySQL database with the name "users". 
create database users;

-- for using the created database
use users;

-- Design a table "users" with the following columns:
--  - id (int, primary key)
--  - name (varchar)
--  - email (varchar)
--  - role (varchar) 
 CREATE TABLE users(
         ID int NOT NULL PRIMARY KEY,
         NAME varchar(200) NOT NULL,
         EMAIL varchar(200),
        ROLE varchar(255)
     );


-- SQL queries to:
--  - Insert sample data into the "users" table. 

INSERT INTO users (ID, NAME, EMAIL, ROLE)
     VALUES (154, 'Nisha Chauhan', 'nisha@mail.com', 'Admin');

--- Retrieve all users from the "users" table. 
select * from users;

--  - Retrieve a specific user by their ID. 
select * from users WHERE ID=154;
