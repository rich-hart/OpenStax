OpenStax
========
Setup
--------

      sudo pip install web.py
      sudo pip install flup
      sudo apt-get install python-psycopg2
      
<!---And run chmod +x code.py to make it executable.-->

Run Server
--------
Make the file executable

      chmod +x code.py

Run the file 

      python code.py

Specify port by running

      python code.py 1234

Retrieve Images From Server
--------

      python image_server.py 8000
      http://0.0.0.0:8000/images/Linux_logo.png
