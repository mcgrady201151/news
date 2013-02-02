#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
import os
import time
import math

class PyMySQL:

    def __init__(self,host='localhost',port=8889,user='root',passwd='123456',db='query',charset='utf8'):

        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset

    def __del__ (self):

        pass
   
    def db_connect(self):
        
	conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
	cur = conn.cursor() 
	return cur

    def runSql(self,sql):
        cur = self.db_connect()
        try:
            cur.execute(sql)
            cur.connection.commit()
        except Exception,e:
            print e

  
    def getData(self,sql):#select all data
    
        cur = self.db_connect()	
        cur.execute(sql)
        data = cur.fetchall()
        return data
	
    def getLine(self,sql):#select one data

        cur = self.db_connect()	
        cur.execute(sql)
        data = cur.fetchone()
        return data    

    def getCount(self,sql):#return count of mysql
    
        cur = self.db_connect()	
        cur.execute(sql)
        count = cur.rowcount
        return count 
       
	

