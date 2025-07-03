# Functions from the mcp python sdk 
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
from tools import *

# Creating our MCP server
# Similar to FastAPI 
# If http specify port and host if not standart io 
mcp = FastMCP(
    name = "Alpha Vantage MCP Server",
    host = "0.0.0.0",   # Only used for SSE transport (localhost)
    port = 8080,    # Only used for SSE transport (set to any port)
)

app = FastAPI()

@mcp.tool()
@app.get("/get_current_price/{symbol}")
async def get_current_price_tool(symbol: str) -> str:
    """
    Gets the current price of a stock from Alpha Vantage API.
    """
    try:
        return get_current_price(symbol)
    except Exception as e:
        return f"Error getting current price for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_stock_price/{symbol}")
async def get_stock_price_tool(symbol: str) -> dict:
    """
    Get the latest intraday stock price.
    """
    try:
        return get_stock_price(symbol)
    except Exception as e:
        return f"Error getting stock price for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_intraday/{symbol}")
async def get_intraday_tool(symbol: str, interval: Optional[str] = "1min") -> dict:
    """
    Fetch intraday time series for a given stock symbol.
    """
    try:
        return get_intraday(symbol, interval)
    except Exception as e:
        return f"Error getting intraday data for {symbol} with interval {interval}: {str(e)}"

@mcp.tool()
@app.get("/get_daily_adjusted/{symbol}")
async def get_daily_adjusted_tool(symbol: str) -> dict:
    """
    Fetch daily adjusted time series data for a given symbol.
    """
    try:
        return get_daily_adjusted(symbol)
    except Exception as e:
        return f"Error getting daily adjusted data for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_weekly/{symbol}")
async def get_weekly_tool(symbol: str) -> dict:
    """
    Fetch weekly time series data for a given symbol.
    """
    try:
        return get_weekly(symbol)
    except Exception as e:
        return f"Error getting weekly data for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_weekly_adjusted/{symbol}")
async def get_weekly_adjusted_tool(symbol: str) -> dict:
    """
    Fetch weekly adjusted time series data for a given symbol.
    """
    try:
        return get_weekly_adjusted(symbol)
    except Exception as e:
        return f"Error getting weekly adjusted data for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_monthly/{symbol}")
async def get_monthly_tool(symbol: str) -> dict:
    """
    Fetch monthly time series data for a given symbol.
    """
    try:
        return get_monthly(symbol)
    except Exception as e:
        return f"Error getting monthly data for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_monthly_adjusted/{symbol}")
async def get_monthly_adjusted_tool(symbol: str) -> dict:
    """
    Fetch monthly adjusted time series data for a given symbol.
    """
    try:
        return get_monthly_adjusted(symbol)
    except Exception as e:
        return f"Error getting monthly adjusted data for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_quote/{symbol}")
async def get_quote_tool(symbol: str) -> dict:
    """
    Fetch the current global quote for a given stock symbol.
    """
    try:
        return get_quote(symbol)
    except Exception as e:
        return f"Error getting quote for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_market_status")
async def get_market_status_tool() -> dict:
    """
    Fetch the current global market status.
    """
    try:
        return get_market_status()
    except Exception as e:
        return f"Error getting market status: {str(e)}"

@mcp.tool()
@app.get("/get_historical_options/{symbol}")
async def get_historical_options_tool(symbol: str, date: Optional[str] = None, datatype: str = "json") -> dict:
    """
    Fetch historical options data for a symbol, optionally for a specific date.
    """
    try:
        return get_historical_options_simple(symbol, date, datatype)
    except Exception as e:
        return f"Error getting historical options for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_news_sentiment/{symbol}")
async def get_news_sentiment_tool(symbol: str) -> dict:
    """
    Fetch news and sentiment trending data for a symbol.
    """
    try:
        return get_news_sentiment(symbol)
    except Exception as e:
        return f"Error getting news sentiment for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_earnings_transcript/{symbol}")
async def get_earnings_transcript_tool(symbol: str) -> dict:
    """
    Fetch earnings call transcript for a symbol.
    """
    try:
        return get_earnings_transcript(symbol)
    except Exception as e:
        return f"Error getting earnings transcript for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_top_gainers_losers")
