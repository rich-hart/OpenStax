OpenStax
========
Notes
--------

Setup

      sudo pip install web.py
      sudo pip install flup
      sudo apt-get install python-psycopg2
      sudo apt-get install sqlite
      
<!---And run chmod +x code.py to make it executable.-->

Run Server:

Make the file executable

      chmod +x code.py

Run the file 

      python code.py

Specify port by running

      python code.py 1234

Test Database Setup:

build image database for testing

      python build_database.py
      
check databaase contents

      sqlite3 test.db
      .schema Images
      sqlite> SELECT * FROM Images;
      sqlite> SELECT * FROM Images_Names;

Retrieve Images From Server:


      python image_server.py 8000
      http://0.0.0.0:8000/images/1

Note: code assumes that database is saved under 'test.db'
