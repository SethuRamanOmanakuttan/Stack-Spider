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
class stackSpiderPipeline:
    def __init__(self):
        #initialize google drive access and access to google sheet
        drive = gspread.service_account(filename=GOOGLE_CREDENTIAL_LOCATION)
        #access the spreadsheet
        workspace = drive.open(GOOGLE_SPREADSHEET_NAME)
        #access the first sheet in the spreadsheet
        self.question_link_sheet = workspace.get_worksheet(0)
        #clears any pre-existing data (optional)
        self.question_link_sheet.clear()
        #the column headers
        sheet0_headers = ["question","link"]
        #add the headers to the first line
        self.question_link_sheet.insert_row(sheet0_headers,index=1)
        #access the second sheet in the spreadsheet
        self.tag_sheet = workspace.get_worksheet(1)
        self.tag_sheet.clear()
        sheet1_headers = ["Tags"]
        self.tag_sheet.insert_row(sheet1_headers,index=1)



    #function for halting the execution thread
    def pause_spider(self):
        print("####### SPIDER PAUSEED #######")
        sleep(60)


    #function coverts a list of items to a list of lists
    # [ a,b,c] -> [[a],[b],[c]]
    def get_list_of_tags(self,tags):
            list_of_tags =[]
            for tag in tags:
                list_of_tags.append([tag])
            return list_of_tags


    #function to add data to the google sheet
    def add_data_to_sheet(self,item):
        try:
            self.question_link_sheet.append_row([item["question"],item["link"]])
            tags = self.get_list_of_tags(item["tags"])
            self.tag_sheet.append_rows(tags)
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