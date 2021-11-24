import scrapy


class LuooSpider(scrapy.Spider):
    name = "luoo"

    def start_requests(self):
        urls = [f'https://www.luoow.com/{i}/' for i in range(1,1000)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):  #TODO
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')