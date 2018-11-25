# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:04:10 2018

@author: mimota
"""
import pymysql

db = pymysql.connect(host = '127.0.0.1',
port = 3306,
user = 'test_user',
passwd = '1290',
db = 'test_for_user',
charset = 'utf8')

cursor = db.cursor()

createTableSql = '''
        create table user(
        id int PRIMARY key not null auto_increment,
        name char(20) not null,
        passwd char(20),
        address char(20),
        point float(5),
        other char(50)
        )
        '''
        
def insertUser(name, passwd, address, point, other = None):        
    insertUserSql = "insert into  user(name,passwd,address,point,other) \
                    values ('%s','%s','%s','%f','%s')"\
                    %(name, passwd, address, point, other)
    
    try:
        cursor.execute(insertUserSql)
        db.commit()
    except:
        print("insert error")
        db.rollback();

        
def selectUser(id):        
    selectUserSql = "select * from user \
                    where id = '%d'" \
                    %(id)
                    
    try:
        cursor.execute(selectUserSql)
        results = cursor.fetchall()
    except:
        print("lookup error")
        
    for row in results:
        id = row[0]
        name = row[1]
        passwd = row[2]
        address = row[3]
        point = row[4]
        other = row[5]
        print("id = %d, name = %s, passwd = %s, address = %s, point = %f, other = %s"\
              %(id, name, passwd, address, point, other))
        
    return results