async def get_top_gainers_losers_tool() -> dict:
    """
    Fetch top gainers and losers data.
    """
    try:
        return get_top_gainers_losers()
    except Exception as e:
        return f"Error getting top gainers and losers: {str(e)}"

@mcp.tool()
@app.get("/get_insider_transactions/{symbol}")
async def get_insider_transactions_tool(symbol: str) -> dict:
    """
    Fetch insider transactions trending data for a symbol.
    """
    try:
        return get_insider_transactions(symbol)
    except Exception as e:
        return f"Error getting insider transactions for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_analytics_fixed/{symbol}/{function_name}")
async def get_analytics_fixed_tool(symbol: str, function_name: str, interval: str = "daily", time_period: int = 10, series_type: str = "close") -> dict:
    """
    Fetch fixed window technical indicator data (e.g., SMA, EMA, RSI).
    """
    try:
        return get_analytics_fixed(symbol, function_name, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting analytics fixed for {symbol} function {function_name}: {str(e)}"

@mcp.tool()
@app.get("/get_analytics_sliding/{symbol}/{function_name}")
async def get_analytics_sliding_tool(symbol: str, function_name: str, interval: str = "daily", time_period: int = 10, series_type: str = "close") -> dict:
    """
    Fetch sliding window technical indicator data (requires premium API).
    """
    try:
        return get_analytics_sliding(symbol, function_name, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting analytics sliding for {symbol} function {function_name}: {str(e)}"

@mcp.tool()
@app.get("/get_fundamental_data/{symbol}")
async def get_fundamental_data_tool(symbol: str) -> dict:
    """
    Fetch fundamental data for a symbol.
    """
    try:
        return get_fundamental_data(symbol)
    except Exception as e:
        return f"Error getting fundamental data for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_company_overview_trending")
async def get_company_overview_trending_tool() -> dict:
    """
    Fetch trending company overview data.
    """
    try:
        return get_company_overview_trending()
    except Exception as e:
        return f"Error getting company overview trending data: {str(e)}"

@mcp.tool()
@app.get("/get_etf_profile_and_holdings/{symbol}")
async def get_etf_profile_and_holdings_tool(symbol: str) -> dict:
    """
    Fetch ETF profile and holdings for a symbol.
    """
    try:
        return get_etf_profile_and_holdings(symbol)
    except Exception as e:
        return f"Error getting ETF profile and holdings for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_corporate_action_dividends/{symbol}")
async def get_corporate_action_dividends_tool(symbol: str) -> dict:
    """
    Fetch corporate action dividend data for a symbol.
    """
    try:
        return get_corporate_action_dividends(symbol)
    except Exception as e:
        return f"Error getting corporate action dividends for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_corporate_action_splits/{symbol}")
async def get_corporate_action_splits_tool(symbol: str) -> dict:
    """
    Fetch corporate action splits data for a symbol.
    """
    try:
        return get_corporate_action_splits(symbol)
    except Exception as e:
        return f"Error getting corporate action splits for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_income_statement/{symbol}")
async def get_income_statement_tool(symbol: str) -> dict:
    """
    Fetch income statement data for a company symbol.
    """
    try:
        return get_income_statement(symbol)
    except Exception as e:
        return f"Error getting income statement for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_balance_sheet/{symbol}")
async def get_balance_sheet_tool(symbol: str) -> dict:
    """
    Fetch the balance sheet data for a company symbol.
    """
    try:
        return get_balance_sheet(symbol)
    except Exception as e:
        return f"Error getting balance sheet for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_cash_flow/{symbol}")
async def get_cash_flow_tool(symbol: str) -> dict:
    """
    Fetch the cash flow statement for a company symbol.
    """
    try:
        return get_cash_flow(symbol)
    except Exception as e:
        return f"Error getting cash flow for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_earnings_trending")
async def get_earnings_trending_tool() -> dict:
    """
    Fetch trending earnings data.
    """
    try:
        return get_earnings_trending()
    except Exception as e:
        return f"Error getting earnings trending data: {str(e)}"

@mcp.tool()
@app.get("/get_listing_delisting_status")
async def get_listing_delisting_status_tool() -> dict:
    """
    Fetch listing and delisting status data.
    """
    try:
        return get_listing_delisting_status()
    except Exception as e:
        return f"Error getting listing/delisting status data: {str(e)}"

