import pandas as pd
import ta

# Assuming you have a pandas DataFrame df with a 'close' column
df = pd.DataFrame({'close': [...]})


# Prompting the user for input values (or you can directly assign them if you don't need to prompt)
lengthBB = int(input("Bollinger Bands Length: ")) or 20
src_std_choice = input("Source (just press Enter for default 'close'): ") or 'close'
mult = float(input("Multiplier: ")) or 2.0

# Using the 'ta' library to calculate the Bollinger Bands
df['basis'] = ta.trend.sma_indicator(df['close'], lengthBB)
df['upper'] = df['basis'] + mult * df[src_std_choice].rolling(window=lengthBB).std()
df['lower'] = df['basis'] - mult * df[src_std_choice].rolling(window=lengthBB).std()

# Print or manipulate the result as needed
print(df[['basis', 'upper', 'lower']])
