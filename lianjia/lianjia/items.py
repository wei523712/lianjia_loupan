# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    lpm = scrapy.Field()        #楼盘名1
    bm = scrapy.Field()         #别名1
    jj = scrapy.Field()         #均价1
    xmdz = scrapy.Field()       #项目地址1
    slcdz = scrapy.Field()      #售楼处地址1
    kfs = scrapy.Field()        #开发商1
    wygs = scrapy.Field()       #物业公司1
    zxkp = scrapy.Field()       #最新开盘1
    jfsj = scrapy.Field()       #交房时间1
    cqnx = scrapy.Field()       #产权年限1
    ghhs = scrapy.Field()       #规划户数1
    cwqk = scrapy.Field()       #车位情况1
    gsfs = scrapy.Field()       #供水方式1
    jzlx = scrapy.Field()       #建筑类型1
    zdmj = scrapy.Field()       #占地面积1
    wylx = scrapy.Field()       #物业类型1
    rjl = scrapy.Field()        #容积率1
    lhl = scrapy.Field()        #绿化率1
    wyfy = scrapy.Field()       #物业费用1
    gnfs = scrapy.Field()       #供暖方式1
    gdfs = scrapy.Field()       #供电方式1
    xwss = scrapy.Field()       #嫌恶设施1
    jzmj = scrapy.Field()       #建筑面积1
    xmts = scrapy.Field()       #项目特色1
    qywz = scrapy.Field()       #区域位置1
    cwpb = scrapy.Field()       #车位配比1
    city = scrapy.Field()       #归属城市1