@mcp.tool()
@app.get("/get_earnings_calendar")
async def get_earnings_calendar_tool() -> dict:
    """
    Fetch earnings calendar data.
    """
    try:
        return get_earnings_calendar()
    except Exception as e:
        return f"Error getting earnings calendar data: {str(e)}"

@mcp.tool()
@app.get("/get_ipo_calendar")
async def get_ipo_calendar_tool() -> dict:
    """
    Fetch IPO calendar data.
    """
    try:
        return get_ipo_calendar()
    except Exception as e:
        return f"Error getting IPO calendar data: {str(e)}"

@app.get("/get_currency_exchange_rate/{from_currency}/{to_currency}")
async def get_currency_exchange_rate_tool(from_currency: str, to_currency: str) -> dict:
    """
    Gets the current exchange rate between two currencies from Alpha Vantage API.
    
    Args:
        from_currency: Source currency (e.g.: USD, EUR)
    """
    try:
        return get_currency_exchange_rate(from_currency, to_currency)
    except Exception as e:
        return f"Error getting exchange rate for {from_currency} to {to_currency}: {str(e)}"
    
@mcp.tool()
@app.get("/get_fx_daily_data/{from_symbol}/{to_symbol}")
async def get_fx_daily_data_tool(from_symbol: str, to_symbol: str) -> dict:
    """
    Gets the daily time series (timestamp, open, high, low, close) of the FX currency pair from Alpha Vantage API.
    """
    try:
        return get_fx_daily_data(from_symbol, to_symbol)
    except Exception as e:
        return f"Error getting FX daily data for {from_symbol} to {to_symbol}: {str(e)}"
    
@mcp.tool()
@app.get("/get_fx_weekly_data/{from_symbol}/{to_symbol}")
async def get_fx_weekly_data_tool(from_symbol: str, to_symbol: str) -> dict:
    """
    Gets the weekly time series (timestamp, open, high, low, close) of the FX currency pair from Alpha Vantage API.
    """
    try:
        return get_fx_weekly_data(from_symbol, to_symbol)
    except Exception as e:
        return f"Error getting FX weekly data for {from_symbol} to {to_symbol}: {str(e)}"
    
@mcp.tool()
@app.get("/get_fx_monthly_data/{from_symbol}/{to_symbol}")
async def get_fx_monthly_data_tool(from_symbol: str, to_symbol: str) -> dict:
    """
    Gets the monthly time series (timestamp, open, high, low, close) of the FX currency pair from Alpha Vantage API.
    """
    try:
        return get_fx_monthly_data(from_symbol, to_symbol)
    except Exception as e:
        return f"Error getting FX monthly data for {from_symbol} to {to_symbol}: {str(e)}"
    
@mcp.tool()
@app.get("/get_digital_currency_daily_data/{symbol}/{market}")
async def get_digital_currency_daily_data_tool(symbol: str, market: str) -> dict:
    """
    Gets the daily historical time series for a digital currency traded on a specific market from Alpha Vantage API.
    """
    try:
        return get_digital_currency_daily_data(symbol, market)
    except Exception as e:
        return f"Error getting digital currency daily data for {symbol} on {market}: {str(e)}"
    
@mcp.tool()
@app.get("/get_digital_currency_weekly_data/{symbol}/{market}")
async def get_digital_currency_weekly_data_tool(symbol: str, market: str) -> dict:
    """
    Gets the weekly historical time series for a digital currency traded on a specific market from Alpha Vantage API.
    """
    try:
        return get_digital_currency_weekly_data(symbol, market)
    except Exception as e:
        return f"Error getting digital currency weekly data for {symbol} on {market}: {str(e)}"

@mcp.tool()
@app.get("/get_digital_currency_monthly_data/{symbol}/{market}")
async def get_digital_currency_monthly_data_tool(symbol: str, market: str) -> dict:
    """
    Gets the monthly historical time series for a digital currency traded on a specific market from Alpha Vantage API.
    """
    try:
        return get_digital_currency_monthly_data(symbol, market)
    except Exception as e:
        return f"Error getting digital currency monthly data for {symbol} on {market}: {str(e)}"
    
