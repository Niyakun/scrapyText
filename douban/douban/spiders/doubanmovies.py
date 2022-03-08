import scrapy
from douban.items import DoubanItem

class DoubanmoviesSpider(scrapy.Spider):
    name = 'doubanmovies'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://movie.douban.com/top250?start={}'.format(num*25)for num in range(11)]
    def parse(self, response):
        li_list=response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in li_list:
            id_list=li.xpath('./div/div[1]/em/text()').get()
            name_list=li.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            grade_list=li.xpath('./div/div[2]/div[2]/div/span[2]/text()').get()
            pj_list=li.xpath('./div/div[2]/div[2]/div/span[4]/text()').get()
            #print(name_list)
            item=DoubanItem()
            item['name_list']=name_list
            item['grade_list'] = grade_list
            item['pj_list'] = pj_list
            item['id_list']=id_list
            yield item



