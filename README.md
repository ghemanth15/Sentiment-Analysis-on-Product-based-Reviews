# Sentiment-Analysis-on-Product-based-Reviews
### About urls.txt
``` urls.txt ``` file has a default customer review on a product from amazon.com website which can be modified/changed by removing the already existing link to a new link.

### About selector.yml
You will notice in reviews.py that we used a file called ``` selectors.yml ```. Selectorlib(from reviews.py) is a tool that makes selecting, marking up, and extracting data from web pages visual and easy. The Selectorlib Web Scraper Chrome Extension lets you mark data that you need to extract, and creates the CSS Selectors or XPaths needed to extract that data 

### About reviews.py
1.Reads a list of Product Review Pages URLs from a file called urls.txt (This file will contain the URLs for the Amazon product) <br/>
2.Uses a selectorlib YAML file that identifies the data on an Amazon page and is saved in a file called selectors.yml <br/>
3.Scrapes the Data <br/>
4.Saves the data as CSV Spreadsheet called data.csv <br/>

### About sentiment.py
This python file is used to extract data from ``` data.csv ``` file and calculate their polarities.

### Polarities
Polarity, also known as orientation is the emotion expressed in the sentence. It can be positive, neagtive or neutral.Polarity in sentiment analysis refers to identifying sentiment. If polarity is positive, then it is a positive review , if the polairty is negative 
then it is a negative review and if polarity is zero then it is neutral. Polarity ranges from -1 to 1 where -1 represents 
negative comment's maximum polarity and +1 represents positive comment's maximum polarity.

### How to run this project
1. Initially download the following packages: <br/>
``` pip install textblob ``` <br/>
``` pip install selectorlib ``` <br/>
2. Run the reviews.py file. It extracts all the customer reviews on a product into a csv file ('data.csv'). <br/>
3. Run the sentiment.py file. It prints all the reviews on that product and their polarities.
