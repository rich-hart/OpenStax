OpenStax
========


Setup
--------

Install web.py, flup,python-psycopg2 and sqlite

      sudo pip install web.py
      sudo pip install flup
      sudo apt-get install python-psycopg2
      sudo apt-get install sqlite
      
<!---And run chmod +x code.py to make it executable.-->
Build Test Database
--------

build image database for testing

      python build_test_database.py
      
check database contents

      sqlite3 test.db
      sqlite> .schema Images;
      sqlite> SELECT * FROM Images;
      sqlite> .schema Image_Names;
      sqlite> SELECT * FROM Image_Names;


Communicate with Server
--------

Start the server

      chmod +x image_server.py
      python image_server.py 8000

Retrieve images from server by going to the flowing urls in browser:

      http://0.0.0.0:8000/images/1
      http://0.0.0.0:8000/images/2
      http://0.0.0.0:8000/images/3

Notes
--------

Assume that the database is saved as 'test.db'

Assume that images are saved in database under a table named 'Images'

The file database_support_functions.py has sqlite support functions

The file image_server.py has web.py GET functions


