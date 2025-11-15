#!/usr/bin/env python
# coding: utf-8

# # Module 3: Data Structures Assignments
# ## Lesson 3.1: Lists
# ### Assignment 1: Creating and Accessing Lists
# 
# Create a list of the first 20 positive integers. Print the list.
# 
# ### Assignment 2: Accessing List Elements
# 
# Print the first, middle, and last elements of the list created in Assignment 1.
# 
# ### Assignment 3: List Slicing
# 
# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
# 
# ### Assignment 4: List Comprehensions
# 
# Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
# 
# ### Assignment 5: Filtering Lists
# 
# Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.
# 
# ### Assignment 6: List Methods
# 
# Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.
# 
# ### Assignment 7: Nested Lists
# 
# Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
# 
# ### Assignment 8: List of Dictionaries
# 
# Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.
# 
# ### Assignment 9: Matrix Transposition
# 
# Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.
# 
# ### Assignment 10: Flattening a Nested List
# 
# Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.
# 
# ### Assignment 11: List Manipulation
# 
# Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.
# 
# ### Assignment 12: List Zipping
# 
# Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.
# 
# ### Assignment 13: List Reversal
# 
# Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.
# 
# ### Assignment 14: List Rotation
# 
# Write a function that rotates a list by n positions. Print the original and rotated lists.
# 
# ### Assignment 15: List Intersection
# 
# Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list.

# In[1]:


#Assignment 1: Creating and Accessing Lists
#Create a list of the first 20 positive integers. Print the list.
l1=list(range(1,21))
print(l1)


# In[5]:


#Assignment 2: Accessing List Elements
#Print the first, middle, and last elements of the list created in Assignment 1.
print("first element:",l1[0])
print("middle element:",l1[len(l1)//2])
print("Last element:",l1[-1])


# In[14]:


#Assignment 3: List Slicing
#Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1
print("first five elements:",l1[1:6])
print("last five elements:",l1[-5::1])
print("elements from index 5 to 15 of list:",l1[5:16])


# In[26]:


#Assignment 4: List Comprehensions
#Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
l1=list(range(1,11))
l2=list()
for i,val in enumerate(l1):
    l2.append(val*val)
print(l2)


# In[28]:


### Assignment 5: Filtering Lists

#Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.
l1=list(range(1,11))
l2=list()
for i,val in enumerate(l1):
    if(val%2==0):
        l2.append(val)
print(l2)        


# In[36]:


### Assignment 6: List Methods

#Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.
l1=[5,46,35,24,13,25,57,90]
l1.sort()
print("Ascending order:",l1)
l1.sort(reverse=True)
print("Descending order:",l1)


# In[61]:


### Assignment 7: Nested Lists

#Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
l1=[[1,2,3],[4,5,6],[7,8,9]]
for i,val in enumerate(l1):
    for j,val in enumerate(l1):
        print(l1[i][j],end=" ")
    print("\n")
print("second row and third column:",l1[1][2])    


# In[4]:


### Assignment 8: List of Dictionaries

#Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.
l1=[{"Laxman":85},{"Sai":88},{"Madhav":85}]
print(l1)


# In[80]:


### Assignment 9: Matrix Transposition

#Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.
print("original matrix:")
l1=[[1,2,3],[4,5,6],[7,8,9]]
for i,val in enumerate(l1):
    for j,val in enumerate(l1):
        print(l1[i][j],end=" ")
    print("\n")
print("Transpose matrix:")
for j,val in enumerate(l1):
    for i,val in enumerate(l1):
        print(l1[i][j],end=" ")
    print("\n")


# In[ ]:


### Assignment 10: Flattening a Nested List

#Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.


# In[92]:


### Assignment 11: List Manipulation

#Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.
l1=list(range(1,11))
l1.remove(l1[2])
l1.remove(l1[4])
l1.remove(l1[6])
l1.insert(5,99)
print(l1)


# In[ ]:


### Assignment 12: List Zipping

#Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.


# In[13]:


### Assignment 13: List Reversal

#Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.
l1=list(range(1,6))
print(l1)
l2=list()
l2=l1[-1::-1]
print(l2)


# In[15]:


### Assignment 14: List Rotation

#Write a function that rotates a list by n positions. Print the original and rotated lists.

l1=list(range(1,11))
print(l1)
for i,val in enumerate(l1):
    if()


# In[5]:


### Assignment 15: List Intersection

#Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list.
        