@mcp.tool()
@app.get("/get_crude_oil_wti_data/")
async def get_crude_oil_wti_data_tool(interval: str) -> dict:
    """
    Gets the daily, weekly, or monthly historical time series for the West Texas Intermediate (WTI) crude oil prices from Alpha Vantage API.
    """
    try:
        return get_crude_oil_wti_data(interval)
    except Exception as e:
        return f"Error getting crude oil WTI data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_crude_oil_brent_data/{interval}")
async def get_crude_oil_brent_data_tool(interval: str) -> dict:
    """
    Gets the daily, weekly, or monthly historical time series for the Brent crude oil prices from Alpha Vantage API.
    """
    try:
        return get_crude_oil_brent_data(interval)
    except Exception as e:
        return f"Error getting crude oil Brent data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_natural_gas_data/{interval}")
async def get_natural_gas_data_tool(interval: str) -> dict:
    """
    Gets the daily, weekly, or monthly historical time series for the natural gas prices from Alpha Vantage API.
    """
    try:
        return get_natural_gas_data(interval)
    except Exception as e:
        return f"Error getting natural gas data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_copper_data/{interval}")
async def get_copper_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of copper from Alpha Vantage API.
    """
    try:
        return get_copper_data(interval)
    except Exception as e:
        return f"Error getting copper data for {interval}: {str(e)}"

@mcp.tool()
@app.get("/get_aluminum_data/{interval}")
async def get_aluminum_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of aluminum from Alpha Vantage API.
    """
    try:
        return get_aluminum_data(interval)
    except Exception as e:
        return f"Error getting aluminum data for {interval}: {str(e)}"

@mcp.tool()
@app.get("get_wheat_data/{interval}")
async def get_wheat_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of wheat from Alpha Vantage API.
    """
    try:
        return get_wheat_data(interval)
    except Exception as e:
        return f"Error getting wheat data for {interval}: {str(e)}"

@mcp.tool()
@app.get("/get_corn_data/{interval}")
async def get_corn_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of corn from Alpha Vantage API.
    """
    try:
        return get_corn_data(interval)
    except Exception as e:
        return f"Error getting corn data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_cotton_data/{interval}")
async def get_cotton_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of cotton from Alpha Vantage API.
    """
    try:
        return get_cotton_data(interval)
    except Exception as e:
        return f"Error getting cotton data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_sugar_data/{interval}")
async def get_sugar_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of sugar from Alpha Vantage API.
    """
    try:
        return get_sugar_data(interval)
    except Exception as e:
        return f"Error getting sugar data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_coffee_data/{interval}")
async def get_coffee_data_tool(interval: str) -> dict:
    """
    Gets the monthly, quarterly and annual global price of coffee from Alpha Vantage API.
    """
    try:
        return get_coffee_data(interval)
    except Exception as e:
        return f"Error getting coffee data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_all_commodities_data/{interval}")
async def get_all_commodities_data_tool(interval: str) -> dict:
    """
    Gets the global price index of all commodities in monthly, quarterly, and annual temporal dimensions.
    """
    try:
        return get_all_commodities_data(interval)
    except Exception as e:
        return f"Error getting all commodities data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_real_gdp_data/{interval}")
async def get_real_gdp_data_tool(interval: str) -> dict:
    """
    Gets the real GDP data of the US economy in quarterly and annual temporal dimensions.
    """
    try:
        return get_real_gdp(interval)
    except Exception as e:
        return f"Error getting real GDP data for {interval}: {str(e)}"
    
@mcp.tool()
@app.get("/get_real_gdp_per_capita_data/")
async def get_real_gdp_per_capita_data_tool() -> dict:
    """
    Gets the real GDP per capita data quaterly of the US economy.
    """
    try:
        return get_real_gdp_per_capita()
    except Exception as e:
        return f"Error getting real GDP per capita data: {str(e)}"
    
@mcp.tool()
@app.get("get_treasury_yield/{interval}-{maturity}")
async def get_treasury_yield_tool(interval: str, maturity: str) -> dict:
    """
    Gets the US Treasury yield data for a specific maturity and interval.
    
    Args:
        interval: Interval of the data (e.g.: daily, weekly, monthly)
        maturity: Maturity of the treasury yield (e.g.: 10Y, 30Y)
    
    Returns:
        Treasury yield data
    """
    try:
        return get_treasury_yield(interval, maturity)
    except Exception as e:
        return f"Error getting treasury yield data for {maturity} at {interval} interval: {str(e)}"
    
