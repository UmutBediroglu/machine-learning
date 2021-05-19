import pandas as pd 

dict = {"Name": ["John", "Marry", "Jessie", "Alice"],
        "Age": [45, 27, 25, 45],
        "Payment": [500, 600, 700, 150]}

dataFrame1 = pd.DataFrame(dict)
head1 = dataFrame1.head()

#%% basic method

print(dataFrame1.columns) # write columns name
print(dataFrame1.info())

print(dataFrame1.dtypes) # columns type
print(dataFrame1.describe()) # data analysis

#%% # indexing and slicing

print(dataFrame1["Name"])

dataFrame1["newFeature"] = [-1, -2, -3, -4]

print(dataFrame1.loc[:1, "Age":"Payment"])

print(dataFrame1.iloc[:1, 1:3])

#%% # filtering

filter1 = dataFrame1.Payment > 200
filter2 = dataFrame1.Age < 26

filtering_data = dataFrame1[filter1 & filter2]

print(filtering_data)

print(dataFrame1[dataFrame1.Age < 30])

#%% # list comprehension
import numpy as np

mean_value = dataFrame1.Payment.mean()
mean_value_numpy = np.mean(dataFrame1.Payment)

dataFrame1["low_Payment"] = ["Hight" if mean_value < x else "Low" 
                            for x in dataFrame1.Payment]

dataFrame1.columns = [ y.lower() for y in dataFrame1.columns]

#%% # concatenating data

dataFrame1.drop(["newfeature"], axis = 1, inplace = True)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical
dataFrame2 = pd.concat([data1, data2], axis = 0)

#horizontal
dataFrame3 = pd.concat([data1, data2], axis = 1)

#%% # transforming data

dataFrame1["agex2"] = [z*2 for z in dataFrame1.age] 

# apply()
def multiply (k):
    return k*2

dataFrame1["apply_method"] = dataFrame1.age.apply(multiply)
