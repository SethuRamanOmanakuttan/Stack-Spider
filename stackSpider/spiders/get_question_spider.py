import scrapy
from stackSpider.settings import BASE_URL,MAX_PAGE_TO_CRAWL, START_URL

#defining the spider
class stackQuestionSpider(scrapy.Spider):
    #name of the spider
    #this will be used to run the crawler
    name = "getQuestionSpider" 
    PAGE_COUNT = 1 #counter to keep track of pages
    start_urls = [START_URL] #the first page to crawl

    
    def parse(self,response):
        #get questions
        for questions in response.css('div.s-post-summary--content'):
            #extract links,question text and tags and return it
            yield {
                "link" : BASE_URL+questions.css('a.s-link').attrib['href'],
                "question":questions.css('a.s-link::text').get(),
                "tags": questions.css('a.post-tag::text').getall()
            }
        #after crawling a page
        # check if the page count exceeded the max number of page to crawl    
        if self.PAGE_COUNT <= MAX_PAGE_TO_CRAWL:
            #if no, get the next page
            next_page = response.css('a[rel="next"]::attr(href)').get()
            if next_page is not None:
                self.PAGE_COUNT += 1
                next_page_url = BASE_URL + next_page
                #start crawling the next page
                yield response.follow(next_page_url,callback=self.parse)
            





