import scrapy
from ..items import FindWatchesItem


class TunisianetSpider(scrapy.Spider):
    name = 'tunisianet'
    allowed_domains = ['www.tunisianet.com.tn']
    start_urls = [
        'https://www.tunisianet.com.tn/550-montre-homme-femme-tunisie?f215-genre=homme,mixte&order=product.price.asc'
    ]

    def parse(self, response):
        items = FindWatchesItem()
        title = response.css('img.logo::attr(alt)').extract_first()

        div_product = response.css('article')
        for product in div_product:
            name = product.css('h2 a::text').extract_first()
            brand = product.css('img::attr(alt)').extract_first()
            price = product.css('span.price::text').extract_first()
            status = product.css('span.in-stock::text').extract_first()
            link = product.css('h2 a::attr(href)').extract_first()
            img = product.css('img::attr(src)').extract_first()
            items['name'] = name
            items['img'] = img
            items['brand'] = brand
            items['price'] = price
            items['status'] = status
            items['link'] = link
            items['website'] = title
            yield items

        next_page = response.css('.pagination').css('li a.next').css('a::attr(href)').get()
        print(next_page)

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
