#!/usr/bin/env python
# coding: utf-8

# In[96]:


l1=[10,11,13,14]
l2=[]
for ind,val in enumerate(l1):
    l2.append(val+10)
print(l2)


# In[120]:


l1=[10,11,13,14]
l2=[5,6,7,8,9]
l3=l2
for ind,val in enumerate(l1):
    l3.insert(ind,val+l2[ind])
    del l3[ind+1]
print(l3)


# In[121]:


l1=[10,11,23,45,78,90,42,41]
l2=[]
for ind,val in enumerate(l1):
    if(val>=40):
        l2.append(val)
print(l2)


# In[93]:


l1=[10,20,15,45,89,90,11,34]
l2=[]
for ind,val in enumerate(l1):
    if(val%2==0):
        l2.append(val)
print(l2)
    


# In[ ]:




