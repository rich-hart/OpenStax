#!/usr/bin/python
# -*- coding: utf-8 -*-

# further reading: http://zetcode.com/db/sqlitepythontutorial/
import sqlite3 as lite
import sys
import os


image_output_directory = "./output_images/"  #Output directory for image database retrieval testing

DATABASE = 'test.db'#database file name

''' function that takes image data and saves it to the file path'''
def writeImage(data,image_path):
    
    try:
        
        fout = open(image_path,'wb')
        
        fout.write(data)
    
    except IOError, e:    
        
        print "Error %d: %s" % (e.args[0], e.args[1])
        
        sys.exit(1)
        
    finally:
        
        if fout:
            
            fout.close()       

''' function that retrieves image data from the database at the specified index'''
def retrieve_image_data_from_db(retrieve_index):
    
    try:
        
        con = lite.connect(DATABASE)
        
        cur = con.cursor()
        
        cur.execute("SELECT image FROM Images WHERE image_id = %d LIMIT 1"%retrieve_index)
        
        data = cur.fetchone()[0]
        
        return data
        
    except lite.Error, e:
        
        print "Error %s:" % e.args[0]
        
        sys.exit(1)
        
    finally:
        
        if con:
            
            con.close()

''' a function that retrieves the file name of an image at the specified index '''
def retrieve_image_filename_from_db(retrieve_index):
    
    try:
        
        con = lite.connect(DATABASE)
        
        cur = con.cursor()
        
        cur.execute("SELECT File_name FROM Images_Names WHERE image_id=%d"%retrieve_index)
        
        image_file_name = cur.fetchone()[0]
        
        return image_file_name
    
    except lite.Error, e:
        
        print "Error %s:" % e.args[0]
        
        sys.exit(1)
        
    finally:
        
        if con:
            
            con.close()

''' retrieves the number of images that have been stored in the database'''
def retrieve_image_count():
    
    try:
        
        con = lite.connect(DATABASE)
        
        cur = con.cursor()
        
        cur.execute("SELECT COUNT(*) FROM Images")
        
        file_count = cur.fetchone()[0]
        
        return int(file_count)
    
    except lite.Error, e:
        
        print "Error %s:" % e.args[0]
        
        sys.exit(1)
        
    finally:
        
        if con:
            
            con.close()
            
''' A main function meant to test the database and its support functions.  The main function
reads all the images currently stored in the database and write those images into an output folder.  '''
if __name__ == "__main__":
    
    if not os.path.exists(image_output_directory):
        
        os.makedirs(image_output_directory)
        
    file_count = retrieve_image_count()
    
    for query_index in range(1,file_count+1):
        
        image_file_name = retrieve_image_filename_from_db(query_index)
        
        data = retrieve_image_data_from_db(query_index)
        
        writeImage(data,image_output_directory+image_file_name)
    
    