# eBay Price Tracker

This project is an **eBay Price Tracker** built in Python. The script scrapes **historical** eBay listings for specific products and prices. The tool helps track historical prices for auctions and "Buy It Now" listings to help you make a more informed decision based on price trends.

<br />
<br />

## Features
- Fetches data for **historical** auction-based and "Buy It Now" listings.
- Tracks key information such as:
  - Product title
  - Sold price
- Supports pagination to scrape data across multiple pages.

<br />
<br />

## Requirements
The script uses the following Python libraries:
- `requests` — For sending HTTP requests to eBay.
- `BeautifulSoup` from `bs4` — For parsing and extracting data from the eBay webpage.

<br />
<br />

## 🚀 How to Run the eBay Price Tracker

Follow these steps to set up and run the project:

### 1️⃣ Clone the Repository
First, download the project from GitHub:
```bash
git clone https://github.com/Tk7TBG/Ebay-Price-Tracker.git
cd Ebay-Price-Tracker
```

### 2️⃣ Create a Virtual Environment
To keep dependencies isolated, create a virtual environment:
```bash
python3 -m venv venv
```

### 3️⃣ Activate the Virtual Environment
On macOS & Linux:
```bash
source venv/bin/activate
```
On Windows (CMD):
```bash
venv\Scripts\activate.bat
```
On Windows (PowerShell):
```powershell
venv\Scripts\Activate.ps1
```

### 4️⃣ Install Required Dependencies
After activating the virtual environment, install the necessary packages:
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Script
Once everything is set up, execute the script inside the virtual environment:
```bash
python price_tracker.py
```


<br />
<br />

## 1. Current Listings

[Regular search.webm](https://github.com/user-attachments/assets/e4a789ee-88e2-4ada-b491-d4dd2a62f59c)

<br />


## 2. Filter by historical Listings

[Filter by ended.webm](https://github.com/user-attachments/assets/dd0f3d77-0c39-4958-a01f-347937d48ebb)

<br />

### Paste the URL in the prompt
[script demo.webm](https://github.com/user-attachments/assets/411aae73-4990-4410-bdba-7821a54bcb68)

Remember to paste with `Ctrl + Shift + v` in the terminal/cmd
<br />
<br />

# Future Improvements
Use statistics to filter out extreme outliers to make data more true

Data Export: Save the scraped data to a CSV file for further analysis.

Error Handling: Add robust error handling for missing fields or invalid URLs.

Graphical Analysis: Integrate data visualization to analyze pricing trends.

<br />

# License
This project is licensed under the MIT License.

