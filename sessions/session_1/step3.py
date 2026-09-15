#Slicing Array
'''


Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end:step].[start:stop:step]

If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
'''
import numpy as np
#Creating a list and converting it to a ndarray
a_list = [1,2,3,4,5,6,7,8,9,10]
a_array = np.array(a_list)

#Slicing

sliced_array1 = a_array[0:5:2]
sliced_array2 = a_array[3:7]
sliced_array3 = a_array[5:]
sliced_array4 = a_array[:5]
sliced_array5 = a_array[-1:-6:-2] #negative slice
sliced_array6 = a_array[::2]


#Print
print(sliced_array1)
print(sliced_array2)
print(sliced_array3)
print(sliced_array4)
print(sliced_array5)
print(sliced_array6)

#----------------------slicing 2-D arrays----------------------
b_array=np.array([[1,2,3,4],[5,6,7,8]])
#                     0          1
#From the second element, slice elements from index 1 to index 3 (not included)
print(b_array[1, 1:3])
#         [.,.,.,.],[.,6,7,.]
#From both elements, return index 2:4
print(b_array[0:2 , 2:4])
#         [.,.,3,4],[.,.,7,8]

#Question ? 
print(b_array[0:2, 2]) # [[?],[?]]