#Source Code http://webpy.github.io/images

import web
import os

from retrieve_image_from_db import * 

urls = (
'/images/(.*)', 'images' #this is where the image folder is located....
)

class images:
    def GET(self,index):
        
        index = int(index)
        name = retrieve_image_filename_from_db(index)
        
        ext = name.split(".")[-1] # Gather extension

        cType = {
            "png":"images/png",
            "jpg":"images/jpeg",
            "gif":"images/gif",
            "ico":"images/x-icon"            }

        if name in os.listdir('images'):  # Security
            web.header("Content-Type", cType[ext]) # Set the Header
            data = retrieve_image_data_from_db(index)
            return data # Notice 'rb' for reading images
        else:
            raise web.notfound()

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()