#!/usr/bin/python
# -*- coding: utf-8 -*-
# source code: http://zetcode.com/db/sqlitepythontutorial/
import sqlite3 as lite
import sys

image_file_name = "images/knot.jpg"

def readImage():

    try:
        fin = open(image_file_name, "rb")
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
    cur.execute("CREATE TABLE Images(Id INTEGER PRIMARY KEY, Data BLOB)")
    cur.execute("INSERT INTO Images(Data) VALUES (?)", (binary,) )

    con.commit()    
    
except lite.Error, e:
    
    if con:
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()  

