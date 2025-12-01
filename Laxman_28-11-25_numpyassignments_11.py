#!/usr/bin/env python
# coding: utf-8

# # Module: NumPy Assignments
# ## Lesson: NumPy
# ### Assignment 1: Array Creation and Manipulation
# 
# 1. Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. Replace all the elements in the third column with 1.
# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.
# 
# ### Assignment 2: Array Indexing and Slicing
# 
# 1. Create a NumPy array of shape (6, 6) with values from 1 to 36. Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.
# 2. Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.
# 
# ### Assignment 3: Array Operations
# 
# 1. Create two NumPy arrays of shape (3, 4) filled with random integers. Perform element-wise addition, subtraction, multiplication, and division.
# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Compute the row-wise and column-wise sum.
# 
# ### Assignment 4: Statistical Operations
# 
# 1. Create a NumPy array of shape (5, 5) filled with random integers. Compute the mean, median, standard deviation, and variance of the array.
# 2. Create a NumPy array of shape (3, 3) with values from 1 to 9. Normalize the array (i.e., scale the values to have a mean of 0 and a standard deviation of 1).
# 
# ### Assignment 5: Broadcasting
# 
# 1. Create a NumPy array of shape (3, 3) filled with random integers. Add a 1D array of shape (3,) to each row of the 2D array using broadcasting.
# 2. Create a NumPy array of shape (4, 4) filled with random integers. Subtract a 1D array of shape (4,) from each column of the 2D array using broadcasting.
# 
# ### Assignment 6: Linear Algebra
# 
# 1. Create a NumPy array of shape (3, 3) representing a matrix. Compute its determinant, inverse, and eigenvalues.
# 2. Create two NumPy arrays of shape (2, 3) and (3, 2). Perform matrix multiplication on these arrays.
# 
# ### Assignment 7: Advanced Array Manipulation
# 
# 1. Create a NumPy array of shape (3, 3) with values from 1 to 9. Reshape the array to shape (1, 9) and then to shape (9, 1).
# 2. Create a NumPy array of shape (5, 5) filled with random integers. Flatten the array and then reshape it back to (5, 5).
# 
# ### Assignment 8: Fancy Indexing and Boolean Indexing
# 
# 1. Create a NumPy array of shape (5, 5) filled with random integers. Use fancy indexing to extract the elements at the corners of the array.
# 2. Create a NumPy array of shape (4, 4) filled with random integers. Use boolean indexing to set all elements greater than 10 to 10.
# 
# ### Assignment 9: Structured Arrays
# 
# 1. Create a structured array with fields 'name' (string), 'age' (integer), and 'weight' (float). Add some data and sort the array by age.
# 2. Create a structured array with fields 'x' and 'y' (both integers). Add some data and compute the Euclidean distance between each pair of points.
# 
# ### Assignment 10: Masked Arrays
# 
# 1. Create a masked array of shape (4, 4) with random integers and mask the elements greater than 10. Compute the sum of the unmasked elements.
# 2. Create a masked array of shape (3, 3) with random integers and mask the diagonal elements. Replace the masked elements with the mean of the unmasked elements.

# In[ ]:





# In[6]:


# Assignment 1: Array Creation and Manipulation
# Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. Replace all the elements in the third column with 1.
# Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.
print('==array of shape (5, 5) filled with random integers between 1 and 20==')
import numpy as np
import random 
a=np.random.randint(1,20,[5,5])
print(a)
print('==Replacing all the elements in the third column with 1.==')
a[:,2]=1
print(a)
# Create a NumPy array of shape (4, 4) with values from 1 to 16. 
print('==array of shape (4,4) filled with values from 1 and 16 ')
b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(b)
#Replace the diagonal elements with 0.
print('==Replacing the diagonal elements with 0.==')
for i in range(0,4):
    for j in range(0,4):
        if i==j:
            b[i][j]=0
print(b)


# In[26]:


# Assignment 2: Array Indexing and Slicing
# Create a NumPy array of shape (6, 6) with values from 1 to 36. Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.
# Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.
import numpy as np
a=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]])
print(a)
for i in range(0,6):
    for j in range(0,6):
        print(a(3:5))


# In[44]:


# Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.
a=np.random.randint(1,10,[5,5])
print(a)
print(a[0],a[3])


# In[20]:


# ### Assignment 3: Array Operations

# 1. Create two NumPy arrays of shape (3, 4) filled with random integers. Perform element-wise addition, subtraction, multiplication, and division.
print("==First numpy array==")
a=np.random.randint(1,10,[3,4])
print(a)
print("==Second numpy array==")
b=np.random.randint(1,10,[3,4])
print(b)
print("Addition of two numpy arrays are:")
print(a+b)
print("Subtraction of two numpy arrays are:")
print(a-b)
print("multiplication of two numpy arrays are:")
print(a*b)
print("division of two numpy arrays are:")
print(a//b)



# In[34]:


# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Compute the row-wise and column-wise sum.
b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(b)
sum1=0
sum2=0
for i in range(0,4):
    for j in range(0,4):
        sum1+=b[i]
    print(sum1)
    sum2+=b[j]
print(sum2)
        


# In[ ]:




