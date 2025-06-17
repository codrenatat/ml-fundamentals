import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_current_price(symbol: str) -> str:
    """
    Gets the current price of a stock from Alpha Vantage API.
    """
    apikey = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not apikey:
        return "Error: ALPHA_VANTAGE_API_KEY not configured"
    
    url = (
        "https://www.alphavantage.co/query"
        f"?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={apikey}"
    )
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Check if there's an error in the response
        if "Error Message" in data:
            return f"Error: Symbol {symbol} is not valid"
        
        if "Note" in data:
            return "Error: API limit reached. Try again later."
        
        if "Time Series (5min)" not in data:
            return f"Error: Could not get data for {symbol}"
        
        # Get most recent price
        time_series = data["Time Series (5min)"]
        latest_time = sorted(time_series.keys())[-1]
        latest_data = time_series[latest_time]
        latest_price = latest_data["4. close"]
        
        return f"{symbol}: ${latest_price} (updated: {latest_time})"
        
    except requests.RequestException as e:
        return f"Connection error: {str(e)}"
    except Exception as e:
        return f"Data processing error: {str(e)}"