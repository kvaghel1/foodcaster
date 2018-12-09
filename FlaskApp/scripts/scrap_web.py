from bs4 import BeautifulSoup
import requests

seasons = ["fall","winter","spring","summer","all-year"]
food_list = []
for season in seasons:

	url = "http://www.fruitsandveggiesmorematters.org/whats-in-season-"+season

	#r  = requests.get("http://www.google.com")
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,"html.parser")
	#entry_div_soup = soup.findAll("div", { "class" : "entry" })
	anchors = [p for p in (div.find_all('p')[2] for div in soup.findAll('div',{"class" : "entry"})) if p]
	season_food_list = []
	for a in p.find_all('a'):
		season_food_list.append(str(a.text)) 

	food_list.append(season_food_list)
print food_list