#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Print your name 5 times using only while loop
i=1
while i<=5:
    print("Laxman")
    i+=1


# In[1]:


# 2. Print numbers 1 to 10 using only while loop. 
i=1
while i<=10:
    print(i)
    i+=1


# In[2]:


# 3. Print numbers 10 down to 1 using only while loop. 
i=10
while i>=1:
    print(i)
    i-=1


# In[5]:


# 4. Take a number from user and print its multiplication table (up to 10) using while loop. 
n=eval(input("enter any number:"))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1


# In[1]:


# 5. Keep asking for password until user enters "analytics2025" → print "Login Success!". 
password=input("enter password:")
while password!="analytics2025":
    print("invalid password!.., please enter correct password")
    password=input("enter password")
print("Login success!")
    


# In[4]:


# 6.Add numbers continuously until user enters 0, then print the sum of all entered numbers
sum=0
num=eval(input("enter any value:"))
while num!=0:
    sum+=num
    num=eval(input("enter any value:"))
print(sum)


# In[9]:


# 7. Calculate factorial of a number using only while loop (e.g., 6! = 720). 
num=eval(input("enter any value:"))
fact=1
while num>1:
    fact*=num
    num-=1
print(fact)    


# In[16]:


# 8.Reverse a number using while loop (12345 → 54321). 
num=eval(input("enter any number:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)    


# In[23]:


# 9. Number guessing game: secret = 35. Give hints "Too high"/"Too low" until correct. 
secret=int(input("enter secret key:"))
while secret!=35:
    if secret>35:
        print("Too high")
        secret=int(input("enter secret key:"))
    else:
        print("Too low")
        secret=int(input("enter secret key:"))
        print("u have gussed correct key")        


# In[1]:


# 10.Check if a number is palindrome using only while loop (no string methods). 
# 8.Reverse a number using while loop (12345 → 54321). 
num=eval(input("enter any number:"))
rev=0
i=num
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if rev==i:
    print("given number is palindrome")
else:
    print("given number is not a palindrome")


# In[12]:


# 11. Print the following pattern using only while loop:
# text
# 1
# 22
# 333
# 4444
# 55555 
i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end=" ")
        j+=1
    print("\n")
    i+=1    
  


# In[15]:


# 12. Implement a login system with maximum 3 attempts. If password is wrong 3 times →
# print "Account Blocked!". Correct password: "python123" 
password=input("enter password:")
n=0
while n<2 and password!="python123":
    print("invalid password!.., please enter correct password")
    password=input("enter password:")
    n+=1
if n!=0 and password!="python123":
    print("Account Blocked!")
else:
    print("Login succesful..!")
    


# In[33]:


# 13. Keep taking expense amounts until user enters -1, then print total expense and count of  transactions. 
total=0
count=0
expenses=eval(input("enter any amount:"))
while expenses!=-1:
    total+=expenses
    count+=1
    expenses=eval(input("enter any amount:"))
print("Total expenses:",total,"\nNumber of transactions:",count)


# In[4]:


# 14. Print only odd numbers from 1 to 20 using while loop and continue statement.
i=1
while i<=20:
    if i%2==0:
        i+=1
        continue
    print(i)
    
    i+=1


# In[8]:


# 15. Write a program using while loop to count and print the number of digits in a given positive integer (Example: 7834 → 4 digits). 
num=eval(input("enter any value:"))
count=0
if num<0:
    print("enter any positive number:")
else:
    while num>0:
        num=num//10
        count+=1
    print("number of digit in given number is:",count)


# In[9]:


#16. Write a program using while loop to calculate and print the sum of the series: 1+ 4 + 9 + 16 + … + 100 (i.e., sum of squares of first 10 natural numbers)
sum=0
i=1
while i<=10:
    sum+=i*i
    i+=1
print("sum of squatres of first 10 natural numbers is:",sum)    


# In[26]:


# 17. Print first 10 Fibonacci numbers using only while loop (0, 1, 1, 2, 3, 5, …)
i=2
a,b=0,1
print(a,b,end=" ")
while i<11:
    print(a+b,end=" ")
    a,b=b,a+b
    
    i+=1


# In[14]:


# 18. Use break when user types "stop" (case insensitive) in an infinite input loop. 
type=input("enter any value:")
while type!='stop':
    type=input("enter any value:")
print(type)


# In[21]:


# 19. What is the output?
# Python 
i = 0
while i < 3:
    print("hii")
    i+= 1
else:
    print("End")


# In[5]:


#20. Write a program to find GCD of two numbers using while loop (Euclidean algorithm)
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
if num1>num2:
   i=num1
else:
   i=num2

gcd=1
j=1
while j<=i:
   if num1%j==0 and num2%j==0:
       gcd=j
   j+=1
       
print(f'gcd of {num1} and {num2}:{gcd}')
   
   


# 
