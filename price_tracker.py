import requests
from bs4 import BeautifulSoup
import pandas as pd

sold_auction_url = 'https://www.ebay.com/sch/i.html?_fsrp=1&_from=R40&_nkw=steam+deck&_sacat=0&LH_Sold=1&rt=nc&LH_Auction=1'
# Am separating these two because a sold buy now doesn't have bids
sold_buy_now_url_steam_deck = 'https://www.ebay.com/sch/i.html?_fsrp=1&_from=R40&_nkw=steam+deck&_sacat=0&LH_Sold=1&rt=nc&LH_BIN=1'
buy_now_url = 'https://www.ebay.com/sch/i.html?_fsrp=1&_from=R40&_nkw=steam+deck&_sacat=0&rt=nc&LH_BIN=1'
current_auction_url = 'https://www.ebay.com/sch/i.html?_fsrp=1&_from=R40&_nkw=steam+deck&_sacat=0&rt=nc&LH_Auction=1'
# I feel like there should be two different methods for both auction and buy now
# But I want to start with buy now cuz it's easier
sold_buy_now_url_r5_2600 = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=ryzen+5+2600&_sacat=0&LH_Sold=1&LH_Complete=1&rt=nc&LH_BIN=1"
sold_buy_now_url_r5_2600X = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=ryzen+5+2600X&_sacat=0&rt=nc&_odkw=ryzen+5+3600&LH_BIN=1&_sop=13&LH_Complete=1&LH_Sold=1'
sold_buy_now_url_r5_3600 = 'https://www.ebay.com/sch/i.html?_nkw=ryzen+5+3600&_sop=13&LH_Sold=1&LH_Complete=1&rt=nc&LH_BIN=1'
sold_buy_now_url_rx_5700XT = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=5700xt&_sacat=0&LH_BIN=1&_sop=13&rt=nc&LH_Sold=1&LH_Complete=1'
sold_buy_now_url_iphone_12 = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Iphone+12&_sacat=0&rt=nc&_odkw=5700xt&_osacat=0&LH_BIN=1&_sop=13&LH_Complete=1&LH_Sold=1'
def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return(soup)

def get_next_page(soup):
    page = soup.find('a', {'class': 'pagination__next icon-link'})['href']
    return page

def parse_auction_data(soup):
    results = soup.find_all('div', {'class': 's-item__wrapper clearfix'})
    for item in results[2:]:
        product_info = {
            'title': item.find('div', {'class': 's-item__title'}).text,
            'sold_price': item.find('span', {'class': 's-item__price'}).text.replace('$', ''),
            'sold_date': item.find('span', {'class': 's-item__caption--signal POSITIVE'}).text,
            'bids': item.find('span', {'class': 's-item__bids s-item__bidCount'}).text
        }
        print(product_info)
    return

def parse_buy_now_data(soup):
    results = soup.find_all('div', {'class': 's-item__wrapper clearfix'})
    for item in results[2:]:
        product_info = {
            'title': item.find('div', {'class': 's-item__title'}).text,
            'sold_price': item.find('span', {'class': 's-item__price'}).text.replace('$', ''),
            'sold_date': item.find('span', {'class': 's-item__caption--signal POSITIVE'}).text,
        }
        print(product_info['sold_price'])
    return


#soup = get_data(sold_auction_url)
#parse_auction_data(soup)

soup = get_data(sold_buy_now_url_iphone_12)
for x in range(4):
    parse_buy_now_data(soup)
    new_page_url = get_next_page(soup)
    soup = get_data(new_page_url)

print(get_next_page(soup))
# parse_buy_now_data(soup)