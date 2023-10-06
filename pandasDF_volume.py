from binance.client import Client
import pandas as pd

API_KEY = 'YOUR_BINANCE_API_KEY'
API_SECRET = 'YOUR_BINANCE_API_SECRET'

# Initialize the Binance client
client = Client(API_KEY, API_SECRET)

def get_binance_data(symbol_pair, interval, start_time, end_time):
    # Fetch klines (candlestick data) from Binance
    klines = client.get_historical_klines(symbol_pair, interval, start_time, end_time)
    
    # Convert klines to DataFrame
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base', 'taker_buy_quote', 'ignore'])
    
    # Convert 'volume' column to float
    df['volume'] = df['volume'].astype(float)
    
    return df[['volume']]  # Only return the 'volume' column

# Example usage:
symbol_pair = input("Enter the symbol pair (e.g., BTCUSDT for Bitcoin/USDT): ")
interval = Client.KLINE_INTERVAL_1DAY  # Daily data; adjust as needed
start_time = input("Enter the start date (YYYY-MM-DD): ")
end_time = input("Enter the end date (YYYY-MM-DD): ")

df = get_binance_data(symbol_pair, interval, start_time, end_time)
print(df.head())  # Display the first 5 rows of 'volume' column
