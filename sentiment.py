import csv
from textblob import TextBlob

infile = 'data.csv'

lists = []

with open(infile, 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
    	if any(row):
        	print(row[0])
        	lists.append(row[0])

for each_review in lists:
   	blob = TextBlob(each_review)
   	print(blob.sentiment.polarity)
	
		

