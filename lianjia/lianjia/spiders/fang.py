# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem
import re
import math
class FangSpider(scrapy.Spider):
    name = 'fang'
    #allowed_domains = ['bj.fang.lianjia.com']
    #start_urls = ['https://bj.fang.lianjia.com/loupan/pg{}/',]

    page = 1
    def start_requests(self):
        f = open('G:/task/lianjia/lianjia/spiders/city.txt','r',encoding='gbk')
        for link in f:
            url = 'https:' + link.replace('\n','') + '/loupan/'
            yield scrapy.Request(url=url,callback=self.parse,meta={'c_url':url})

    #楼盘列表页
    def parse(self,response):

        bigtag = response.xpath('//div[@class="resblock-list-container clearfix"]/ul[@class="resblock-list-wrapper"]/li')
        for tag in bigtag:
            lp_link = tag.xpath('.//div/div[@class="resblock-name"]/a/@href').extract_first()
            yield scrapy.Request(url=response.urljoin(lp_link),callback=self.parse_lou)

        #翻页
        page_num = response.xpath('//div[@class="page-box"]/@data-total-count').extract_first()
        number = math.ceil(int(page_num)/10)
        link = response.meta['c_url']
        for p in range(2,number+1):
            url = link + 'pg' + str(p) + '/'
            yield scrapy.Request(url=url, callback=self.parse,meta={'c_url':link})

    #解析详情页1级
    def parse_lou(self,response):
        bigname = response.xpath('//div[@class="box-left"]/div[@class="box-left-top"]/div[@class="name-box"]/a/h1/text()').extract_first().strip()
        littlename = response.xpath('//div[@class="box-left"]/div[@class="box-left-top"]/div[@class="name-box"]/a/span/text()').extract_first()
        lpm_c = bigname if bigname else '无楼盘信息'
        bm_c = re.findall('别名/(.*)',littlename)[0] if littlename else '无别名信息'

        kaipan = response.xpath('//div[@class="box-loupan"]/ul/li[1]/p/span[2]/text()').extract_first().strip()
        jiaofang = response.xpath('//div[@class="box-loupan"]/ul/li[3]/p/span[2]/text()').extract_first().strip()
        xianwu = response.xpath('//div[@class="box-loupan"]/ul/li[12]/p/span[2]/text()').extract_first().strip()
        kpsj_c = kaipan if kaipan else '暂无开盘时间信息'
        jfsj_c = jiaofang if jiaofang else '暂无交房时间信息'
        xwss_c = xianwu if xianwu else '暂无嫌恶设施信息'

        next_detail = response.url + 'xiangqing/'
        yield scrapy.Request(url=next_detail,callback=self.parse_detail,meta={'lpm_c':lpm_c,'bm_c':bm_c,'kpsj_c':kpsj_c,'jfsj_c':jfsj_c,'xwss_c':xwss_c,})


    def parse_detail(self,response):
        item = LianjiaItem()
        item['lpm'] = response.meta['lpm_c']
        item['bm'] = response.meta['bm_c']
        item['zxkp'] = response.meta['kpsj_c']
        item['jfsj'] = response.meta['jfsj_c']
        item['xwss'] = response.meta['xwss_c']
        #基本信息
        tag_jb = response.xpath('//div[@class="big-left fl"]/ul[@class="x-box"][1]')
        wuyelx = tag_jb.xpath('.//li[1]/span[2]/text()').extract_first()
        xiangmuts = tag_jb.xpath('.//li[3]/span[2]/text()').extract_first()
        loupandz = tag_jb.xpath('.//li[5]/span[2]/text()').extract_first()
        shouloucdz = tag_jb.xpath('.//li[6]/span[2]/text()').extract_first()
        kaifas = tag_jb.xpath('.//li[7]/span[2]/text()').extract_first().strip()
        cankaojg = tag_jb.xpath('.//li[2]/span[2]/span/text()').extract_first().strip()
        quyuwz= tag_jb.xpath('.//li[4]/span[2]').xpath('string(.)').extract_first().strip()
        city = quyuwz.split('-')[0] if quyuwz else '暂无归属城市'
        item['wylx'] = wuyelx if wuyelx else '暂无物业类型信息'
        item['xmts'] = xiangmuts if xiangmuts else '暂无项目特色信息'
        item['xmdz'] = loupandz if loupandz else '暂无楼盘地址信息'
        item['slcdz'] = shouloucdz if shouloucdz else '暂无售楼处地址信息'
        item['kfs'] = kaifas if kaifas else '暂无开发商信息'
        item['jj'] = cankaojg if cankaojg else '暂无参考价格信息'
        item['qywz'] = quyuwz if quyuwz else '暂无区域位置信息'
        item['city'] = city
        #规划信息
        tag_gh = response.xpath('//div[@class="big-left fl"]/ul[@class="x-box"][2]')
        jianzhulx = tag_gh.xpath('.//li[1]/span[2]/text()').extract_first().strip()
        lvhual = tag_gh.xpath('.//li[2]/span[2]/text()').extract_first().strip()
        zhandimj = tag_gh.xpath('.//li[3]/span[2]/text()').extract_first().strip()
        rongjil = tag_gh.xpath('.//li[4]/span[2]/text()').extract_first().strip()
        jianzhumj = tag_gh.xpath('.//li[5]/span[2]/text()').extract_first().strip()
        guihuahs = tag_gh.xpath('.//li[7]/span[2]/text()').extract_first().strip()
        changquannx = tag_gh.xpath('.//li[8]/span[2]/text()').extract_first().strip()
        item['jzlx'] = jianzhulx if jianzhulx else '暂无建筑类型信息'
        item['lhl'] = lvhual if lvhual else '暂无绿化率信息'
        item['zdmj'] = zhandimj if zhandimj else '暂无占地面积信息'
        item['rjl'] = rongjil if rongjil else '暂无容积率信息'
        item['jzmj'] = jianzhumj if jianzhumj else '暂无建筑面积信息'
        item['ghhs'] = guihuahs if guihuahs else '暂无规划户数信息'
        item['cqnx'] = changquannx if changquannx else '暂无产权年限信息'
        #配套信息
        tag_pt = response.xpath('//div[@class="big-left fl"]/ul[@class="x-box"][3]')
        wuyegs = tag_pt.xpath('.//li[1]/span[2]/text()').extract_first().strip()
        cheweipb = tag_pt.xpath('.//li[2]/span[2]/text()').extract_first().strip()
        wuyef = tag_pt.xpath('.//li[3]/span[2]/text()').extract_first().strip()
        gongnuanfs = tag_pt.xpath('.//li[4]/span[2]/text()').extract_first().strip()
        gongshuifs = tag_pt.xpath('.//li[5]/span[2]/text()').extract_first().strip()
        gongdianfs = tag_pt.xpath('.//li[6]/span[2]/text()').extract_first().strip()
        chewei = tag_pt.xpath('.//li[7]/span[2]/text()').extract_first().strip()
        zhoubian = tag_pt.xpath('.//li[8]/div[@id="around_txt"]').xpath('string(.)').extract_first()
        item['wygs'] = wuyegs if wuyegs else '暂无物业公司信息'
        item['cwpb'] = cheweipb if cheweipb else '暂无车位信息'
        item['wyfy'] = wuyef if wuyef else '暂无物业费用信息'
        item['gnfs'] = gongnuanfs if gongnuanfs else '暂无供暖方式信息'
        item['gsfs'] = gongshuifs if gongshuifs else '暂无供水方式信息'
        item['gdfs'] = gongdianfs if gongdianfs else '暂无供电方式信息'
        item['cwqk'] = chewei.replace(' ','') if chewei else '暂无车位情况信息'
        yield item

