import requests
from bs4 import BeautifulSoup

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

"https://www.ebay.com/sch/i.html?_nkw=Iphone+12&_sacat=0&_from=R40&_sop=13&LH_Complete=1&LH_Sold=1&rt=nc&LH_All=1"
"https://www.ebay.com/sch/i.html?_nkw=iphone+12&_sacat=0&_from=R40&_trksid=p4432023.m570.l1313"
"https://www.ebay.com/sch/i.html?_fsrp=1&rt=nc&_from=R40&_nkw=iphone+12&_sacat=0&LH_Sold=1"

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return(soup)

def get_next_page(soup):
    page = soup.find('a', {'class': 'pagination__next icon-link'})
    next_page_link = page.get('href')
    return next_page_link

def parse_data(soup):
    results = soup.find_all('div', {'class': 's-item__wrapper clearfix'})
    for item in results[2:]:
        product_info = {
            'title': item.find('div', {'class': 's-item__title'}).text,
            'sold_price': item.find('span', {'class': 's-item__price'}).text.replace('$', ''),
            # 'sold_date': item.find('span', {'class': 's-item__caption--signal POSITIVE'}).text,
            #'bids': item.find('span', {'class': 's-item__bids s-item__bidCount'}).text
        }
        print(product_info)
    return

item_url = str(input("Enter the ebay url you want to track: "))
while True:
    pagination_num = int(input("Enter the number of pages you want to track: "))
    if pagination_num > 0 and pagination_num < 100:
        break
    else:
        print("Please enter a number greater than 0 and less than 100")
        continue

soup = get_data(item_url)
for x in range(pagination_num):
    parse_data(soup)
    new_page_url = get_next_page(soup)
    soup = get_data(new_page_url)

