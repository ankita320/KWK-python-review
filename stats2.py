# KWK-python-review
python review for data science from KWK
import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/mikaela-el/repo/master/kwk_spotify.csv'
spotify = pd.read_csv(url)

# preview data 
spotify.head()
spotify.cov()

# create a correlation matrix 
import seaborn as sns

# set the figure size 
plt.subplots(figsize=(18, 12))

# create var for matrix 
corr = spotify.corr()

# plot the cor matrix 
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values, linewidths=.5,annot=True)

#change the color palette
sns.color_palette("coolwarm", as_cmap=True)

# looking at the color scale, what do you notice?

from scipy.stats import norm


mean = 170
sdev = 20
xvals = np.arange(110, 230, 0.01)

plt.figure()
plt.plot(xvals, norm.pdf(xvals, loc = mean, scale = sdev))
plt.xlabel('Height')
plt.ylabel('Density')
plt.show()

norm.pdf(xvals, loc = mean, scale = sdev)

x=200
mean=170
sdev=20


zscore= (x-mean)/sdev
# print the zscore
print(zscore)

fill_range = np.arange(100,200,0.01)

plt.figure()
plt.plot(xvals, norm.pdf(xvals, loc = mean, scale = sdev))
plt.xlabel('Height')
plt.ylabel('Density')
plt.fill_between(fill_range,norm.pdf(fill_range, loc = mean, scale = sdev))
plt.show()

norm.cdf(zscore)

1-norm.cdf(zscore)
