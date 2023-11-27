import numpy as np


myVector = np.array(np.int16([1, 2, 3, 4, 5]))
print(myVector)

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

b = np.array([[2, 2, 3], [5, 5, 7]])

# compare two arrays
print('Compare a and b', a == b)

# sum of two arrays
print('Sum of a and b', a + b)
# multiply two arrays
print('Multiply a and b', a * b)

# take the square root of each element
print('Square root of a', np.sqrt(a))

# sum of all elements of array a
print('Sum of all elements of a', np.sum(a))
# axis = 0 means sum of each column, get sum of each row if axis = 0
print('Sum of each column of a', np.sum(a, axis=0))
# sum of each column when axis = 1
print('Sum of each row of a', np.sum(a, axis=1))
# get just min
print('Min value of a', np.min(a))
# get the min value of each column
print('Min value of each column of a', np.min(a, axis=0))
# get the min 
print('Min value of each row of a', np.min(a, axis=1))
# get max
print("Max value of each column of a", np.max(a))
# get mean
print("Mean value of each column of a", np.mean(a))

