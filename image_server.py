#further reading: http://webpy.github.io/images

from database_support_functions import retrieve_image_data_from_db

import web
import os


'''
OpenStax CNX Python Coding Exercise Part 2: 

Write a REST API that can be used to access an image by image_id using the code written in Step #1.  Assume it is a simple GET.  You can use any framework. 
Web.py (http://webpy.org/) is a simple framework if you need a suggestion.
'''


urls = ( '/images/(.*)', 'images' ) #URL Suffix where images can be loaded


'''class that handles REST API GET request.  The class uses the retrieve_image_data_from_db function
from the database_support_functions modules to retrieve image data needed to complete the get request'''
class images:
    
    def GET(self,index):
        
        index = int(index)
        
        image_data = retrieve_image_data_from_db(index)
        
        return image_data 


'''main function which starts the image server.  To test the server open up a web browser on the 
local machine and type in the domain returned by STDOUT when the script was first started, followed by
the suffix 'images/1', 'images/2', or 'images/2'.  For example, 'http://0.0.0.0:8000/images/1' '''
if __name__ == "__main__":
    
    app = web.application(urls, globals())
    
    app.run()