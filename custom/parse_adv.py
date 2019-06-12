import requests
import bs4
import re


URL = 'https://premier.ua/prodam-1-kom-iz-kvartiru-zashchitnikov-ukrainy-metro-ul-malinovsk-12259009.html'

response = requests.get(URL)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

info = soup.find_all('table', 'adv_info_table')

tags = re.findall(r'^<td')


print(info)
