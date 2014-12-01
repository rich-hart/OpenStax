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

Build image database for testing

      python build_test_database.py
      
Check database contents

      sqlite3 test.db
      sqlite> .schema
      sqlite> SELECT * FROM Images;
      sqlite> SELECT * FROM Images_Names;


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

Entires for filenames and images in the database tables that are created when build_test_database.py is run will not nessisarily correspond to one another.  This is due to the fact that the functions meant to handle these operations not designed to run concurently. This is not a problem since the database that is created is only for testing purposes  and is not meant to be the actual database used by the image server. 

