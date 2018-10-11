# -*- coding: utf-8 -*-

import pymysql
from image.settings import DB_CONFIG

class DBHelper():
    '''
    读取settings中的配置，实现数据库操作
    '''
    def __init__(self):
        
        self.connect = pymysql.connect(
            host=DB_CONFIG['MYSQL_HOST'],
            db=DB_CONFIG['MYSQL_DBNAME'],
            user=DB_CONFIG['MYSQL_USER'],
            passwd=DB_CONFIG['MYSQL_PASSWD'],
            charset=DB_CONFIG['MYSQL_CHARSET'],
            port=DB_CONFIG['MYSQL_PORT']
        )

        self.cursor = self.connect.cursor()

    #插入数据库
    def insert(self, item):
        cursor = self.cursor
        sql = "insert into images(title,img_url) values(%s,%s)"
        #调用插入的方法
        cursor.execute(sql, (
            item["title"], item['url']
            )
        )
        self.connect.commit()
        return item