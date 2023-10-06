import pandas as pd
import ta.trend

# Assuming you have a DataFrame named 'df' with a 'close' column for your data source
# df = pd.DataFrame({'close': [...]}).

# Compute MACD
df['macd'] = ta.trend.macd_diff(df['close'], n_fast=12, n_slow=26, fillna=False)

# Note: In the 'ta' library, the MACD difference (macd_diff) is the difference between the MACD line and the signal line.
# If you want to separately get the MACD line and the signal line, you can do:
df['macd_line'] = ta.trend.macd_line(df['close'], n_fast=12, n_slow=26, fillna=False)
df['signal_line'] = ta.trend.macd_signal(df['close'], n_fast=12, n_slow=26, n_sign=9, fillna=False)

# Print or manipulate the result as needed
print(df[['macd', 'macd_line', 'signal_line']].head())  # Display the first 5 rows of the columns
