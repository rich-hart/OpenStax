#!/usr/bin/python
# -*- coding: utf-8 -*-

# source code: http://zetcode.com/db/sqlitepythontutorial/
import sqlite3 as lite
import sys

image_output_directory = "output_images/"

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
    

try:
    con = lite.connect('test.db')
    cur = con.cursor()
    
    cur.execute("SELECT File_name FROM Images_Names WHERE Id=1")
    image_file_name = cur.fetchone()[0]
    #image_file_name = "output_images/knot.jpg"
    
    cur.execute("SELECT Data FROM Images WHERE Id = 1 LIMIT 1")
    data = cur.fetchone()[0]
    
    writeImage(data,image_output_directory+image_file_name)

    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()