import pandas as pd
import ta.trend
from binance.client import Client

API_KEY = 'YOUR_BINANCE_API_KEY'
API_SECRET = 'YOUR_BINANCE_API_SECRET'
client = Client(API_KEY, API_SECRET)

def get_binance_data(symbol_pair, interval, start_time, end_time):
    klines = client.get_historical_klines(symbol_pair, interval, start_time, end_time)
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base', 'taker_buy_quote', 'ignore'])
    df['close'] = df['close'].astype(float)
    return df

# Fetching data
symbol_pair = input("Enter the symbol pair (e.g., BTCUSDT for Bitcoin/USDT): ")
interval = Client.KLINE_INTERVAL_1DAY
start_time = input("Enter the start date (YYYY-MM-DD): ")
end_time = input("Enter the end date (YYYY-MM-DD): ")
df = get_binance_data(symbol_pair, interval, start_time, end_time)

# Compute MACD
df['macd'] = ta.trend.macd_diff(df['close'], n_fast=12, n_slow=26, fillna=False)
df['macd_line'] = ta.trend.macd_line(df['close'], n_fast=12, n_slow=26, fillna=False)
df['signal_line'] = ta.trend.macd_signal(df['close'], n_fast=12, n_slow=26, n_sign=9, fillna=False)

# Print results
print(df[['close', 'macd', 'macd_line', 'signal_line']].head())
