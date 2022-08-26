# import time
# import mechanicalsoup

# browser = mechanicalsoup.Browser()

# page = browser.get("https://www.ryanscomputers.com/search?q=mac")
# test = page.soup.find("div", class_="special-price")
# print(test)
# time.sleep(10)

import time
from bs4 import BeautifulSoup
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# url = "http://legendas.tv/busca/walking%20dead%20s03e02"

# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# browser.get(url)
# html = browser.page_source
# soup = BeautifulSoup(html, 'lxml')
# a = soup.find('section', 'wrapper')
# print(a)
# #browser.quit()

url = "https://cutt.ly/RE8gqpQ"

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get(url)

time.sleep(5)
browser.execute_script("window.scrollTo(0, 10000);")
html = browser.page_source
soup = BeautifulSoup(html, "html.parser")
raw_names = soup.find_all('div', attrs={'class': 'product-content-info'})
# links = soup.find_all('a', attrs={'class': 'udlite-custom-focus-visible'})
# ratings = soup.find_all('span', attrs={'class': 'udlite-heading-sm'})
# descrptions = soup.find_all('p', attrs={'class': 'udlite-text-sm'})
#browser.quit()
raw_prices = soup.find_all('span', attrs={'class': 'price'})

# print(raw_prices)

clean_names = []
clean_urls = []
for name in raw_names:
    # print(name.a.text.strip())
    # print(name.a.attrs['href'])
    clean_names.append(name.a.text.strip())
    clean_urls.append(name.a.attrs['href'])

clean_prices = [price.text.strip() for price in raw_prices]
data_list = []

for name, price, url in zip(clean_names, clean_prices, clean_urls):
    data_format = {
        "product_name": name,
        "product_price": price,
        "product_url": url,
    }
    data_list.append(data_format)



print(data_list)
