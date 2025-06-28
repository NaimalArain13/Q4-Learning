from agents import function_tool
from dotenv import load_dotenv
import os
import requests

load_dotenv()

base_url=os.getenv("COIN_LORE_BASE_URL")
print(base_url)
@function_tool
def get_all_tickers(start:int=0,limit:int=10):
    print("get_all_tickers is calling")
    url=f"{base_url}/tickers?start={start}&limit={limit}"
    response=requests.get(url)
    return response.json()["data"]

@function_tool
def get_ticker_by_id(ticker_id:str):
    print("get_ticker_by_id is calling")
    print("ticker_id is",ticker_id)
    url=f"{base_url}/tickers/?id={ticker_id}"
    response=requests.get(url)
    return response.json()

@function_tool
def get_cryptoInfo():
    print("get_cryptoInfo is calling")	
    url=f"{base_url}/global"
    response=requests.get(url)
    return response.json()

@function_tool
def get_ticker_by_symbol(symbol: str):
    print("symbol is",symbol)
    print("get_ticker_by_symbol is calling	")
    """Get ticker info by coin symbol, such as 'ETH'."""
    url = f"{base_url}/tickers"
    response = requests.get(url)
    tickers = response.json()["data"]
    
    for ticker in tickers:
        if ticker["symbol"].upper() == symbol.upper():
            return ticker["id"]
    
    return {"error": f"Symbol '{symbol}' not found."}


@function_tool
def get_market_cap_id(market_cap_id):
    print("market_cap_id is", market_cap_id)
    print("get_market_cap_id is calling")
    url=f"{base_url}/coin/markets/?id={market_cap_id}"
    print("url is",url)
    response=requests.get(url)
    return response.json()



