# encoding=utf-8
BOT_NAME = 'Sina_spider'

SPIDER_MODULES = ['Sina_spider.spiders']
NEWSPIDER_MODULE = 'Sina_spider.spiders'


ITEM_PIPELINES = {
    'Sina_spider.pipelines.NewsPipeline': 300,
}

SPLASH_URL = 'http://192.168.99.100:8050'

# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }

# 下载中间件设置
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810
}

# 设置去重过滤器
#DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# 启用缓存系统
#HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


# DOWNLOADER_MIDDLEWARES = {
#     "Sina_spider.middleware.UserAgentMiddleware": 401,
#     "Sina_spider.middleware.CookiesMiddleware": 402,
# }


DOWNLOAD_DELAY = 2  # 间隔时间
# CONCURRENT_ITEMS = 1000
# CONCURRENT_REQUESTS = 100
# REDIRECT_ENABLED = False
# CONCURRENT_REQUESTS_PER_DOMAIN = 100
# CONCURRENT_REQUESTS_PER_IP = 0
# CONCURRENT_REQUESTS_PER_SPIDER=100
# DNSCACHE_ENABLED = True
# LOG_LEVEL = 'INFO'    # 日志级别
# CONCURRENT_REQUESTS = 70
