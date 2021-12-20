# password-generator-manager

To run this:

1. Download the files to one folder
2. Install Postgresql with 'brew install postgresql'
3. Run 'psql postgres'   
4. Create database with 'create database password_manager;'
5. Connect to database with '\c password_manager'
6. Create a user with 'create user USER;' 
7. Create password with '\password PASSWORD'
Replace USER and PASSWORD with a username and password. 
Also, edit all the lines in pw_database.py such that user='soham', password='soham' is changed to user='USER', password='PASSWORD' with whatever values you chose)
7. Grant privileges with 'GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO USER;'
Once again, replace USER with your username
8. Run:
'CREATE TABLE accounts (app VARCHAR ( 50 ) NOT NULL, username VARCHAR ( 50 ), email VARCHAR ( 50 ) NOT NULL, password VARCHAR ( 50 ) NOT NULL, url VARCHAR ( 50 ), id SERIAL PRIMARY KEY);'
9. 'GRANT USAGE, SELECT ON SEQUENCE accounts_id_seq TO USER;'
Once again, replace USER with your username

Then, run 'python pw_manager.py' and use the password 'Password'. CHANGE THIS PASSWORD PLEASE!
