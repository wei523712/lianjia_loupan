# lianjia_loupan
This scrapy project is used to crawl the house information on chain home websites.
https://bj.fang.lianjia.com/loupan/
## 分析网页链接
链家网站上有很多个城市，查看了个城市的网页链接发现有些城市是简写，有些是全称，如下图所示：
![image](https://github.com/wei523712/lianjia_loupan/blob/master/%E5%8C%97%E4%BA%AC.png)
![image](https://github.com/wei523712/lianjia_loupan/blob/master/%E6%89%BF%E5%BE%B7.png)
对于有些城市的楼盘信息较多，不只一页，因此分析需要翻页。总页数可以通过div标签中的data-total-count属性提取，该数字除以每页的总条数10并向上取整即为总页数。
![image]()
## 分析可提取信息 字段
进入楼盘的一级详情页可以看到很多的相关楼盘信息，点击“楼盘详情”下面的“查看更多”可以进入二级详情页面，此页的楼盘详情比一级页面多几个，因此我们提取此处的信息。链接为一级页面的信息加“/xiangqing/”
