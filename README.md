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

      python build_database.py
      
check databaase contents

      sqlite3 test.db
      .schema Images
      sqlite> SELECT * FROM Images;
      sqlite> SELECT * FROM Images_Names;



Communicate with Server
--------

Start the server

      chmod +x image_server.py
      python image_server.py 8000

Retrieve Images From Server:

      http://0.0.0.0:8000/images/1

Notes
--------
Assume that the database is saved as 'test.db'

retrieve_image_from_db.py has sqlite support functions
