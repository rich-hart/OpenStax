#!/usr/bin/python
# -*- coding: utf-8 -*-

# source code: http://zetcode.com/db/sqlitepythontutorial/
import sqlite3 as lite
import sys
import os
image_output_directory = "./output_images/"
database = 'test.db'
query_index = 1

def writeImage(data,image_file_name):
    try:
        fout = open(image_file_name,'wb')
        fout.write(data)
    
    except IOError, e:    
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
        
    finally:
        
        if fout:
            fout.close()       

def retrieve_image_data_from_db(retrieve_index):
    try:
        con = lite.connect(database)
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

def retrieve_image_filename_from_db(retrieve_index):
    try:
        con = lite.connect(database)
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

    
if __name__ == "__main__":
    if not os.path.exists(image_output_directory):
        os.makedirs(image_output_directory)
    image_file_name = retrieve_image_filename_from_db(query_index)
    data = retrieve_image_data_from_db(query_index)
    writeImage(data,image_output_directory+image_file_name)
    
    