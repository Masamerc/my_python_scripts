# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem

class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonspider'
    start_urls = ['https://www.amazon.com/s?i=videogames-intl-ship&bbn=16225016011&rh=n%3A16225016011%2Cn%3A6427814011%2Cp_n_date%3A1249090011&dc&page=1&fst=as%3Aoff&qid=1571886055&rnid=16225016011&ref=sr_pg_2']
    page_num = 2

    def parse(self, response):
        items = AmazonItem()

        name = response.css('.a-color-base.a-text-normal::text').extract()
        price = response.css('.index\=2 .a-spacing-top-small span , .a-spacing-top-small .a-price-whole').css('::text').extract()
        release_date = response.css('.a-spacing-top-micro span .a-color-secondary').css('::text').extract()
        image_link = response.css('.s-image::attr(src)').extract()

        items['item_name'] = name
        items['item_price'] = price
        items['item_imagelink'] = image_link
        items['item_releaseDate'] = release_date

        yield items

        if AmazonspiderSpider.page_num <= 5:
            next_page = 'https://www.amazon.com/s?i=videogames-intl-ship&bbn=16225016011&rh=n%3A16225016011%2Cn%3A6427814011%2Cp_n_date%3A1249090011&dc&page='\
                 + str(AmazonspiderSpider.page_num) + \
                     '&fst=as%3Aoff&qid=1571886055&rnid=16225016011&ref=sr_pg_2'
            AmazonspiderSpider.page_num += 1
            yield response.follow(next_page, callback=self.parse)






