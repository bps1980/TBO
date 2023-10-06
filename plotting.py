import matplotlib.pyplot as plt

# Assuming upper, lower, overbought, and oversold are already defined

# Plot Bollinger Bands
plt.plot(upper, color='red', label="Upper Bollinger Band")
plt.plot(lower, color='green', label="Lower Bollinger Band")

# Add horizontal lines for overbought and oversold levels
plt.axhline(y=overbought, color='red')
plt.axhline(y=oversold, color='green')

# Adding legends, title, and showing the plot
plt.legend()
plt.title("Bollinger Bands with Overbought and Oversold Levels")
plt.show()

pip install matplotlib