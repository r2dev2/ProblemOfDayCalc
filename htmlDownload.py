from bs4 import BeautifulSoup as bs
import requests
import fnc

url = 'http://rkorsunsky.weebly.com/potd-for-calculus.html'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content
soup = bs(html, 'html.parser')
neat = soup.prettify()

fnc.init("htmlSource.txt")

source = open("htmlSource.txt", "w")
source.write(str(neat))
source.close()
