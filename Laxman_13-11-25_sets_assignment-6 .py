#!/usr/bin/env python
# coding: utf-8

# # Module 3: Data Structures Assignments
# ## Lesson 3.3: Sets
# ### Assignment 1: Creating and Accessing Sets
# 
# Create a set with the first 10 positive integers. Print the set.
# 
# ### Assignment 2: Adding and Removing Elements
# 
# Add the number 11 to the set created in Assignment 1. Then remove the number 1 from the set. Print the modified set.
# 
# ### Assignment 3: Set Operations
# 
# Create two sets: one with the first 5 positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.
# 
# ### Assignment 4: Set Comprehensions
# 
# Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.
# 
# ### Assignment 5: Filtering Sets
# 
# Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.
# 
# ### Assignment 6: Set Methods
# 
# Create a set with duplicate elements and remove the duplicates using set methods. Print the modified set.
# 
# ### Assignment 7: Subsets and Supersets
# 
# Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.
# 
# ### Assignment 8: Frozenset
# 
# Create a frozenset with the first 5 positive integers. Print the frozenset.
# 
# ### Assignment 9: Set and List Conversion
# 
# Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set.
# 
# ### Assignment 10: Set and Dictionary
# 
# Create a dictionary with set keys and integer values. Print the dictionary.
# 
# ### Assignment 11: Iterating Over Sets
# 
# Create a set and iterate over the elements, printing each element.
# 
# ### Assignment 12: Removing Elements from Sets
# 
# Create a set and remove elements from it until it is empty. Print the set after each removal.
# 
# ### Assignment 13: Set Symmetric Difference Update
# 
# Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.
# 
# ### Assignment 14: Set Membership Testing
# 
# Create a set and test if certain elements are present in the set. Print the results.
# 
# ### Assignment 15: Set of Tuples
# 
# Create a set containing tuples, where each tuple contains two elements. Print the set.

# In[1]:


#Assignment 1: Creating and Accessing Sets
#Create a set with the first 10 positive integers. Print the set.
s={1,2,3,4,5,6,7,8,9,10}
print(s,type(s))


# In[2]:


#Assignment 2: Adding and Removing Elements
#Add the number 11 to the set created in Assignment 1. Then remove the number 1 from the set. Print the modified set.
s={1,2,3,4,5,6,7,8,9,10}
print(s,type(s))
s.add(11)
s.remove(1)
print(s,type(s))


# In[5]:


#Assignment 3: Set Operations
#Create two sets: one with the first 5 positive integers and another with the first 5 even integers. Perform and print the results of union, intersection, difference, and symmetric difference operations on these sets.
s1={1,2,3,4,5}
s2={0,2,4,6,8}
s3=s1.union(s2)
print("Union is:",s3,type(s3))
s4=s1.intersection(s2)
print("Intersection:",s4,type(s4))
s5=s1.difference(s2)
print("difference:",s5,type(s5))


# In[89]:


#Assignment 4: Set Comprehensions
#Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.
s1={1,2,3,4,5,6,7,8,9,10}
s2=set()
for val in range(1,11):
    s2.add(val*val)
print(s2,type(s2))    
        
    


# In[80]:


### Assignment 5: Filtering Sets

#Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.
s1={1,2,3,4,5,6,7,8,9,10}
s2=set()
for val in range(2,11,2):
    if(val%2==0):
        s2.add(val)
print(s2)
    


# In[40]:


## Assignment 6: Set Methods

#Create a set with duplicate elements and remove the duplicates using set methods. Print the modified set.
s1={1,2,3,2,3,4,5}
s2=s2.union(s1)
print(s2)


# In[5]:


### Assignment 7: Subsets and Supersets

#Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.
s1={1,2,3,4,5}
s2={1,2,3}
s3=s2.issubset(s1)
print("s2 is subset of s1:",s3)
s4=s1.issuperset(s1)
print("s1 is superset of s2",s4)


# In[ ]:


#Assignment 8: Frozenset
#Create a frozenset with the first 5 positive integers. Print the frozenset.
###Skip


# In[46]:


### Assignment 9: Set and List Conversion

#Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set.
s={1,2,3,4,5}
print(s,type(s))
l1=list(s)
l1.append(6)
print(l1,type(l1))
s1=set(l1)
print("Resulting set:",s1)


# In[59]:


### Assignment 10: Set and Dictionary

#Create a dictionary with set keys and integer values. Print the dictionary.
x={1:10,2:20,3:30}
print(x)


# In[60]:


### Assignment 11: Iterating Over Sets

#Create a set and iterate over the elements, printing each element.
s={1,2,3,4,5,6}
for val in enumerate(s):
    print(val)


# In[62]:


### Assignment 12: Removing Elements from Sets

#Create a set and remove elements from it until it is empty. Print the set after each removal
s={10,"Lucky",True}
print(s,type(s))
s.pop()
s.pop()
s.pop()
print(s,type(s))


# In[ ]:


### Assignment 13: Set Symmetric Difference Update

#Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.


# In[16]:


### Assignment 14: Set Membership Testing

#Create a set and test if certain elements are present in the set. Print the results.
s={10,"Lucky",34.56,True}
s.remove(10)
print(s)


# In[71]:


### Assignment 15: Set of Tuples

#Create a set containing tuples, where each tuple contains two elements. Print the set.
s={(10,"Lucky"),(34.56,True),("HYD",20)}
print(s,type(s))


# In[ ]:




