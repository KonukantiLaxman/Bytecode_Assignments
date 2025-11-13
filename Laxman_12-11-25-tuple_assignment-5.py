#!/usr/bin/env python
# coding: utf-8

# # Module 3: Data Structures Assignments
# ## Lesson 3.2: Tuples
# ### Assignment 1: Creating and Accessing Tuples
# 
# Create a tuple with the first 10 positive integers. Print the tuple.
# 
# ### Assignment 2: Accessing Tuple Elements
# 
# Print the first, middle, and last elements of the tuple created in Assignment 1.
# 
# ### Assignment 3: Tuple Slicing
# 
# Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.
# 
# ### Assignment 4: Nested Tuples
# 
# Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
# 
# ### Assignment 5: Tuple Concatenation
# 
# Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple.
# 
# ### Assignment 6: Tuple Methods
# 
# Create a tuple with duplicate elements and count the occurrences of an element. Find the index of the first occurrence of an element in the tuple.
# 
# ### Assignment 7: Unpacking Tuples
# 
# Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.
# 
# ### Assignment 8: Tuple Conversion
# 
# Convert a list of the first 5 positive integers to a tuple. Print the tuple.
# 
# ### Assignment 9: Tuple of Tuples
# 
# Create a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.
# 
# ### Assignment 10: Tuple and List
# 
# Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.
# 
# ### Assignment 11: Tuple and String
# 
# Create a tuple with the characters of a string. Join the tuple elements into a single string. Print the string.
# 
# ### Assignment 12: Tuple and Dictionary
# 
# Create a dictionary with tuple keys and integer values. Print the dictionary.
# 
# ### Assignment 13: Nested Tuple Iteration
# 
# Create a nested tuple and iterate over the elements, printing each element.
# 
# ### Assignment 14: Tuple and Set
# 
# Create a tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.
# 
# ### Assignment 15: Tuple Functions
# 
# Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.

# In[3]:
1.### Assignment 1: Creating and Accessing Tuples
# 
# Create a tuple with the first 10 positive integers. Print the tuple.
x=1,2,3,4,5,6,7,8,9,10
print(x,type(x))

2.#Assignment 2: Accessing Tuple Elements
#Print the first, middle, and last elements of the tuple created in Assignment 1.
x=1,2,3,4,5,6,7,8,9,10
print(x,type(x))
t=tuple(x)
print(t[0], t[0]+t[9]//2, t[9])


# In[65]:


3.#Assignment 3: Tuple Slicing
#Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.
x=1,2,3,4,5,6,7,8,9,10
print(x,type(x))
t=tuple(x)
print(t[0:3], t[7:10], t[2:6])


# In[22]:


#4.Assignment 4: Nested Tuples
#Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
x=((1,2,3),(4,5,6),(7,8,9))
t=tuple(x)
print("matrix:",t)
print("element at second row and third",t[1][2])


# In[23]:


#5.Assignment 5: Tuple Concatenation
#Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple.
t1=1,2,3
t2=4,5,6
print(t1+t2)


# In[29]:


### Assignment 6: Tuple Methods

#Create a tuple with duplicate elements and count the occurrences of an element. Find the index of the first occurrence of an element in the tuple.
t=1,2,3,4,3,4,5
print(t.count(3))
print(t.index(3))


# In[73]:


##Assignment 7: Unpacking Tuples
#Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.
x=1,2,3,4,5
a,b,c,d,e=x
print("a=",a, "b=",b, "c=",c, "d=",d, "e=",e)


# In[6]:
# ### Assignment 8: Tuple Conversion
# 
# Convert a list of the first 5 positive integers to a tuple. Print the tuple.
x=[1,2,3,4,5]
t=tuple(x)
print(t)

# In[7]:
### Assignment 9: Tuple of Tuples

#Create a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.
x=((1,2,3),(4,5,6),(7,8,9))
print(x,type(x))


# In[8]:


### Assignment 10: Tuple and List

#Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.
x=1,2,3,4,5
l1=list(x)
print(l1,type(l1))
l1.append(6)
t=tuple(l1)
print(t,type(t))


# In[56]:


### Assignment 11: Tuple and String

#Create a tuple with the characters of a string. Join the tuple elements into a single string. Print the string.
x="H","E","L","L","O"
s="".join(x)
print(s,type(s))


# In[58]:


### Assignment 12: Tuple and Dictionary

#Create a dictionary with tuple keys and integer values. Print the dictionary.
x={(1,2):100,(3,4):200}
print(x,type(x))


# In[60]:


### Assignment 13: Nested Tuple Iteration

#Create a nested tuple and iterate over the elements, printing each element.
x=1,2,3,(4,5,6),7,8
for ind,val in enumerate(x):
    print(val)


# In[26]:


### Assignment 14: Tuple and Set

#Create a tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.
x=1,2,3,2,3
s=set(x)
print(s)


# In[46]:


### Assignment 15: Tuple Functions

#Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.
x=1,2,3,4,5
print("minimun_value is:",t[0], "maximum_value is:",t[4],  "Sum of elements:",t[0]+t[1]+t[2]+t[3]+t[4])







