#Import Libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import urllib.parse

website = "https://www.laptopsdirect.co.uk/ct/laptops-and-netbooks/laptops?fts=laptops"
response = requests.get(website)
response.status_code
# Soup Object
soup = BeautifulSoup(response.content, "html.parser")
results = soup.findAll("div", {"class": "OfferBox"})
print(results)

# Name
name = results[0].find("a", {"class": "offerboxtitle"}).get_text()

# Price
price = results[0].find("span", {"class": "offerprice"}).get_text()

#Review Rating
review_rating = results[0].find("star-rating").get("rating-value")
print(review_rating.strip())