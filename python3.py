# KWK-python-review
python review for data science from KWK
import numpy as np
import pandas as pd

my_first_array = np.array([1,2,3])
print(my_first_array)
np.zeros(2)
np.arange(4)

#types of functions used
np.append()
np.delete()
np.sort()
random.rand()

my_array = np.array([9,10])
np.append(my_array, [9,10])
my_new_array= np.array([5,16,9,13,12, 8, 7, 17])

# sort the new array
np.sort(my_new_array)

from numpy import random

#print ten random numbers
print(random.rand(10))

print(random.rand(5,5))

np.sqrt() # Returns square root

np.exp() # Returns the exponential

np.asarray() # Converts any data type to NumPy array

array.shape() # Finds the shape of the NumPy array

np.mean() # Returns the mean of elements in the array

np.std() # Returns the standard deviation of elements in the arrasy 

np.var() # Returns the variance of elements in the array

# Creating data using lists 
names = ['Karlie', 'Taylor', 'Billie', 'Lizzo', 'Demi']
age = [ 28, 31, 19, 32, 28]
city = ["Chicago", "Wyomissing", "Los Angeles", "Detroit", "Dallas"]

friends = pd.DataFrame(dictionary)
print(friends)

# deleting the city column 
new_friends = new_friends.drop('City',axis=1)
# print the updated dataframe
print(new_friend)

new_friends.drop(1,axis=0)

new_friends['names']

new_friends[['Names','Age']]

friends[(friends['Age'] > 30) & (friends['City'] == "Detroit")]

df = pd.read_csv(r'Path where the CSV file is stored\File name.csv')
print (df)


from google.colab import files
uploaded = files.upload()

import io
sales_combined = pd.read_csv(io.BytesIO(uploaded['nameoffile.csv']))
# Dataset is now stored in a Pandas Dataframe

# creating a variable called "url" to hold link to data
url = 'https://raw.githubusercontent.com/datacult/kwk-datascience/master/data/chipotle.tsv'
    
# creating a dataframe called chipo 
chipo = pd.read_csv(url, '\t')

chipo['item_price'] = chipo['item_price'].str.replace('$', '')

# checking to see if the '$' is removed 
chipo.head()

desc = chipo["choice_description"]
check_list = isinstance(desc, list)

print(check_list)

chipo['choice_description'] = chipo['choice_description'].str.strip('[]')

chipo.fillna('NA', inplace=True)
chipo.head()

artist_timesheet = pd.DataFrame({'First_NamMeE':['Frieda','Georgia','Georgia','Yayoi','Cindy','Jenny','Petra'],
                          'Last_Name':['Khalo',"O'Keeffe","O'Keeffe",'Kusama','Sherman','Holzer','Collins'],
                             'Total Hours':[12,9,9,8,14,np.NaN,11],
                             'WEEkkly SeSSiOns':['2','3','3','1','2',np.NaN,'3'],
                             'Time of Day':['Night','Night','Day','Night','Day',np.NaN,'Day',]},
                            index=[1,2,2,3,4,5,6])
artist_timesheet