@mcp.tool()
@app.get("/get_federal_funds_rate/{interval}")
async def get_federal_funds_rate_tool(interval: str) -> dict:
    """
    Gets the Federal Funds Rate in the US data for a specific interval.
    
    Args:
        interval: Interval of the data (e.g.: daily, weekly, monthly)
    
    Returns:
        Federal Funds Rate data
    """
    try:
        return get_federal_funds_rate(interval)
    except Exception as e:
        return f"Error getting Federal Funds Rate data at {interval} interval: {str(e)}"
    
@mcp.tool()
@app.get("/get_cpi_data/{interval}")
async def get_cpi_data_tool(interval: str) -> dict:
    """
    Gets the Consumer Price Index (CPI) data in the US for a specific interval.
    
    Args:
        interval: Interval of the data (monthly and semi-annual)
    
    Returns:
        CPI data
    """
    try:
        return get_cpi_data(interval)
    except Exception as e:
        return f"Error getting CPI data at {interval} interval: {str(e)}"
    
@mcp.tool()
@app.get("/get_inflation_data")
async def get_inflation_data_tool() -> dict:
    """
    Gets the inflation rate data in the US.
    """
    try:
        return get_inflation()
    except Exception as e:
        return f"Error getting inflation data: {str(e)}"

@mcp.tool()
@app.get("/get_retail_sales")
async def get_retail_sales_tool() -> dict:
    """
    Gets the monthly retail sales data in the US.
    """
    try:
        return get_retail_sales()
    except Exception as e:
        return f"Error getting retail sales data: {str(e)}"
    
@mcp.tool()
@app.get("/get_durables")
async def get_durables_tool() -> dict:
    """
    Gets the monthly manufacturers' new orders of durable goods in the US.
    """
    try:
        return get_durables()
    except Exception as e:
        return f"Error getting durable goods data: {str(e)}"
    
@mcp.tool()
@app.get("get_monthly_unemployment_rate")
async def get_monthly_unemployment_rate_tool() -> dict:
    """
    Gets the monthly unemployment rate in the US.
    """
    try:
        return get_monthly_unemployment()
    except Exception as e:
        return f"Error getting monthly unemployment rate data: {str(e)}"
    
@mcp.tool()
@app.get("/get_nonfarm_payrolls")
async def get_nonfarm_payrolls_tool() -> dict:
    """
    Gets the monthly US All Employees: Total Nonfarm (commonly known as Total Nonfarm Payroll), 
    a measure of the number of U.S. workers in the economy that excludes proprietors, private household employees,
    unpaid volunteers, farm employees, and the unincorporated self-employed.
    """
    try:
        return get_nonfarm_payroll()
    except Exception as e:
        return f"Error getting non-farm payrolls data: {str(e)}"
    
@mcp.tool()
@app.get("/get_sma_data/{symbol}/{series_type}")
async def get_sma_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the Simple Moving Average (SMA) data for a given symbol and series type.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        SMA data
    """
    try:
        return get_sma_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting SMA data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_ema_data/{symbol}/{series_type}")
async def get_ema_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the Exponential Moving Average (EMA) data for a given symbol and series type.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        EMA data
    """
    try:
        return get_ema_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting EMA data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_wma_data/{symbol}/{series_type}")
async def get_wma_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the Weighted Moving Average (WMA) data for a given symbol and series type.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        WMA data
    """
    try:
        return get_wma_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting WMA data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_dema_data/{symbol}/{series_type}")
async def get_dema_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the Double Exponential Moving Average (DEMA) data for a given symbol and series type.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        DEMA data
    """
    try:
        return get_dema_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting DEMA data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_tema_data/{symbol}/{series_type}")
async def get_tema_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the Triple Exponential Moving Average (TEMA) data for a given symbol and series type.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        TEMA data
    """
    try:
        return get_tema_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting DEMA data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_trima_data/{symbol}/{series_type}")
async def get_trima_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the Triangular Moving Average (TRIMA) data for a given symbol and series type.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        TRIMA data
    """
    try:
        return get_trima_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting TRIMA data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_kama_data/{symbol}/{series_type}")
