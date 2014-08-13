#encoding: utf-8
import scrapy
import re
from scrapy.selector import Selector
from tech163.items import Tech163Item
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
class ExampleSpider(CrawlSpider):
	name = "news"
	# allowed_domains = ["tech.163.com"]
	start_urls = ['http://tech.163.com/']
	# f = open("out.txt", "w") 
	rules=(
		Rule(LinkExtractor(allow=r"/14/08\d+/\d+/*"),
		callback="parse_news",follow=True),
	)
	def printcn(suni):
		for i in uni:
			print uni.encode('utf-8')
	def parse_news(self,response):
		item = Tech163Item()
		item['news_thread']=response.url.strip().split('/')[-1][:-5]
		# self.get_thread(response,item)
		self.get_title(response,item)
		self.get_source(response,item)
		self.get_url(response,item)
		self.get_news_from(response,item)
		self.get_from_url(response,item)
		self.get_text(response,item)
		return item##############!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!remenber to Retrun Item after parse
	def get_title(self,response,item):
		title=response.xpath("/html/head/title/text()").extract()
		if title:
			# print 'title:'+title[0][:-5].encode('utf-8')
			item['news_title']=title[0][:-5]

	def get_source(self,response,item):
		source=response.xpath("//div[@class='left']/text()").extract()
		if source:
			# print 'source'+source[0][:-5].encode('utf-8')
			item['news_time']=source[0][:-5]

	def get_news_from(self,response,item):
		news_from=response.xpath("//div[@class='left']/a/text()").extract()
		if news_from:
			# print 'from'+news_from[0].encode('utf-8')		
			item['news_from']=news_from[0]

	def get_from_url(self,response,item):
		from_url=response.xpath("//div[@class='left']/a/@href").extract()
		if from_url:
			# print 'url'+from_url[0].encode('utf-8')		
			item['from_url']=from_url[0]	

	def  get_text(self,response,item):
		news_body=response.xpath("//div[@id='endText']/p/text()").extract()
		if news_body:
			# for  entry in news_body:
			# 	print entry.encode('utf-8')
			item['news_body']=news_body	
	def get_url(self,response,item):
		news_url=response.url
		if news_url:
			print news_url	
		item['news_url']	=news_url
	# def get_thread(self,response,item):
	# 	news_thread=response.url.strip().split('/')[-1][:-5]
	# 	print news_thread
	# 	item['news_thread']=news_thread
		# print >>this.f,item			
	# def parse(self, response):
	#     #sel=Selector(response)
	#     #f=open("163new.html",'wb')
	#     #f.write(response.body)
	#     sel=Selector(response)
	#     posts = sel.xpath('//h2[@class="color-link"]')
	#     item = NewsItem()
	#     def printcn(uni):
	#         for i in uni:
	#             print uni.encode('utf-8')
	#     for post in posts:
	#         title=post.xpath('a/text()').extract()
	#         url=post.xpath('a/@href').extract()
	#         desc=post.xpath('a/data-title').extract()
	#         #whether list is empty
	#         if title:
	#             item['title']=title[0].encode('utf-8')
	#             printcn(title[0])
	#         else:
	#             item['title']=title
	#             print 'title is empty'
	#         if url:    
	#             item['url']=url[0].encode('utf-8')  
	#             print url
	#         else:
	#             item['url']=url
	#         if desc:
	#             item['desc']=desc[0].encode('utf-8')
	#             printcn(desc[0])
	#         else:
	#             item['desc']=desc
	#             print 'desc is empty'
	#         yield item
