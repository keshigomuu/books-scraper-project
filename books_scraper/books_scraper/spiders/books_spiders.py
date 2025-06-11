import scrapy
from books_scraper.items import BookItem
from urllib.parse import urljoin

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            detail_url = book.css('h3 a::attr(href)').get()
            detail_url = urljoin(response.url, detail_url)
            yield response.follow(detail_url, callback=self.parse_book_details)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_book_details(self, response):
        item = BookItem()
        item['title'] = response.css('div.product_main h1::text').get()
        item['price'] = response.css('p.price_color::text').get()
        item['rating'] = response.css('p.star-rating::attr(class)').get().replace('star-rating', '').strip()
        item['availability'] = response.css('p.availability::text').re_first('\d+')
        item['description'] = response.css('#product_description ~ p::text').get()
        item['category'] = response.css('ul.breadcrumb li:nth-child(3) a::text').get()
        item['product_page_url'] = response.url
        item['image_url'] = urljoin(response.url, response.css('div.item.active img::attr(src)').get())

        table = response.css('table.table.table-striped tr')
        for row in table:
            label = row.css('th::text').get()
            value = row.css('td::text').get()
            if label == 'UPC':
                item['upc'] = value
            elif label == 'Product Type':
                item['product_type'] = value
            elif label == 'Price (excl. tax)':
                item['price_excl_tax'] = value
            elif label == 'Price (incl. tax)':
                item['price_incl_tax'] = value
            elif label == 'Tax':
                item['tax'] = value
            elif label == 'Number of reviews':
                item['num_reviews'] = value

        yield item
