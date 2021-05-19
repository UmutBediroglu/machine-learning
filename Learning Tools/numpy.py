import numpy as np

array1 = np.array([1,2,3,4,5,6]) # 6*1 vector
print(array1.shape)

array2 =  array1.reshape(2, 3)
print("Shape:", array2.shape)
print("Dimension:", array2.ndim)

print("Data Type:", array2.dtype.name)
print("Size:", array2.size)

array3 = np.zeros((3,4))
array3[0,0] = 5
print(array3)

array4 = np.ones((3,4))
print(array4)

array5 = np.empty((3,2))
print(array5)

array6 = np.arange(10,50,5)
print(array6)

#%% numpy basic operations

x = np.array([1,2,3])
y = np.array([4,5,6])

print(x+y)
print(x-y)
print(x**2)

print(np.sin(x))

print(x < 2)

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2,3],[4,5,6]])

#transpose
y = y.T
print(y)

#matrix product
z = x.dot(y)
print(z)

#exp
k = np.exp(x)
print(k)

array7 = np.random.random((5,5))
print(array7)

print(array7.sum())
print(array7.sum(axis = 0))
print(array7.sum(axis = 1))


print(array7.min())
print(array7.max())

print(np.sqrt(array7))
print(np.square(array7))

#%% indexing and slicing

array1 = np.array([1,2,3,4,5,6])
print(array1[0:3])

reverse_array = array1[::-1]
print(reverse_array)

array2 = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
print(array2[1,5])

print(array2[-1,:])
print(array2[:,-1])

#%% shape manipulation

array1 = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])

#flatten
array2 = array1.ravel()
print(array2)

array3 = array2.reshape(3,4) # not change in data
print(array3)

array4 = array2.resize(2,6) # change in data
print(array4)

arrayT = array3.T
print(arrayT)

#%% stacking arrays

array1 = np.array([[1,2,3],[4,5,6]])
array2 = np.array([[-1,-2,-3],[-4,-5,-6]])

#vertical
array3 = np.vstack((array1, array2))
print(array3)

#horizontal
array4 = np.hstack((array1, array2))
print(array4)

#%% # convert and copy array

list1 = [1,2,3,4] # list
array1 = np.array(list1) # array
list2 = list(array1) # list


# copy the array
array2 = np.array([5,6,7,8])
array3 = array2.copy()

