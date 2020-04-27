



#Author : DIVS TECH

import requests
from bs4 import BeautifulSoup
country=input("Enter Your Country Name:")
url="https://www.worldometers.info/coronavirus/country/{}/".format(country)
r=requests.get(url)
s=BeautifulSoup(r.text,"html.parser")
data=s.find_all("div",class_="maincounter-number")

print("Total Cases : ",data[0].text.strip())
print("Total Deaths : ",data[1].text.strip())
print("Total Recovered : ",data[2].text.strip())