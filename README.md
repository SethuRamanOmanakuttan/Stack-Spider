# STACK-SPIDER
A python-scrapy based web-crawler that crawls through stackExchange pages , retrieves the questions, associated tags and links to the questions and adds it to a user specified google sheet

## Getting Started

### Prerequisites

* python v3.6 (or greater)
* google developer account
  
### Installing The packages

You can use the following command to install all the required python packages
```
pip install -r requirements.txt
```

### Setting up the API

 * Adding data to google sheets requires access to google sheets api. 
 * To enable google sheets api,  you need to setup a google [developer's account](https://developers.google.com/). 
 * In the google developer console, you can set up a new project and enable the API services in that project. Here's how you can do it : [enable API](https://developers.google.com/workspace/guides/enable-apis). 
 * Once you have everything set up , create a service account and download the google credentials in .json format ([Link](https://developers.google.com/workspace/guides/create-credentials#service-account)).
 *  Store the credentials in your system and set the path in the [settings.py](stackSpider/settings.py) file.


## Running the crawler 

To run the crawler, go to the stackSpider folder , open the terminal and execute the following command : 
```
$ scrapy crawl stackSpider
```

You can even write the data to a json file using the follwoing command :
```
$ scrapy crawl stackSpider -O <json-file-name>

```
