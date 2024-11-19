# Stock API Python - Technical Specification

**Version**: 3.0  
**Author**: FCS API Team

---

## Overview
**FCS Stock API Python** provides access to real-time stock financial market data, indices, company profiles, dividend information, historical prices, and technical indicators. This API is designed for users seeking reliable and frequent stock price updates and analytics through Python.
Fetching stock exchange ange data in Python can be done using libraries like FCS API.

## System Requirements

- **Programming Language**: Python 3.6 or later
- **Dependencies**: External libraries listed in the `requirements.txt` file
- **API Key**: Access to the API requires an API key, available upon registration at the [FCS API Dashboard](https://fcsapi.com/dashboard).

## Python Stock API Installation 

### Step 1: Clone Repository
The first step is to clone the repository from GitHub.

```bash
# Clone the repository
git clone <repository_url>
cd FCS_Stock
```

### Step 2: Install Dependencies
Navigate to the project folder and install the required libraries.

```bash
pip install -r requirements.txt

```
### Step 3: Set Up API Key
Obtain an API key from the FCS API dashboard. Insert the key into your Python script to authenticate API requests.

  ```python
from fcs_forex import FCSForex

# Initialize with your API key
forex_api = FCSForex(api_key='YOUR_API_KEY')

stock_latest_price=stock_api.get_stock_Latest_price(symbol='AAPL',exchange='nasdaq,mexico')

print("stock_latest_price:", stock_latest_price)

  ```

## API Response Format
The default response format is JSON.

```python
OUTPUT:
{
  "status": true,
  "code": 200,
  "msg": "Successfully",
  "response": [
    {
      "c": "225",
      "h": "226.92",
      "l": "224.27",
      "ch": "-3.22",
      "cp": "-1.41%",
      "t": "1731704399",
      "s": "AAPL",
      "cty": "united-states",
      "ccy": "USD",
      "exch": "NASDAQ",
      "id": "15",
      "tm": "2024-11-15 20:59:59"
    },
    {
      "c": "4588",
      "h": "4638",
      "l": "4565.01",
      "ch": "-73.23",
      "cp": "-1.57%",
      "t": "1731704399",
      "s": "AAPL",
      "cty": "mexico",
      "ccy": "MXN",
      "exch": "Mexico",
      "id": "107838",
      "tm": "2024-11-15 20:59:59"
    }
  ],
  "info": {
    "exchanges": [],
    "sectors": [],
    "server_time": "2024-11-18 08:22:56 UTC",
    "credit_count": 1
  }
}
  ```


## Stock API Python - Methods

### 1. Stock Indices API

- **What it Does**:  
  You can retrieve a complete list of supported indices for any country of your choice. API. Simply provide the country name of the indices to get the full list of indices for that country.

- **How to Use**:

  ```python
     stocks_indices = stock_api.get_stocks_indices(country="japan,turkey")
     stocks_indices = stock_api.get_stocks_indices(country="United-states")
     print("Stock List:", stocks_indices)

     Response:
     { 
      "index_id": "1",   
      "index_name": "Dow Jones",
      "full_name": "Dow Jones Industrial Average",
      "country": "united-states"
     },
     {
      "index_id": "2",
      "index_name": "Nasdaq 100",
      "full_name": "Nasdaq 100",
      "country": "united-states"
     }, 
     { 
      "index_id": "3",
      "index_name": "Nasdaq",
      "full_name": "NASDAQ Composite",
      "country": "united-states"
     }, 
     {and more}

  ```

### 2. Stock List

- **What it Does**:  
  Fetch a list of stocks by specifying either a valid country name or an indices_id (which will ignore the country). You can also optionally filter by sector (e.g., technology, construction) and exchange (e.g., NYSE, BSE, JPX, Nasdaq, NSE 
  Moscow Exchange (MOEX) – Russia
  Deutsche Börse (Frankfurt Stock Exchange) – Germany
  Toronto Stock Exchange (TSX) – Canada
  Bombay Stock Exchange (BSE) - India
  National Stock Exchange (NSE) - India
  Saudi Stock Exchange - (Tadawul)
  etc...
  ).

- **How to Use**:

  ```python
    stock_list = stock_api.get_stocks_list(country="japan,turkey")
    stock_list = stock_api.get_stocks_list(sector="services,energy",country="japan,turkey")
    stock_list = stock_api.get_stocks_list(exchange='nyse,nasdaq,NYSE')
    print("Stock List:", stock_list)

    Response: 
    {
    "0": 
    {
      "id": "1",
      "name": "Boeing",
      "short_name": "BA",
      "country": "united-states", 
      "ccy": "USD",
      "exch": "NYSE", 
      "sector": "Industrials"
    },
    "1":
    {
      "id": "2",
      "name": "Chevron", 
      "short_name": "CVX",
      "country": "united-states", 
      "ccy": "USD",
      "exch": "NYSE",
      "sector": "Energy"
    },
    "2":
    {
      "id": "3",
      "name": "Caterpillar",
      "short_name": "CAT",
      "country": "united-states",
      "ccy": "USD",
      "exch": "NYSE",
      "sector": "Capital Goods"
    },
    } 
    {and more}

  ```

### 3. Stock Latest Price API 

- **What it Does**:  
  Retrieve stock information using a valid stock ID or symbol. If you provide an indices_id, it will override the ID and symbol parameters. Similarly, specifying a country will ignore the ID and symbol, returning all stocks for that country. You can also filter by exchange (e.g., NYSE) and sector (e.g., technology).

- **How to Use**:

  ```python
    stock_latest_price=stock_api.get_stock_Latest_price(country="japan,turkey")
    stock_latest_price=stock_api.get_stock_Latest_price(exchange='nyse,nasdaq,pari')
    stock_latest_price=stock_api.get_stock_Latest_price(id='1,2,3,4,5')
    stock_latest_price=stock_api.get_stock_Latest_price(symbol='AMD,AAPL,MSFT,FB')
    stock_latest_price=stock_api.get_stock_Latest_price(country='united-states',exchange='NYSE')
    stock_latest_price=stock_api.get_stock_Latest_price(symbol='AAPL',exchange='nasdaq,mexico')
    print("stock_latest_price:", stock_latest_price)

    'response': 
    [{
      'c': '225',
      'h': '226.92', 
      'l': '224.27', 
      'ch': '-3.22', 
      'cp': '-1.41%', 
      't': '1731704399', 
      's': 'AAPL', 
      'cty': 'united-states', 
      'ccy': 'USD', 
      'exch': 'NASDAQ', 
      'id': '15', 
      'tm': '2024-11-15 20:59:59'
    },
    {
      'c':'4588', 
      'h': '4638',
      'l': '4565.01', 
      'ch': '-73.23', 
      'cp': '-1.57%', 
      't': '1731704399', 
      's': 'AAPL', 
      'cty': 'mexico', 
      'ccy': 'MXN', 
      'exch': 'Mexico', 
      'id': '107838', 
      'tm': '2024-11-15 20:59:59'
    }],
  
  ```

### 4. Get Indices Latest Data

- **What it Does**:  
Fetch one or multiple indices prices at the same time. You can either provide an id to get a specific indices or a country to get all indices for that country (overriding id if specified).

- **How to Use**:

  ```python
    indices_latest_price=stock_api.get_indices_latest(id='1')
    indices_latest_price=stock_api.get_indices_latest(id='1,2')
    indices_latest_price=stock_api.get_indices_latest(country="japan,turkey")

    print("stock_latest_price:", indices_latest_price)

    Response:  
    {
    'c': '38232.50',
    'h': '38561.00', 
    'l': '38137.00', 
    'ch': '-405.00', 
    'cp': '-1.05%', 
    't': '1731911401', 
    'name': 'Nikkei 225', 
    'cty': 'japan', 
    'id': '268', 
    'tm': '2024-11-18 06:30:01'
    },{and more}

  ```

### 5. Historical Data

- **What it Does**:  
The code fetches stock data using parameters like id (stock ID), symbol (stock short name), and period (timeframe). You can specify a date range with from and to for historical data or omit them for the latest data. The level parameter determines the number of data points: 1 for 300 candles, 2 for 600, and 3 for 900 candles..

- **How to Use**:

  ```python
    history_data = stock_api.get_history({
        'id': '10',
        'period': '1d',
        'level': 1,
        'from': '2024-10-30',
        'to': '2024-10-31'
    })
    print("History Data for countries:", history_data)

    history_data = stock_api.get_history({
        'indices_id': '1',
        'period': '1d',
        'from': '2024-10-30',
        'to': '2024-10-31'
    })
    print("History Data for countries:", history_data)

    history_data = stock_api.get_history({
        'id': '3',
        'period': '1h'
    })
    print("History Data for countries:", history_data)

    Response:
    
    "1730246400":
    {
      "o":"42249.808594",
      "h":"42457.921875",
      "l":"42141.539063",
      "c":"42141.539063",
      "v":"377428512",
      "t":1730246400,
      "tm":"2024-10-30 00:00:00"
    },{and more}
 
  ```

### 6. Dividend Information

- **What it Does**:  
The code retrieves stock data using id (stock ID), symbol (stock short name). These inputs provide access to specific stock information securely.

- **How to Use**:

  ```python
    stock_dividend=stock_api.stock_dividend(id='1')
    stock_dividend=stock_api.stock_dividend(id='1,2')
    stock_dividend=stock_api.stock_dividend(symbol="AAPL")

    print("stock dividend:", stock_dividend)

  ```

### 7. Get Stock Profile

- **What it Does**:  
Retrieve complete company details, including address, number of employees, equity type, sector, and country of origin. To achieve this, just add the FCS API's stock symbols/IDs parameter to your API request and assign it one or more comma-separated symbols/IDs.

- **How to Use**:

  ```python
    stock_profile=stock_api.get_profile(id='1')
    stock_profile=stock_api.get_profile(id='1,2')
    stock_profile=stock_api.get_profile(symbol="TSLA")

    print("stock dividend:", stock_profile)
  ```

### 8. Get Stock Performance

- **What it Does**:  
  Get stock performance, when and how much stock price performs, based on parameters like stock id, symbol, country, indices_id, index_id, exchange, and sector to customize the request.

- **How to Use**:

  ```python
    performance = stock_api.get_performance(country='germany',sector='technology')
    performance = stock_api.get_performance(sector="services,energy")
    performance = stock_api.get_performance(exchange='nyse,nasdaq,pari')
    performance = stock_api.get_performance(indices_id='1,2,3')
    print("performance:", performance)

  ```

### 9. Get Stock Fundamentals

- **What it Does**:  
  Get stock fundamental to track stock performance for screening, customized based on parameters such as stock ID, symbol, country, indices ID, index ID, exchange, and sector.

- **How to Use**:

  ```python
    fundamental = stock_api.get_fundamental(country='germany',sector='technology')
    fundamental = stock_api.get_fundamental(sector="services,energy")
    fundamental = stock_api.get_fundamental(exchange='nyse,nasdaq,pari')
    fundamental = stock_api.get_fundamental(indices_id='1,2,3')
    print("fundamental:", fundamental)
  ```

### 10. Get Stock Finance

- **What it Does**:  
It provides access to both current and historical data on a stock's income, balance sheet, and cash flow.

Below are examples of 4 different API request URLs.

Note: These APIs do not support multiple IDs as parameters in the URL. Please include only one ID or symbol name per API request.

- **How to Use**:

  ```python
    #get stock income
    stock_income = stock_api.stock_income(id='1')
    stock_income = stock_api.stock_income(id='1',duration='interim')
    print("Stock Income:", stock_income)
    
    #get stock cash
    stock_cash = stock_api.stock_cash(id='1')
    stock_cash = stock_api.stock_cash(id='1',duration='interim')
    print("Stock Income:", stock_cash)
    
    #get stock balance
    stock_balance = stock_api.stock_balance(id='1')
    stock_balance = stock_api.stock_balance(id='1',duration='interim')
    print("Stock Income:", stock_balance)

    #get stock earning
    #Earning does not support duration parameter
    stock_earning = stock_api.stock_earning(id='1')
    print("Stock Income:", stock_earning)
  ```
### 11. Get Pivot Points

- **What it Does**:  

  A pivot point is the average of important prices from the previous trading period on an exchange. Get response By using parameters like  id, symbol, and period to define time frame.

- **How to Use**:

  ```python
    pivot_points = stock_api.get_pivot_points(id="4", period='1d')
    pivot_points = stock_api.get_pivot_points("IBM", '1d')
    print("Pivot Points:", pivot_points)


### 12. Get Moving Averages API

- **What it Does**:  
Moving Average (MA) is a trend indicator that uses values from previous candles (such as 5, 10, 20, 50, 100, 200) to assess the market value. Fetch response By using parameters like  id, symbol, and period to define time frame.

- **How to Use**:

  ```python
    moving_averages = stock_api.get_moving_averages(id="4", period='1d')
    moving_averages = stock_api.get_moving_averages(symbol="IBM", period='1d')
    print("Moving Averages:", moving_averages)
  ```

### 13. Technical Indicators API - Python

- **What it Does**:  
  Technical indicators are calculated using popular stock indicators like MA, RSI, STOCH, ATR, and others. Retrieve response By using parameters like  id, symbol, and period to define time frame.

- **How to Use**:

  ```python
    indicators = stock_api.get_technical_indicator('7', '1d')
    indicators = stock_api.get_technical_indicator(symbol="IBM,AV", period='1d')
    print("Technical Indicators:", indicators)

  ```

### 14. Get Stock Signals Indicator

- **What it Does**:  
  This setup lets you retrieve stock data using parameters like id (stock ID), symbol (stock short name), country (for all stocks from a specific country), indices_id (for all stocks from an index), and index_id (for data from a specific index).

- **How to Use**:

  ```python
    signals_indicator = stock_api.get_signals_indicator(symbol="TSLA,MSFT,FB")
    signals_indicator = stock_api.get_signals_indicator(id='1,2,3,4,5')
    signals_indicator = stock_api.get_signals_indicator(country='germany')
    print("Technical Indicators:", signals_indicator)
  ```


### 15. Search for Stocks

- **What it Does**:  
 This allows you to search using the s parameter (search query), strict (0 for any word or 1 for all words), and type (either index, stock, or both). These options help refine the search for specific stock or index data.

- **How to Use**:

  ```python
    search_results = stock_api.get_search_query("General Electric")
    search_results = stock_api.get_search_query(search='eneral Electric',strict=0, type='index')
    print("Search Results: ", search_results)
  ```

### 16. Get Country Report

- **What it Does**:  
  Retrieve a detailed report on each country, including the number of stocks in each country, exchange, and sector.

- **How to Use**:

  ```python
    country_report = stock_api.get_country_report()  # Get the country economic report
    print(country_report)

## Other Resources:

- **Forex Live Prices with PHP Socket**: [Github Real-Time Prices](https://github.com)
- **Forex JS WebSocket**: [FCSAPI Socket API](https://fcsapi.com/document/socket-api)
- **Python Library**: [Forex API Python](https://github.com/fcsapi/Forex-API-Python)
- **NodeJS Library**: [Forex API Node JS](https://github.com/fcsapi/forex-api-node-js)
- **PHP Library**: [Forex API PHP](https://github.com/fcsapi/Forex-API-PHP)

### Support

## Support and Contact

For any assistance, reach out to us via email at [support@fcsapi.com](mailto:support@fcsapi.com) or connect with us through our [Live Chat](https://fcsapi.com).


### License and Terms

The **FCS Stock API** is provided under the MIT license and is also governed by FCS's privacy policy, terms, and conditions.