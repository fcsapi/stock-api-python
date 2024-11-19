import requests # Library to handle HTTP requests

class FcsStock:
    def __init__(self, api_key=''):
        # Set the API key, defaulting to "API_KEY" if not provided
        self.api_key = api_key if api_key else "API_KEY"
        self.output = ''  # default is json
        self.output_type = 'JSON'  # Default output type JSON
        self.basic_url = "https://fcsapi.com/api-v3/stock"
        self.api_message = "API Key is empty, please set your API Key."


    def return_error(self, msg):
        # Returns a standardized error message in a dictionary format
        return {"status":False,"msg":msg,"Error":"Code or input data error"}
    

    def check_api_key(self):
        """Check if the API key is valid."""
        return self.api_key is not None and self.api_key != 'api_key'
    
    
    def response(self, url, params):
        """Make a request to the given URL and return the JSON response."""
        
        if not self.check_api_key():
            return self.return_error(self.api_message)
        
        if self.api_key:
            params['access_key'] = self.api_key
        if self.output:
            params['output'] = self.output

        response = requests.post(url, data=params)

        # Check if response is JSON
        try:
            response_data = response.json()
            return response_data  # Return JSON data without prettifying
        except ValueError:
            # If response is not JSON, return it as is
            return self.return_error(response.text)

    
    """"
    Return all stock indices for the given country.
    Args: 
        country (str): The country code.
    Return:
        all stock indices for the given country.
    """
    def get_stocks_indices(self, country): 
        """Return all stock indices for the given country."""
        
        # Check if country parameter is not empty
        if not country:
            return self.return_error("Country parameter is required")
        
        # Prepare the parameters for the request
        params = {'country': country}
        
        # Construct the API endpoint URL
        link = f"{self.basic_url}/indices"

        # Make the request and return the response
        return self.response(link, params)

    """
    Get stock list based on country, indices_id, sector, and exchange.
    Args:
        # country (str): The country code.
        # indices_id (str): The indices ID.
        # sector (str): The sector name.
        # exchange (str): The exchange name.
    Returns:
        dict: The JSON response containing stock list or an error message.    
    """
    def get_stocks_list(self, country='', indices_id='', sector='', exchange=''):
        """Get base p based on country, indices_id, sector, exchange."""
        
        if not self.check_api_key():
            return self.return_error(self.api_message)

        # Prepare parameters based on the input
        params = {}
        
        # If country or indices_id is provided, include them in the parameters
        if country:
            params['country'] = country
        if indices_id:
            params['indices_id'] = indices_id
        
        # Optional parameters
        if sector:
            params['sector'] = sector
        if exchange:
            params['exchange'] = exchange

        # Validate that at least one of country or indices_id is provided
        if not any([country, indices_id, sector, exchange]):
            return self.return_error("Enter at least one parameter ")

        # Construct the API link
        link = f"{self.basic_url}/list"
        
        # Call the response method, assuming it handles the access_key internally
        return self.response(link, params)
    
    
    """
    Get the latest stock prices.
    Args:
        # id (str): The stock ID.
        # symbol (str): The stock symbol.
        # country (str): The country code.
        # indices_id (str): The indices ID.
        # sector (str): The sector name.
        # exchange (str): The exchange name.
    Returns:
        dict: The JSON response with the latest prices or an error message.
    """
    def get_stock_Latest_price(self, id='',symbol='',country='', indices_id='', sector='', exchange=''):
        """Get base prices based on country, indices_id, sector, exchange."""
        
        if not self.check_api_key():
            return self.return_error(self.api_message)

        # Prepare parameters based on the input
        params = {}
        
        if id:
            params['id'] = id
        if symbol:
            params['symbol'] = symbol
        # If country or indices_id is provided, include them in the parameters
        if country:
            params['country'] = country
        if indices_id:
            params['indices_id'] = indices_id
        
        # Optional parameters
        if sector:
            params['sector'] = sector
        if exchange:
            params['exchange'] = exchange

        # Validate that at least one of country or indices_id is provided
        if not any([id,symbol,country, indices_id, sector, exchange]):
            return self.return_error("Enter at least one parameter ")

        # Construct the API link
        link = f"{self.basic_url}/latest"
        
        # Call the response method, assuming it handles the access_key internally
        return self.response(link, params)
    
    """
    Get the latest stock indices data.
    Args:
        # country (str): The country code.
        # id (str): The stock indices ID.
    Returns:
        dict: The JSON response with the latest indices data or an error message.
    """
    def get_indices_latest(self,country='',id=''):
        if not self.check_api_key():
            return self.return_error(self.api_message)
        
        params={}
        if country:
           params['country']=country 
        elif id:
            params['id']=id
        
        if not country and not id:
            return self.return_error("country or id is missing")
        
        link=f"{self.basic_url}/indices_latest"
        return self.response(link,params)
    
    """
    Get historical data for a specific stock or index.
    Args:
        data (dict): A dictionary containing:
            - id (str): The stock ID.
            - symbol (str): The stock symbol.
            - indices_id (str): The indices ID.
            - period (str): The historical period ('1h', '4h', '1d', etc.). Defaults to '1h'.
            - level (int): The level of detail (1, 2, or 3). Defaults to 1.
            - from (str): The start date (format 'YYYY-MM-DD').
            - to (str): The end date (format 'YYYY-MM-DD').
    Returns:
        dict: The JSON response with historical data or an error message.
    """
    def get_history(self, data):
        """Get specific currency history data."""
        id      = data.get('id', '')
        symbol  = data.get('symbol', '')
        indices_id=data.get('indices_id','')

        period  = data.get('period', '1h')
        level   = data.get('level', 1)
        if (level < 1 or level > 3) : level = 1
   
        from_date = data.get('from', '')
        to_date = data.get('to', '')

        if not any([id, indices_id, symbol]):
            return self.return_error("enter atleat any of them (id, indices_id, symbl ")

        params = {
            'period': period,
            'limit': level
        }
        if id: 
            params['id'] = id
        elif symbol:
            params['symbol'] = symbol
        elif indices_id:
            params['indices_id']=indices_id

        if from_date and to_date:
            params['from'] = from_date
            params['to'] = to_date

        link = f"{self.basic_url}/history"
        return self.response(link, params)

    """
    Fetch stock information for 'dividend' or 'profile' based on the endpoint.
    Args:
        # endpoint (str): The endpoint to query ('dividend' or 'profile').
        # symbol (str): The stock symbol.
        # id (str): The stock ID.
    Returns:
        dict: The JSON response with stock profile data or an error message.
    """
    def get_stock_profile(self, endpoint, symbol='', id=''):
        """Fetch stock information for either 'dividend' or 'profile' based on the endpoint."""
        
        if not self.check_api_key():
            return self.return_error(self.api_message)

        # Prepare parameters based on the input
        params = {}
        
        if id:
            params['id'] = id
        elif symbol:
            params['symbol'] = symbol

        # Validate that either symbol or id is provided
        if not symbol and not id:
            return self.return_error("country or id is missing")

        # Construct the API link using the provided endpoint
        link = f"{self.basic_url}/{endpoint}"
        return self.response(link, params)

    # Wrapper functions for Dividend and Profile endpoints
    def stock_dividend(self, **kwargs):
        return self.get_stock_profile('dividend', **kwargs)

    def get_profile(self, **kwargs):
        return self.get_stock_profile('profile', **kwargs)


    """
    Get data for 'performance' or 'fundamental' endpoints.
    Args:
       # endpoint (str): The endpoint to query ('performance' or 'fundamental').
       # id (str): The stock ID.
       # symbol (str): The stock symbol.
       # country (str): The country code.
       # indices_id (str): The indices ID.
       # index_id (str): The index ID.
       # sector (str): The sector name.
       # exchange (str): The exchange name.
    Returns:
        dict: The JSON response with data or an error message.
    """
    def get_data(self, endpoint, id='', symbol='', country='', indices_id='', index_id='', sector='', exchange=''):
        """Get data based on various parameters for either 'performance' or 'fundamental' endpoints."""
        if not self.check_api_key():
            return self.return_error(self.api_message)

        # Prepare parameters based on the input
        params = {}
        
        if id:
            params['id'] = id
        elif index_id:
            params['index_id'] = index_id
        elif symbol:
            params['symbol'] = symbol
        elif indices_id:
            params['indices_id'] = indices_id
        
        if country:
            params['country'] = country
        if sector:
            params['sector'] = sector
        if exchange:
            params['exchange'] = exchange

        # Validate that at least one parameter is provided
        if not any([id, symbol, country, indices_id, index_id, sector, exchange]):
            return self.return_error("Enter at least one parameter")

        # Construct the API link based on the endpoint provided
        link = f"{self.basic_url}/{endpoint}"
        return self.response(link, params)

