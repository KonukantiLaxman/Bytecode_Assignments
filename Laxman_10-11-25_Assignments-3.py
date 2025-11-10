#!/usr/bin/env python
# coding: utf-8

# # Lesson 1.2: Python Basics
# ## Topics Covered:
# - Syntax and Semantics
# - Variables and Data Types
# - Basic Operators (Arithmetic, Comparison, Logical)
# 

# ## 1. Syntax and Semantics
# 
# **Question 1:** Write a Python program to print "Hello, World!".

# In[1]:


print("Hello, World!")


# **Question 2:** Write a Python program that takes a user input and prints it.

# In[6]:


a=input("Enter the name:")
msg="My name is:"
print(msg,a)


# **Question 3:** Write a Python program to check if a number is positive, negative, or zero.

# In[14]:


a=int(input("Enter the number:"))
if(a>0):
  print("number is positive:")
if(a<0):
   print("number is negative:")
if(a==0):
 print("number is zero:")


# **Question 4:** Write a Python program to find the largest of three numbers.

# In[27]:


a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>b and a>c):
    print("the largest number is:",a)
elif(b>a and b>c):
    print("the largest number is:",b)
else:
    print("the largest number is:",c)


# **Question 5:** Write a Python program to calculate the factorial of a number.

# In[21]:


n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)


# ## 2. Variables and Data Types
# 
# **Question 6:** Create variables of different data types: integer, float, string, and boolean. Print their values and types.

# In[28]:


a,b,c,d=5,5.6,"Hi",True
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))


# **Question 7:** Write a Python program to swap the values of two variables.

# In[29]:


a,b=5,10
a,b=b,a
print(a, b)


# **Question 8:** Write a Python program to convert Celsius to Fahrenheit.

# In[5]:


a=float(input("Enter the value to convert from Celsius to Fahrenheit:"))
F=(a*1.8)+32
print(F)


# **Question 9:** Write a Python program to concatenate two strings.

# In[1]:


a=input("Enter first string:")
b=input("Enter second string:")
c=a+b
print(c)


# **Question 10:** Write a Python program to check if a variable is of a specific data type.

# In[2]:


a=10
print(a,type(a))


# ## 3. Basic Operators (Arithmetic, Comparison, Logical)
# 
# **Question 11:** Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division.

# In[3]:


a=10
b=5
print("Addition of a and b is:", a+b)
print("Subtraction of a and b is:", a-b)
print("Multiplication of a and b is:",a*b)
print("Division of a and b is:",a/b)


# **Question 12:** Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.

# In[4]:


a=10
b=5
print("a equals to b:",a==b)
print("a is not equal to b:",a!=b)
print("a is greater than b:", a>b)
print("a is less than b:", a<b)


# **Question 13:** Write a Python program to demonstrate logical operators: and, or, not.

# In[12]:


a=10
b=5
print("a logical_AND b is:",a and b)
print("a logival_OR b is:",a or b)
print("a Logical_NOT b is:",not a)


# **Question 14:** Write a Python program to calculate the square of a number.

# In[10]:


num=int(input("Enter the number:"))
print("square of a number is:", num*num)


# **Question 15:** Write a Python program to check if a number is even or odd.

# In[12]:


num=int(input("Enter the number:"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")


# **Question 16:** Write a Python program to find the sum of the first n natural numbers.

# In[19]:


a=int(input("enter the numbers:"))
n=a*(a+1)/2
print("sum of the first n natural numbers is :", n)


# **Question 17:** Write a Python program to check if a year is a leap year.

# In[36]:


year=int(input("enter the year"))
if(year%4==0 or year%100==0):
    print("year is leap year")
else:
    print("year is not leap year")


# **Question 18:** Write a Python program to reverse a string.

# In[65]:


a="Python"
b=len(a)-1
c=""
while(b>=0):
 c=c+list(a)[b]
 b=b-1
print(c)


# **Question 19:** Write a Python program to check if a string is a palindrome.

# In[8]:


a="malayalam"
b=len(a)-1
c=""
while(b>=0):
    c=c+list(a)[b]
    b=b-1
if(a==c):
    print("string is a palindrome")
else:
    print("string is not a plaindrome")


# **Question 20:** Write a Python program to sort a list of numbers in ascending order.

# In[9]:


a=[10,2,45,0,-2]
a.sort(reverse=False)
print(a)

