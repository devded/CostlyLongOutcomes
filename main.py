
import time
from bs4 import BeautifulSoup
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

url = "https://www.henleyglobal.com/passport-index/ranking"

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get(url)

time.sleep(10)
browser.execute_script("window.scrollTo(0, 10000);")
html = browser.page_source
soup = BeautifulSoup(html, "html.parser")
country_list = soup.find_all('div', attrs={'class': 'country-container'})

list = soup.find_all('div', attrs={'class': 'row-ranking'})

n=2
rank_list = []
for x in list:
  #print(x.div[1])
  #print(x.select("div:nth-child("+str(n)+")")[0])
  rank_list.append(x.select("div:nth-child("+str(n)+")")[0])


for rank_value in rank_list:
  print(rank_value)

#print(country_list)
# for country_name in country_list:
#   #print(country_name.p.text)
#   print(country_name.div.img.attrs['src'])




# raw_names = soup.find_all('div', attrs={'class': 'product-content-info'})
# # links = soup.find_all('a', attrs={'class': 'udlite-custom-focus-visible'})
# # ratings = soup.find_all('span', attrs={'class': 'udlite-heading-sm'})
# # descrptions = soup.find_all('p', attrs={'class': 'udlite-text-sm'})
# #browser.quit()
# raw_prices = soup.find_all('span', attrs={'class': 'price'})

# # print(raw_prices)

# clean_names = []
# clean_urls = []
# clean_prices = []

# for name in raw_names:
#     # print(name.a.text.strip())
#     # print(name.a.attrs['href'])
#     clean_names.append(name.a.text.strip())
#     clean_urls.append(name.a.attrs['href'])

# for price in raw_prices:
#     # print(price.text.strip())
#     clean_prices.append(price.text.strip())

# data_list = []

# for name, price, url in zip(clean_names, clean_prices, clean_urls):
#     data_format = {
#         "product_name": name,
#         "product_price": price,
#         "product_url": url,
#     }
#     data_list.append(data_format)



# print(data_list)
