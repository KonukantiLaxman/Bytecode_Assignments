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
        bill=units*5  
        print("Category: Domestic",bill)
    case "shop":
        bill=units*8       
        print("Category: Commercial",bill)
    case "industry":
        bill=units*10       
        print("Category: Industrial",bill)
    case _:
        print("Invalid connection type!")
        


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
              
    

# 1. Core Billing Logic (Using if-else and if)
# The most fundamental part is calculating the total bill based on item prices and quantity.
item_name=input("enter item name:")
price=eval(input("enter price of item:"))
qty=eval(input("enter the quantity:"))
if qty>0:
    subtotal=price*qty
    print("subtotal:", subtotal)
else:
    print("invalid quantity")

if qty>10:
    discount=0.5*subtotal
    print("quantity discount:",discount)
else:
    discount=0
    print("quantity discount:",discount)

loyal=input("is the customer is loyal :(yes/no):")

total=subtotal-discount
if loyal=="yes":
    l_discount=0.10*total
    print("Loyal discount:",l_discount)
else:
    l_discount=0
    print("Loyal discount:",l_discount)

final_bill=total-l_discount
print("final bill",final_bill)

#2. Tiered Discounts & Surcharges (Using if-elif-else / match-case)
# This adds complexity by handling multiple possible states or ranges for the final total.
total=eval(input("enter total purchase amount:"))
payment=input("enter payment mode(credit/debit/cash):")
if total<100:
    discount=0
elif total<500:
    discount=0.05*total
elif total<1000:
    dicount=0.10*total
else:
    dicount=0.15*total
fee=0
cash_discount=0
match(payment):
    case 'credit':
        fee=0.2*total
        final=total-fee-discount-cash
        print("final Amount:",final)
    case 'debit':
        fee=0.01*total
        final=total-fee-dicount-cash
        print("final Amount:",final)
    case 'cash':
        cash_discount=5
        final=total-fee-dicount-cash
        print("final Amount:",final)
    case _:
        print("invalid payment mode:")
    
    
##3.Shipping/Delivery Fees:
custid=input("enter customer id:")
total=int(input("enter amount:"))
is_delivery=input("delivery is applicable(yes/no):")
delivery_fee=0
if is_delivery=='yes':
    if total>500:
        delivery_fee=0
    else:
        delivery_fee=50
else:
    delivery_fee=0
    print("no delivery and no fee")

is_premium=input("customer is premium member(yes/no):")
bonus_points=0
normal_points=0
premium_discount=0
if is_premium=='yes':
    if total>200:
        bonus_points=50
    else:
        bonus_points=10
    premium_discount=0.05*total
    total-=premium_discount
    print("you have applied premium discount:",premium_discount)
else:
 normal_points=5
 print("you have applied normal points:",normal_points)
print("total amount:",total)
        
     
    


# In[ ]:

#4. Tax/VAT Calculation (Using match-case or if-elif-else)
subtotal=int(input("enter subtotal:"))
ch=input("enter choice(essential/luxury goods/electronics):")
match ch:
    case 'essential':
        tax=subtotal*0.05
        total=subtotal+tax
        print("total price of product is:",total)
    case 'luxury goods':
        tax=subtotal*0.20
        total=subtotal+tax
        print("total price of product is:",total)
    case 'electronics':
        tax=subtotal*0.12
        total=subtotal+tax
        print("total price of product is:",total)
 


