#Source Code http://webpy.github.io/images

import web
import os

from retrieve_image_from_db import * 

#database = 'test.db'

urls = (
'/images/(.*)', 'images' #this is where the image folder is located....
)

class images:
    def GET(self,index):
        
        index = int(index)
        
        data = retrieve_image_data_from_db(index)
        return data # Notice 'rb' for reading images

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()