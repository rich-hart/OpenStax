#!/usr/bin/python
# -*- coding: utf-8 -*-

# source code: http://zetcode.com/db/sqlitepythontutorial/
import sqlite3 as lite
import sys


database = 'test.db'

'''function for reading image data from a database'''
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




    
    