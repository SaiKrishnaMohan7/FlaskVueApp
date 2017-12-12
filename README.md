# Flask CRUD App

## Runnign the App?

1) Create a virtualenv -> virtualenv `name_of_your_preference`
2) Intsall requirements -> `pip install -r requirements.txt`
3) Tell Flask what configuraton to run `FLASK_CONFIG=development`
4) Tell Flask what to run -> `FLASK_APP=run.py`
5) Check if you have mysql installed or `brew install mysql` or `sudo apt-get install mysql`
6) Fire up the db server with `mysqld`
7) Run `mysql -u root`
8) Run these command one by one
    ``` CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'dt2017';```
    
    ```CREATE DATABASE dreamteam_db;```
    
    ```GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'dt_admin'@'localhost';```
9) Run the App -> flask run


## Places where I got stuck while building the app
* I am using a Mac for this and following are the places where I got stuck and the internet bailed me out
    * While installing the dependencies, msql-python, crapped out and complained that msql_config is not found. [This] (https://stackoverflow.com/questions/25459386/mac-os-x-environmenterror-mysql-config-not-found) helped. Turns out, mysql wasn't globally installed.

    * After doing the above I tried conecting to the DB, NOPE! Threw `ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)`. [This] (https://stackoverflow.com/questions/15450091/for-a-newbie-error-2002-hy000-cant-connect-to-local-mysql-server-through-so) helped, specifically a comment on the accepted answer by user ProfNanda.
