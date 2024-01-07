# sigma(price) indicators.

''' check for the daily returns... and arrange in increasing order. and plot the distribution and check for the sigma moves. 
    plot the price and below the weekly returns. 
    highlight the points where there are weekly sigma moves(>1 sigma).

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("^SPX.csv")
df['monthly_returns'] = (df['Close'] - df['Open'])
df['monthly_returns_perc'] = df['monthly_returns'] * 100 / df['Close']
jd =  df['monthly_returns_perc'].sort_values()
plt.hist(jd, bins = 30)
plt.plot()

# Specify the value of x you want to indicate
value_of_x = 0

# Plot a vertical line at the specified x value
plt.axvline(x=value_of_x, color='red', linestyle='-', linewidth=1.5)


# Annotate the line with a small triangle pointer
plt.annotate(
    f' x = {value_of_x}',  # Text to display
    xy=(value_of_x, 0),  # Coordinate to annotate
    xytext=(value_of_x, 30),  # Coordinate to place the text
    textcoords='offset points',
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', lw=1),
    color='black',
    fontsize=10,
)

value_of_x = df['monthly_returns_perc'][len(jd)-1]

# Plot a vertical line at the specified x value
plt.axvline(x=value_of_x, color='blue', linestyle='-', linewidth=0.5)

# Annotate the line with a small triangle pointer
plt.annotate(
    f' x = {value_of_x}',  # Text to display
    xy=(value_of_x, 0),  # Coordinate to annotate
    xytext=(value_of_x, 30),  # Coordinate to place the text
    textcoords='offset points',
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', lw=1),
    color='blue',
    fontsize=10,
)

plt.show()

history = df[df['monthly_returns_perc'].between(df['monthly_returns_perc'].iloc[-1] - 1, 
                                                df['monthly_returns_perc'].iloc[-1] + 1)].index

plt.plot(df['Date'],df['Close'])


for i in history:
    value_of_x = df['Date'][i]

    # Plot a vertical line at the specified x value
    plt.axvline(x=value_of_x, color='blue', linestyle='-', linewidth=0.5)

    # Annotate the line with a small triangle pointer
    plt.annotate(
        f' x = {value_of_x}',  # Text to display
        xy=(value_of_x, 0),  # Coordinate to annotate
        xytext=(value_of_x, 30),  # Coordinate to place the text
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', lw=1),
        color='blue',
        fontsize=10,
    )

plt.show()
one_month = []
three_month = []
six_month = []
twelve_month = []


for i in history:
    value_of_x = df['Date'][i]
    try:
        one_month.append(100*(df['Close'][i+1]-df['Close'][i])/df['Close'][i])
    except Exception as e:
        one_month.append("NA")

    try:
        three_month.append(100*(df['Close'][i+3]-df['Close'][i])/df['Close'][i])
    except Exception as e:
        three_month.append("NA")
    
    try:
        six_month.append(100*(df['Close'][i+3]-df['Close'][i])/df['Close'][i])
    except Exception as e:
        six_month.append("NA")

    try:
        twelve_month.append(100*(df['Close'][i+3]-df['Close'][i])/df['Close'][i])
    except Exception as e:
        twelve_month.append("NA")

data = {'1-Month': one_month,'3-Month': three_month, '6-month': six_month, '12-month': twelve_month}
df2 = pd.DataFrame(data)
print(df2)



