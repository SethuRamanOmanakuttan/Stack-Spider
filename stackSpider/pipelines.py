# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# each objects yielded by the parse function of the stackQuestionSpider class
# can be processed using the functions mentioned in the pipeline class
# The process_item function acts as the entry point through which the objects are processed 
from time import sleep
import gspread
from stackSpider.settings import GOOGLE_CREDENTIAL_LOCATION, GOOGLE_SPREADSHEET_NAME

#defining pipeline
class StackspiderPipeline:
    def __init__(self):
        #initialize google drive access and access to google sheet
        drive = gspread.service_account(filename=GOOGLE_CREDENTIAL_LOCATION)
        self.sheet = drive.open(GOOGLE_SPREADSHEET_NAME).sheet1

    #function for halting the execution thread
    def pause_spider(self):
        print("####### SPIDER PAUSEED #######")
        sleep(60)

    #function for joining a list of tags into 
    #comma seperated values
    def join_tags(self,tag_list):
        tags = ",".join(tag_list)
        return tags

    #function to add data to the google sheet
    def add_data_to_sheet(self,item):
        try:
            tags = self.join_tags(item["tags"])
            self.sheet.append_row([item["question"],item["link"],tags])
        except Exception as e:
            #if we encounter "write quota exceeded" error
            if e.args[0]['code'] == 429:
                #halt the spider for a miniute 
                self.pause_spider()
                #retry
                self.add_data_to_sheet(item)        


    def process_item(self, item, spider):
        self.add_data_to_sheet(item)
        return item
