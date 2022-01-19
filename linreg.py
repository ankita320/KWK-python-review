# KWK-python-review
python review for data science from KWK

import pandas as pd
import numpy as np


url = 'https://raw.githubusercontent.com/datacult/kwk-datascience/master/Linear%20regression/test_scores.csv'
data = pd.read_csv(url)

# Be sure to remove duplicates in any data

data.drop_duplicates(inplace = True)

# Count the values in the dataset

data.info()
# Print high level summaries of what is in the dataset
data.describe()

import seaborn as sns
import matplotlib.pyplot as plt


pd.options.display.max_columns = None
from sklearn.linear_model import LinearRegression
# Set size of plot
plt.figure(figsize=(15,8))
# Set X andY values to plot
plt.scatter(data["minutes_studied"],data["test_score"])
# Set axis labels
plt.xlabel("Minutes Studied")
plt.ylabel("Test Score")
# Set axis range
plt.xlim(0,140)
plt.ylim(0,110)
# Y dataset
Y = data[["test_score"]]


# X dataset
X = data[["minutes_studied"]]
test_score_LR_model = LinearRegression()
test_score_LR_model.fit(X,Y)
test_score_LR_model.intercept_
test_score_LR_model.coef_
plt.figure(figsize=(8,8))

# Plot our model output
x_plot = np.linspace(0, 140) 
y_plot = 0.17550916 * x_plot + 70.25449762
plt.plot(x_plot, y_plot)

# Plot our Observed Data
plt.scatter(data["minutes_studied"],data["test_score"])
plt.xlabel("Minutes Studied")
plt.ylabel("Test Score")
plt.xlim(0,140)
plt.ylim(0,110);
test_score_LR_model.predict([[105]])
test_score_LR_model.score(X , Y)
import pandas as pd
import numpy as np
url = 'https://raw.githubusercontent.com/mikaela-el/repo/master/weather_data.csv'
weather = pd.read_csv(url)
# Be sure to remove duplicates in any data
weather.drop_duplicates(inplace = True)

# Count the values in the dataset
weather.info()

import seaborn as sns
import matplotlib.pyplot as plt


pd.options.display.max_columns = None
from sklearn.linear_model import LinearRegression

# Set size of plot
plt.figure(figsize=(15,8))
# Set X andY values to plot
plt.scatter(weather["temp"],weather["rain"])
# Set axis labels
plt.xlabel("temp")
plt.ylabel("rain")
# Set axis range
plt.xlim(0,30)
plt.ylim(0,200)
# Set size of plot
plt.figure(figsize=(8,8))

# Plot our model output
x_plot = np.linspace(0, 200) 
y_plot = -8.6598596 * x_plot + 188.53860881
plt.plot(x_plot, y_plot)

# Set X andY values to plot
plt.scatter(weather["temp"],weather["rain"])
# Set axis labels
plt.xlabel("temp")
plt.ylabel("rain")
# Set axis range
plt.xlim(0,30)
plt.ylim(0,200)




