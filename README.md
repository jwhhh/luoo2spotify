# luoo2spotify

A scraper and playlist creater for self learning and use.

## How to run it

Set up virtual environment and install dependencies from provided yaml file.

To run Splash, follow instructions from [their doc](https://splash.readthedocs.io/en/latest/install.html) or use the following:

```shell
$ docker run -p 8050:8050 scrapinghub/splash
```

After Splash starts running, crawl:

```shell
$ scrapy crawl luoow
```
