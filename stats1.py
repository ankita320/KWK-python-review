# KWK-python-review
python review for data science from KWK
import math 
import statistics 
import numpy as np 
import scipy.stats 
import pandas as pd

mean = sum(x) / len(x)
print(mean)

dataframe_name["column_name"].mean()

# creating our dataframe
order = pd.DataFrame({'item_price':[2.39, 3.39, 3.39, 2.39, 16.98, 10.98, 1.69, 11.75, 9.25, 9.25, 4.45, 8.75],
                   'items_ordered':[1,2,2,1,4,3,1,4,3,3,2,3 ]})

# looking at our data
order.head(12)

# calculating the mean 
order['item_price'].mean()

dataframe_name["column_name"].median()


order['item_price'].median()
dataframe_name["column_name"].mode()

order['item_price'].mode()

np.var(order["item_price"],ddof=1)
# ddof=1 calculates population variance instead of sample variance

# calculated by taking the square root of the variance 
np.sqrt(np.var(order["item_price"],ddof=1))

# calculated using np.std function 
(np.std(order["item_price"],ddof=1))

# find the 50th quantile
(np.quantile(order["item_price"], .5))

# find the quartiles 
np.quantile(order["item_price"], [0,0.25,0.5,0.75,1])
np.quantile(order["item_price"], [0,0.25,0.5,0.75,1])

# find the interquartile range
np.quantile(order["item_price"],.75) - np.quantile(order["item_price"],.25)

from scipy.stats import iqr

iqr(order['item_price'])

order.describe()

url =  'https://raw.githubusercontent.com/mikaela-el/repo/master/kwk_spotify.csv' 
spotify =  pd.read_csv(url)
# preview data 
spotify.head()
