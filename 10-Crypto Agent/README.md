## Crytpo Agent usign OpenAI Agent SDK:

# ✅ Available Tools (Functions)

---

## 1. `get_all_tickers(start=0, limit=10)`
🔍 **Purpose:** Fetches data for the top cryptocurrencies in the market.  
📦 **Data Returned:** Symbol, price, market cap, volume, etc.  
🧠 **Use Case:** When a user asks “Show me the top 10 coins”, this function is used.

---

## 2. `get_ticker_by_id(ticker_id)`
🔍 **Purpose:** Retrieves detailed data of a specific coin using its numeric ID.  
🎯 **Input:** Coin's numeric ID (not the symbol).  
🧠 **Use Case:** Used in backend tasks when a coin needs to be fetched using its ID.

---

## 3. `get_cryptoInfo()`
🔍 **Purpose:** Provides an overview of the entire crypto market.  
📈 **Data Returned:** Total market cap, 24-hour volume, number of active currencies, etc.  
🧠 **Use Case:** When the user asks “What’s today’s crypto market overview?”

---

## 4. `get_ticker_by_symbol(symbol)`
🔍 **Purpose:** Returns the numeric ID of a coin when given its symbol (e.g., BTC, ETH).  
🧠 **Use Case:** When the user wants to fetch a coin’s ID using its symbol (for use in other functions).

---

## 5. `get_market_cap_id(market_cap_id)`
🔍 **Purpose:** Provides market data of a specific coin using its market cap ID.  
📦 **Data Returned:** Market-related data of that coin.

---