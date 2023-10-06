import pandas as pd
import ta.momentum

# Sample DataFrame for demonstration purposes
# df = pd.DataFrame({'close': [...]})

# RSI Calculation
rsi_length = int(input("Enter RSI Length (default is 14): ") or 14)
overbought = 80
oversold = 20
df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=rsi_length).rsi()

# Print or manipulate the result as needed
print(df[['close', 'rsi']].head())  # Display the first 5 rows of 'close' and 'rsi' columns