async def get_kama_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the Kaufman Adaptive Moving Average (KAMA) data for a given symbol and series type.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        KAMA data
    """
    try:
        return get_kama_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting KAMA data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_mama_data/{symbol}/{series_type}")
async def get_mama_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the MESA Adaptive Moving Average (MAMA) data for a given symbol and series type.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        MAMA data
    """
    try:
        return get_kama_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting MAMA data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_vwap_data/{symbol}")
async def get_vwap_data_tool(symbol: str, interval: str = "daily") -> dict:
    """
    Gets the Volume Weighted Average Price (VWAP) data for a given symbol.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        VWAP data
    """
    try:
        return get_vwap_values(symbol, interval)
    except Exception as e:
        return f"Error getting VWAP data for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_tthree_data/{symbol}/{series_type}")
async def get_tthree_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the Triple Exponential Moving Average (T3) values for a given symbol and series type.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        MAMA data
    """
    try:
        return get_tthree_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting MAMA data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_macd_data/{symbol}/{series_type}")
async def get_macd_data_tool(symbol: str, interval: str = "daily", series_type: str = "open", fastperiod: int = 12,
                    slowperiod: int = 26, signalperiod: int = 9) -> dict:
    """
    Gets the Moving Average Convergence Divergence (MACD) values for a given symbol and series type.
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
        fastperiod: Fast period for MACD
        slowperiod: Slow period for MACD
        signalperiod: Signal period for MACD
    Returns:
        MACD data
    """
    try: 
        return get_macd_values(symbol, interval, series_type, fastperiod, slowperiod, signalperiod)
    except Exception as e:
        return f"Error getting MACD data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_macdext_data/{symbol}/{series_type}")
async def get_macdext_data_tool(symbol: str, interval: str = "daily", series_type: str = "open", fastperiod: int = 12,
                    slowperiod: int = 26, signalperiod: int = 9) -> dict:
    """
    Gets the Moving Average Convergence Divergence (MACDEXT) values for a given symbol and series type.
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
        fastperiod: Fast period for MACDEXT
        slowperiod: Slow period for MACDEXT
        signalperiod: Signal period for MACDEXT
    Returns:
        MACD data
    """
    try: 
        return get_macdext_values(symbol, interval, series_type, fastperiod, slowperiod, signalperiod)
    except Exception as e:
        return f"Error getting MACDEXT data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_stoch_data/{symbol}/{series_type}")
async def get_stoch_data_tool(symbol: str, interval: str = "daily", fastk_period: int = 14, slowk_period: int = 3,
                                slowd_period: int = 3, series_type: str = "close") -> dict:
    """
    Gets the Stochastic Oscillator (STOCH) values for a given symbol and series type.
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
        fastk_period: Fast period for STOCH
        slowk_period: Slow period for STOCH
    Returns:
        MACD data
    """
    try: 
        return get_stoch_oscillator_values(symbol, interval, series_type, fastk_period, slowk_period, slowd_period)
    except Exception as e:
        return f"Error getting STOCH data for {symbol} with series type {series_type}: {str(e)}"

@mcp.tool()
@app.get("/get_stochfast_data/{symbol}")
async def get_stochf_data_tool(symbol: str, interval: str = "daily", fastk_period: int = 5, fastdperiod: int = 3) -> dict:
    """
    Gets the Stochastic Fast Oscillator (STOCHF) values for a given symbol.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    Returns:
        STOCHF data
    """
    try: 
        return get_stochf_oscillator_values(symbol, interval, fastk_period, fastdperiod)
    except Exception as e:
        return f"Error getting STOCHF data for {symbol}: {str(e)}"
    
@mcp.tool()
@app.get("/get_rsi_data/{symbol}/{series_type}")
async def get_rsi_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the Relative Strength Index (RSI) values for a given symbol and series type.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        RSI data
    """
    try:
        return get_rsi_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting RSI data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_stochrsi_data/{symbol}/{series_type}")
async def get_stochrsi_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close",
                        fastkperiod: int = 5, fastdperiod: int = 3) -> dict:
    """
    Gets the Stochastic Relative Strength Index (STOCHRSI) values for a given symbol and series type.
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        series_type: Type of the series (e.g.: close, open, high, low)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    Returns:
        STOCHRSI data
    """
    try:
        return get_stochrsi_values(symbol, interval, time_period, series_type, fastkperiod, fastdperiod)
    except Exception as e:
        return f"Error getting STOCHRSI data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_willr_data/{symbol}")
