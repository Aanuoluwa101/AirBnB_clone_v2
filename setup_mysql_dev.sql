-- This script preparesa MySQL server
-- for the HBNB project

-- create a database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create a new user in localhost
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant new user privleges on hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant new user select privilege
-- on the performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
