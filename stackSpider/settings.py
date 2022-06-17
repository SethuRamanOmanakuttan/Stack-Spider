
# Setting the parameter of the crawler
# The user can change the values according to the usecase
#delay between page downloads
DOWNLOAD_DELAY = 2
#number of concurrent requests
CONCURRENT_REQUESTS = 1
BOT_NAME = 'stackSpider'

SPIDER_MODULES = ['stackSpider.spiders']
NEWSPIDER_MODULE = 'stackSpider.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

#pipeline
ITEM_PIPELINES = {
   'stackSpider.pipelines.StackspiderPipeline': 300,
}

#number of pages to crawl
MAX_PAGE_TO_CRAWL = 50

#base url of the website
BASE_URL = "https://ethereum.stackexchange.com"

#the page to start the crawl
START_URL = "https://ethereum.stackexchange.com/questions?tab=newest&page=1"

#location of google_credential.json file
GOOGLE_CREDENTIAL_LOCATION = "<location-google-credential-file.json>"

#name of the spreadsheet
GOOGLE_SPREADSHEET_NAME = "<google-sheet-name>"