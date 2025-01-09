# eBay Price Tracker

This project is an **eBay Price Tracker** built in Python. The script scrapes eBay listings for specific products, including their selling prices, sold dates, and other relevant information. The tool helps track historical and ongoing prices for auctions and "Buy It Now" listings.

## Features
- Fetches data for both auction-based and "Buy It Now" listings.
- Tracks key information such as:
  - Product title
  - Sold price
  - Sold date
  - Number of bids (for auctions)
- Supports pagination to scrape data across multiple pages.
- Configurable URLs for specific products or categories.

## Requirements
The script uses the following Python libraries:
- `requests` — For sending HTTP requests to eBay.
- `BeautifulSoup` from `bs4` — For parsing and extracting data from the eBay webpage.
- `pandas` — For potential future data manipulation and saving as CSV (currently unused).

To install the required dependencies:
```bash
pip install requests beautifulsoup4 pandas
```

# How It Works
## URLs for Target Products
The script uses pre-defined URLs for specific products, such as Steam Deck, Ryzen processors, GPUs, and iPhones, to fetch data from eBay.

Example:
```python
sold_auction_url = 'https://www.ebay.com/sch/i.html?_fsrp=1&_from=R40&_nkw=steam+deck&_sacat=0&LH_Sold=1&rt=nc&LH_Auction=1'
sold_buy_now_url_iphone_12 = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Iphone+12&_sacat=0&rt=nc&_odkw=5700xt&_osacat=0&LH_BIN=1&_sop=13&LH_Complete=1&LH_Sold=1'
```

## Functions
``` python
get_data(url): Sends an HTTP GET request to the given URL and parses the response with BeautifulSoup.
get_next_page(soup): Retrieves the URL of the next page of results.
parse_auction_data(soup): Extracts auction-specific data such as product title, sold price, sold date, and bid count.
parse_buy_now_data(soup): Extracts "Buy It Now" specific data such as product title, sold price, and sold date.
```
## Pagination
The script fetches multiple pages of results using the pagination URL provided by eBay.

Example:
``` python
soup = get_data(sold_buy_now_url_iphone_12)
for x in range(4):  # Scrapes 4 pages
    parse_buy_now_data(soup)
    new_page_url = get_next_page(soup)
    soup = get_data(new_page_url)
```
Output
The extracted data is currently printed to the console for debugging and display purposes.

## Example output:
``` python
{'title': 'iPhone 12 128GB', 'sold_price': '650.00', 'sold_date': 'Sold Nov-01-2023'}
```

# How to Run
## Clone the repository:
``` bash
git clone https://github.com/yourusername/ebay-price-tracker.git
cd ebay-price-tracker
```
## Update the target URLs in the script as needed.
## Run the script:
``` bash
python ebay_price_tracker.py
```

# Example Use Case
Suppose you want to track the sold prices of iPhone 12 devices listed as "Buy It Now." Update the URL:
``` python
sold_buy_now_url_iphone_12 = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=Iphone+12&_sacat=0&rt=nc&_odkw=5700xt&_osacat=0&LH_BIN=1&_sop=13&LH_Complete=1&LH_Sold=1'
```
Run the script, and it will output details like:
``` bash
{'title': 'iPhone 12 64GB - Black', 'sold_price': '599.99', 'sold_date': 'Sold Oct-31-2023'}
{'title': 'iPhone 12 Pro 128GB - Silver', 'sold_price': '699.99', 'sold_date': 'Sold Nov-01-2023'}
```
# Future Improvements
Data Export: Save the scraped data to a CSV file for further analysis.
Error Handling: Add robust error handling for missing fields or invalid URLs.
Dynamic URL Input: Allow users to input their own eBay search URLs dynamically.
Graphical Analysis: Integrate data visualization to analyze pricing trends.

# License
This project is licensed under the MIT License.

Feel free to update this README to fit your specific use case or additional features!
