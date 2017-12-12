# Flask CRUD App

## Places where I got stuck
* I am using a Mac for this and following are the places where I got stuck and the internet bailed me out
    * While installing the dependencies, msql-python, crapped out and complained that msql_config is not found. [This] (https://stackoverflow.com/questions/25459386/mac-os-x-environmenterror-mysql-config-not-found) helped. Turns out, mysql wasn't globally installed.

    * After doing the above I tried conecting to the DB, NOPE! Threw `ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)`. [This] (https://stackoverflow.com/questions/15450091/for-a-newbie-error-2002-hy000-cant-connect-to-local-mysql-server-through-so) helped, specifically a comment on the accepted answer by user ProfNanda.

    * Tried the Blueprint route, didn't really wokrout.
