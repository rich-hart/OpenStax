#!/usr/bin/python
# -*- coding: utf-8 -*-

# further reading: http://zetcode.com/db/sqlitepythontutorial/

import database_support_functions 

import sqlite3 as lite
import sys
from os import listdir
from os.path import isfile, join


image_directory = "./input_images/" #default directory where test images are stored


'''function for the reading of images'''
def readImage(image_file_name):

    try:
        
        fin = open(image_directory+image_file_name, "rb")
        
        img = fin.read()
        
        return img
        
    except IOError, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        
        sys.exit(1)

    finally:
        
        if fin:
            
            fin.close()


'''function for loading images into a sqlite DATABASE'''
def load_image_into_database(image_file_name):
    
    try:
        
        con = lite.connect(database_support_functions.DATABASE)
        
        cur = con.cursor()
        
        data = readImage(image_file_name)
        
        binary = lite.Binary(data)
        
        cur.execute("INSERT INTO Images(image) VALUES (?)", (binary,) )

        cur.execute("INSERT INTO Images_Names(File_name) VALUES (?)", (image_file_name,) )
    
        con.commit()    
        
    except lite.Error, e:
        
        if con:
            
            con.rollback()
            
        print "Error %s:" % e.args[0]
        
        sys.exit(1)
        
    finally:
        
        if con:
            
            con.close()
            
            
''' function for listing files currently in a directory'''            
def get_file_names_from_dir(directory):
    
    file_list = [ f for f in listdir(directory) if isfile(join(directory,f)) ]
    
    return file_list


'''
main function that is used to load a collection of images from a directory into a 
database for testing both the database_support_functions and image_server modules.  When the main
function is run two tables are created (if tables existed before they are destroyed).  One table 
named 'Images' is used to store a collection of image data, the other table Images_Names stores their
original file names.  
'''
if __name__ == "__main__":
    
    try:
        #connect to the DATABASE
        con = lite.connect(database_support_functions.DATABASE)
        
        cur = con.cursor()
        #destroy and create a new image table
        cur.execute("DROP TABLE IF EXISTS Images_Names")
        
        cur.execute("CREATE TABLE Images_Names(image_id INTEGER PRIMARY KEY, File_name TEXT)")
        
        cur.execute("DROP TABLE IF EXISTS Images")
        
        cur.execute("CREATE TABLE Images(image_id INTEGER PRIMARY KEY, image BLOB)")
        
    except lite.Error, e:
        
        if con:
            
            con.rollback()
            
        print "Error %s:" % e.args[0]
        
        sys.exit(1)
        
    finally:
        
        if con:
            
            con.close()
    #load images from directory into the DATABASE
    image_file_list = get_file_names_from_dir(image_directory)
    
    for image_file in image_file_list:
        
        load_image_into_database(image_file)
