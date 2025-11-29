#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assignment 1: Simple if Statement
#Write a program that asks the user to input a number and prints whether the  number is positive.
n=eval(input("enter a number:"))
if n>0:
    print("number is positive")


# In[2]:


#Assignment 2: if-else Statement
#Write a program that asks the user to input a number and prints whether the number is positive or negative.
num=eval(input("enter a number:"))
if num>0:
    print("number is positive")
else:
    print("number is negative")


# In[10]:


#Assignment 3: if-elif-else Statement
#Write a program that asks the user to input a number and prints whether the number is positive, negative, or zero
num=eval(input("enter a number:"))
if num>0:
    print("number is positive")
elif num<0:
        print("number is negetive")
else:
    print("number is Zero")


# In[16]:


#Assignment 4: Nested if Statement
#Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative.
num=eval(input("enter a number:"))
if num>=0:
    if num%2==0:
        print("number is positive and even ")
    elif num%2!=0:
        print("number is positive and odd")
else:
    print("number is Negative")


# In[18]:


#Lesson 2.2: Loops
#Assignment 5: for Loop
#Write a program that prints all the numbers from 1 to 10 using a for loop.
for i in  range(1,11):
    print(i)


# In[2]:


#Assignment 6: while Loop
#Write a program that prints all the numbers from 1 to 10 using a while loop.
n=1
while n<11:
    print(n)
    n+=1
    


# In[14]:


#Assignment 7: Nested Loops
#Write a program that prints a 5x5 grid of asterisks (*) using nested loops
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
    


# In[28]:


# Assignment 8: break Statement
# Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.
sum=0
num=eval(input("enter a number:"))
while num!=0:
     sum+=num
     num=eval(input("enter a number:"))
print(sum)

    


# In[33]:


# Assignment 9: continue Statement
# Write a program that prints all the numbers from 1 to 10 except 5 using a for loop and continue statement.
num=eval(input("enter a number:"))
for num in range(1,num+1):
    if num==5:
        continue
    print(num)


# In[35]:


# Assignment 10: pass Statement
# Write a program that defines an empty function using the pass statement.
def fun():
    pass
fun()


# In[38]:


# Assignment 11: Combining Loops and Conditionals
# Write a program that asks the user to input a number and prints all the even numbers from 1 to that number using a for loop.
num=eval(input("enter a number:"))
for num in range(1,num+1):
    if num%2==0:
        print(num)


# In[1]:


# Assignment 12: Factorial Calculation
# Write a program that calculates the factorial of a number input by the user using a while loop.
num=eval(input("enter a number:"))
fact=1
while num>0:
    fact*=num
    num-=1
print(fact)    


# In[23]:


# Assignment 13: Sum of Digits
# Write a program that calculates the sum of the digits of a number input by the user using a while loop.
num=eval(input("enter a number:"))
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num=num//10
print(sum)


# In[20]:


# Assignment 14: Prime Number Check
# Write a program that checks if a number input by the user is a prime number using a for loop.

num = int(input("Enter a number: "))
count = 0

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            count+= 1
            break  
    if count == 0:
        print("Given number is prime")
    else:
        print("Given number is not prime")
else:
    print("Given number is not prime")


# In[ 25]:
# Assignment 15: Fibonacci Sequence
# Write a program that prints the first n Fibonacci numbers, where n is input by the user.
num=eval(input("enter a number:"))
x,y=0,1
for i in range(num):
    print(x,end=" ")
    x,y=y,x+y




