import requests
from bs4 import BeautifulSoup

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

