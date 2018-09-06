import bs4
import requests
para= [('q','foss@amrita')]
url= "https://google.com/search"
result= requests.get(url=url,params=para)
extract=bs4.BeautifulSoup(result.text,'lxml')
titles=extract.find_all("h3")
x=0
for title in titles:
	x=x+1
	print(title.get_text())
	
