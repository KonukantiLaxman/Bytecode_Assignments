#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Login Verification: Check if the entered password equals 'admin123'.
password='admin123'
user_password=input("enter password:")
if user_password==password:
    print("correct password")
else:
    print("incorrect password")


# In[5]:


# 2. Age Eligibility: Check if age ≥ 18 for A-rated movie.
age=int(input("enter age:"))
if age>=18:
    print("A-rated movie")
else:
    print("not eligible")


# In[6]:


# 3. Mobile Recharge Offer: ₹199 or above → free 2GB data coupon.
offer=int(input("enter Recharge offer:"))
if offer>=199:
    print("free 2GB data coupon")
else:
    print("No coupon applicable")


# In[10]:


# 4. Student Grade Checker: Assign grades based on marks.
marks=int(input("enter marks:"))
if marks>=90:
    print("Grade: A","Excellent")
elif marks>=70:
    print("Grade :B","good")
else:
    print("Grade: F","Failed")


# In[12]:


# 5. Temperature Alert System: Categorize weather by temperature.
temp=int(input("enter temperature:"))
if temp>20:
    print("Its too sunny")
else:
    print("Its cold")


# In[14]:


# 6. Credit Card Eligibility: Salary and CIBIL nested check.
Cibil=700
salary=30000
emp_salary=int(input("enter Employee Salary:"))
if emp_salary>=30000:
    emp_cibil=int(input("enter Employee cibil Score:"))
    if emp_cibil>=700:
        print("Eligible for credit card")
    else:
        print("insufficient cibil score")
else:
    print("ur Not Eligible due to Insufficient salary")
    


# In[18]:


# 7. ATM Withdrawal Validator: Check balance + multiple of 100.
balance=50000
withdraw=int(input("Enter Amount"))
if withdraw<=balance:
    if(balance%10==0):
        print("Transaction Succesful...")
    else:
        print("enter balance in multiple of 100")
else:
    print("Insufficient Balnace")


# In[35]:


# 8. Mobile Number Validator: Length 10 and starts with 6/7/8/9.
number=int(input("enter mobile number:"))
mobileno=str(number)
if len(mobileno)==10:
    if mobileno[0]=='6':
        print("mobile Number is validate")
    elif mobileno[0]=='7':
        print("mobile Number is validate")
    elif mobileno[0]=='8':
        print("mobile Number is validate")
    elif mobileno[0]=='9':
        print("mobile Number is validate")
    else:
        print("number starts with 6/7/8/9")
else:
    print("enter 10 digits mobile number")


# In[10]:


#9.Electricity Bill Category: Use match-case for type.
# Electricity Bill Category using match-case

units = int(input("Enter units consumed: "))
ch = input("Enter choice (home/shop/industry): ")
match ch:
    case "home":
        rate = 5  
        print("Category: Domestic")
    case "shop":
        rate = 8       
        print("Category: Commercial")
    case "industry":
        rate = 10       
        print("Category: Industrial")
    case _:
        print("Invalid connection type!")
        rate = 0

bill = units * rate
print(f"Total Bill Amount: ₹{bill}")


# In[40]:


# 10. Simple Calculator: Use match-case for +, -, *, /.
num1=eval(input("enter first number:"))
num2=eval(input("enter second number:"))
ch=input("enter operator(+,-,*,/):")
match(ch):
    case'+':
        print(f' {num1}+{num2} is: {num1+num2}')
    case '-':
        print(f' {num1}-{num2} is: {num1-num2}')
    case '*':
        print(f' {num1}*{num2} is: {num1*num2}')
    case '/':
        print(f' {num1}/{num2} is:{num1/num2}')
    case _:
        print("Invalid operator")
              
    



# In[ ]:




