import pandas as pd 

df = pd.read_csv("iris.csv")

print(df.Species.unique())
print(df.info())
print(df.describe())

#%% line plot
import matplotlib.pyplot as plt

df1 = df.drop(["Id"], axis = 1)

#df1.plot()
#plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "blue", label = "virginica")
plt.legend()
plt.xlabel("ID")
plt.ylabel("PetalLengthCm")
plt.plot(grid = True, linestyle = ":")
plt.show()

#%% scatter plot

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color = "red", label = "setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color = "green", label = "versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color = "blue", label = "virginica")

plt.title("Scatter Plot")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.plot()
plt.show()

#%% histogram 

plt.hist(setosa.PetalLengthCm, bins = 10)

plt.title("Histogram")
plt.legend()
plt.xlabel("PetalLengthCm Values")
plt.ylabel("Frekans")
plt.show()

#%% bar plot

import numpy as np

x = np.array([1,2,3,4,5])
y = x * 2 + 5

plt.bar(x,y)
plt.title("Bar Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#%% #subplot

df1.plot(grid = True, subplots = True)
plt.show()
