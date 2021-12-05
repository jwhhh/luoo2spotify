import logging
import scrapy
import scrapy_splash
from scrapy_splash import SplashRequest
from scrapy import Selector


res_folder = "playlists_luoow"

class LuoowSpider(scrapy.Spider):
    name = "luoow"
    base_url = "https://www.luoow.com"
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
    }

    def start_requests(self):
        urls = [f'{self.base_url}/{i}/' for i in range(1,1000)]
        for url in urls:
            # yield scrapy.Request(url=url, callback=self.parse)
            yield SplashRequest(url, self.parse,
                args={
                    # optional; parameters passed to Splash HTTP API
                    'wait': 3,

                    # 'url' is prefilled from request url
                    # 'http_method' is set to 'POST' for POST requests
                    # 'body' is set to request body for POST requests
                },
                # endpoint='render.json', # optional; default is render.html
                # splash_url='<url>',     # optional; overrides SPLASH_URL
                slot_policy=scrapy_splash.SlotPolicy.PER_DOMAIN,  # optional
            )

    def parse(self, response):  #TODO
        page = response.url.split("/")[-2]
        self.log(f'Downloaded html from page {page}', level=logging.INFO)

        selector = Selector(response)
        title = selector.css('h3::text').get()
        indices = selector.css('[class="skPlayer-list-index"]::text').extract()
        song_names = selector.css('[class="skPlayer-list-name"]::text').extract()
        song_artists = selector.css('[class="skPlayer-list-author"]::text').extract()
        songs = list(zip(indices, song_names, song_artists))

        print()
        print(songs)
        print()

        playlist_name = "_".join(title.split(' ')[1:])
        filename = f'{res_folder}/vol_%03d_{playlist_name}.csv' % int(page)
        with open(filename, 'w+') as f:
            for i in range(len(indices)):
                f.write(", ".join(songs[i]) + "\n")
        
        self.log(f'Saved file {filename}', level=logging.INFO)
