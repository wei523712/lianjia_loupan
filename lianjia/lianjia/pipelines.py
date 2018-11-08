# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LianjiaPipeline(object):
    def open_spider(self,spider):
        # 链接数据库
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123456',db='lianjia',charset='utf8')
        # 获取游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO loupan (lpm,bm,jj,xmdz,slcdz,kfs,wygs,zxkp,jfsj,cqnx,ghhs,cwqk,gsfs,jzlx,zdmj,wylx,rjl,lhl,wyfy,gnfs,gdfs,xwss,jzmj,xmts,qywz,cwpb,city) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (item['lpm'],item['bm'],item['jj'],item['xmdz'],item['slcdz'],item['kfs'],item['wygs'],item['zxkp'],item['jfsj'],item['cqnx'],item['ghhs'],item['cwqk'],item['gsfs'],item['jzlx'],item['zdmj'],item['wylx'],item['rjl'],item['lhl'],item['wyfy'],item['gnfs'],item['gdfs'],item['xwss'],item['jzmj'],item['xmts'],item['qywz'],item['cwpb'],item['city'])
        try:
            self.cursor.execute(sql)
            # 提交
            self.conn.commit()
        except Exception as e:
            print('写入错误：',e)
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()