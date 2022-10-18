from bs4 import BeautifulSoup
import urllib3
from tqdm import tqdm

url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
theurl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(theurl, "lxml")

i = 0

movies = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
for div_item in tqdm(movies):
    div = div_item.find('div', attrs={'class': 'lister-item-content'})
    header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
    print(str(i) + '.''Movie: ' +
          str((header[0].findChildren('a'))[0].contents[0]))
    i += 1
