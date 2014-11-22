#!/usr/bin/python
# -*- coding: utf-8 -*-
# source code: http://zetcode.com/db/sqlitepythontutorial/
import sqlite3 as lite
import sys

image_directory = "images/"
#image_file_name = "knot.jpg"
#image_file_name = "Linux_logo.png"
image_file_name = "partyanimsm.gif"

def readImage():

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







try:
    con = lite.connect('test.db')
    
    cur = con.cursor()
    data = readImage()
    binary = lite.Binary(data)
    cur.execute("DROP TABLE IF EXISTS Images")
    cur.execute("CREATE TABLE Images(image_id INTEGER PRIMARY KEY, image BLOB)")
    cur.execute("INSERT INTO Images(image) VALUES (?)", (binary,) )
    cur.execute("DROP TABLE IF EXISTS Images_Names")
    cur.execute("CREATE TABLE Images_Names(image_id INTEGER PRIMARY KEY, File_name TEXT)")
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

