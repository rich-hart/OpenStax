#further reading: http://webpy.github.io/images

import web
import os
from retrieve_image_from_db import retrieve_image_data_from_db
'''
database name is assumed to be 'test.db'

url suffix where images can be retrieved .e.g. 
 http://0.0.0.0:8000/images/2
'''

urls = (
'/images/(.*)', 'images' 
)

'''class that handles REST API GET request'''
class images:
    
    def GET(self,index):
        
        index = int(index)
        
        data = retrieve_image_data_from_db(index)
        
        return data 

'''main function which starts the server'''
if __name__ == "__main__":
    
    app = web.application(urls, globals())
    
    app.run()