# https://www.rithmschool.com/blog

# Goal : Grab all links from blog
# Data : store URL,anchor tag text and date
import requests
from bs4 import BeautifulSoup
from csv import writer
 
''' make req -> get res as html -> nav thru that -> extract info -> write to csv'''

response = requests.get("https://www.rithmschool.com/blog")

soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("article")

with open("blog_data.csv","w") as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(["title","link","date"])


	for article in articles:
		a_tag = article.find("a")
		#title
		title = a_tag.get_text()
		#url
		url = a_tag['href']
		#date
		date = article.find("time")["datetime"]

		csv_writer.writerow([title,url,date])