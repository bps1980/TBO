import pandas as pd

# Assuming you have a DataFrame named 'df' with a 'volume' column
# df = pd.DataFrame({'volume': [...]})

# Volume Confirmation
vol_multiplier = float(input("Volume Multiplier (default is 1.5): ") or 1.5)
avg_vol = df['volume'].rolling(window=20).mean()
df['vol_condition'] = df['volume'] > avg_vol * vol_multiplier

# Print or manipulate the result as needed
print(df['vol_condition'].head())  # Display the first 5 rows of vol_condition