async def get_wilrr_data_tool(symbol: str, interval: str = "daily", time_period: int = 60) -> dict:
    """
    Gets the Williams %R (WILLR) values for a given symbol.
    
    Args:
        symbol: Stock symbol (e.g.: AAPL, MSFT)
        interval: Time interval for the data (e.g.: daily, weekly, monthly)
    
    Returns:
        WILLR data
    """
    try:
        return get_willr_values(symbol, interval, time_period)
    except Exception as e:
        return f"Error getting WILLR data for {symbol}: {str(e)}"
    
@mcp.tool()
@app.get("/get_adx_data/{symbol}/{series_type}")
async def get_adx_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Fetch Average Directional Movement Index (ADX) values for a given symbol.
    """
    try:
        return get_adx_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting ADX data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_adxr_data/{symbol}/{series_type}")
async def get_adxr_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Fetch Average Directional Movement Rating Index (ADX) values for a given symbol.
    """
    try:
        return get_adxr_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting ADXR data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_apo_data/{symbol}/{series_type}")
async def get_apo_data_tool(symbol: str, interval: str = "daily", series_type: str = "close", fastperiod: int = 12,
                   slowperiod: int = 26) -> dict:
    """
    Fetch Absolute Price Oscillator (APO) values for a given symbol.
    """
    try:
        return get_apo_values(symbol, interval, series_type, fastperiod, slowperiod)
    except Exception as e:
        return f"Error getting APO data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_ppo_data/{symbol}/{series_type}")
async def get_ppo_data_tool(symbol: str, interval: str = "daily", series_type: str = "close", fastperiod: int = 12,
                   slowperiod: int = 26) -> dict:
    """
    Fetch Percentage Price Oscillator (PPO) values for a given symbol.
    """
    try:
        return get_ppo_values(symbol, interval, series_type, fastperiod, slowperiod)
    except Exception as e:
        return f"Error getting PPO data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_mom_data/{symbol}/{series_type}")
async def get_mom_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Fetch Momentum (MOM) values for a given symbol.
    """
    try:
        return get_mom_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting MOM data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_bop_data/{symbol}")
async def get_bop_data_tool(symbol: str, interval: str = "daily") -> dict:
    """
    Fetch Balance of Power (BOP) values for a given symbol.
    """
    try:
        return get_bop_values(symbol, interval)
    except Exception as e:
        return f"Error getting BOP data for {symbol}: {str(e)}"
    
@mcp.tool()
@app.get("/get_cci_data/{symbol}")
async def get_cci_data_tool(symbol: str, interval: str = "daily", time_period: int = 60) -> dict:
    """
    Fetch Commodity Channel Index (CCI) values for a given symbol.
    """
    try:
        return get_cci_values(symbol, interval, time_period)
    except Exception as e:
        return f"Error getting CCI data for {symbol}: {str(e)}"

@mcp.tool()
@app.get("/get_cmo_data/{symbol}/{series_type}")
async def get_cmo_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Fetch Chande momentum oscillator (CMO) values for a given symbol.
    """
    try:
        return get_cmo_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting CMO data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_roc_data/{symbol}/{series_type}")
async def get_roc_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Fetch rate of change (ROC) values for a given symbol.
    """
    try:
        return get_roc_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting ROC data for {symbol} with series type {series_type}: {str(e)}"
    
@mcp.tool()
@app.get("/get_rocr_data/{symbol}/{series_type}")
async def get_rocr_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Fetch rate of change ratio (ROCR) values for a given symbol.
    """
    try:
        return get_rocr_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting ROCR data for {symbol} with series type {series_type}: {str(e)}"

@mcp.tool()
@app.get("/get_mama_data/{symbol}/{series_type}")
async def get_mama_data_tool(symbol: str, interval: str = "daily", time_period: int = 60, series_type: str = "close") -> dict:
    """
    Gets the MESA Adaptive Moving Average (MAMA) data for a given symbol and series type.
    """
    try:
        return get_mama_values(symbol, interval, time_period, series_type)
    except Exception as e:
        return f"Error getting MAMA data for {symbol} with series type {series_type}: {str(e)}"

# Run the server
if __name__ == "__main__":
    transport = "stdio"
    if transport == "stdio":
        print("Running mcp server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unknown transport: {transport}")