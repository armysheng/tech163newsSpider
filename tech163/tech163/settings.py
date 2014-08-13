# -*- coding: utf-8 -*-

# Scrapy settings for tech163 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tech163'

SPIDER_MODULES = ['tech163.spiders']
NEWSPIDER_MODULE = 'tech163.spiders'
ITEM_PIPELINES = ['tech163.pipelines.Tech163Pipeline',
			]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tech163 (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'

DOWNLOAD_TIMEOUT = 15
# DOWNLOAD_DELAY = 0.1
# LOG_LEVEL = "INFO"
# LOG_STDOUT = True
# LOG_FILE = "log/newsSpider.log"