# Performance and Fundamental Functions
    def get_performance(self, **kwargs):
        return self.get_data('performance', **kwargs)

    def get_fundamental(self, **kwargs):
        return self.get_data('fundamental', **kwargs)
    
    """
    Get stock financial data (income, cash, balance, earning).
    Args:
        # symbol (str): The stock symbol.
        # id (str): The stock ID.
        # duration (str): The duration ('annual' or 'interim'). Defaults to 'annual'.
    Returns:
        dict: The JSON response with financial data or an error message.
    """    
    def _stock_finance_common(self, endpoint, symbol='', id='', duration='annual'):
        if not self.check_api_key():
            return self.return_error(self.api_message)
        
        params = {}
        if id:
            params['id'] = id  
        elif symbol:
            params['symbol'] = symbol
        
        # Validate duration
        if duration not in ["annual", "interim"]:
            duration = "annual"
        
        if duration:
            params['duration'] = duration
        
        # Ensure either symbol or id is provided
        if not symbol and not id:
            return self.return_error("symbol or id is missing")
        
        # Construct the API link based on the endpoint
        link = f"{self.basic_url}/{endpoint}"
        return self.response(link, params)

    def stock_income(self, symbol='', id='', duration='annual'):
        return self._stock_finance_common('income', symbol, id, duration)

    def stock_cash(self, symbol='', id='', duration='annual'):
        return self._stock_finance_common('cash', symbol, id, duration)

    def stock_balance(self, symbol='', id='', duration='annual'):
        return self._stock_finance_common('balance', symbol, id, duration)
    
    def stock_earning(self, symbol='', id='', ):
        return self._stock_finance_common('earning', symbol, id)



    """
    Get technical signals for a stock.
    Args:
        # endpoint (str): The endpoint to query ('pivot_points', 'ma_avg', etc.).
        # id (str): The stock ID.
        # symbol (str): The stock symbol.
        # period (str): The period for the signal ('1h', '4h', '1d', etc.). Defaults to '1h'.
    Returns:
        dict: The JSON response with signal data or an error message.
    """
    def get_signal(self,endpoint,id='',symbol='',period='1h'):
        if not symbol and not id:
            return self.return_error("Symbol or Id not defined")

        if len(id.split()) > 1:
            return self.return_error("Signals API only accepts a single id")

        params = {}
        if id:
            params['id']=id
        elif symbol:
            params['symbol']=symbol
        
        if period:
            params['period']=period

        link = f"{self.basic_url}/{endpoint}" 
        return self.response(link, params)


    def get_pivot_points(self, **kwargs):
        """Get pivot points."""
        return self.get_signal("pivot_points",**kwargs)

    def get_moving_averages(self, **kwargs):
        """Get moving averages forex."""
        return self.get_signal("ma_avg", **kwargs)

    def get_technical_indicator(self, **kwargs):
        """Get top indicators signals."""
        return self.get_signal("indicators",**kwargs)
    
    """
    Get technical signals based on various parameters.
    Args:
        # id (str): The stock ID.
        # symbol (str): The stock symbol.
        # country (str): The country code.
        # indices_id (str): The indices ID.
        # index_id (str): The index ID.
    Returns:
        dict: The JSON response with signals data or an error message.
    """    
    def get_signals_indicator(self, id='', symbol='', country='', indices_id='', index_id=''):
        """Get data based on various parameters for either 'performance' or 'fundamental' endpoints."""
        if not self.check_api_key():
            return self.return_error(self.api_message)

        # Prepare parameters based on the input
        params = {}
        
        if id:
            params['id'] = id
        elif index_id:
            params['index_id'] = index_id
        elif symbol:
            params['symbol'] = symbol
        elif indices_id:
            params['indices_id'] = indices_id
        
        if country:
            params['country'] = country

        # Validate that at least one parameter is provided
        if not any([id, symbol, country, indices_id, index_id]):
            return self.return_error("Enter at least one parameter")

        # Construct the API link based on the endpoint provided
        link = f"{self.basic_url}/technicals"
        return self.response(link, params)
    """
    Perform a search query on stocks.
    Args:
        # search (str): The search term.
        # strict (int): The strictness level (0 or 1). Defaults to 0.
        # type (str): The type of asset ('stock', 'forex', etc.). Defaults to 'stock'.
    Returns:
        dict: The JSON response with search results or an error message.
    """
    def get_search_query(self, search, strict=0, type='stock'):
        """Search API."""

        if not search:
            return self.return_error("Search value in empty")

        params = {'s': search, 'strict': strict, 'type':type}
        link = f"{self.basic_url}/search"
        return self.response(link, params)
    
    """
    Get the analytics report for all countries.
    Returns:
        dict: The JSON response with country analytics data or an error message.
    """
    def get_country_report(self):
        params={}
        link = f"{self.basic_url}/analytics"
        return self.response(link,params)

    
   