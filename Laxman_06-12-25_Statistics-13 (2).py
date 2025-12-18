#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Find the mean of first 10 odd integers?
import statistics
n=list(range(1,20,2))
mean=statistics.mean(n)
print("Mean:",mean)


# In[2]:


#2.what is the median of following dataset?
#data=[32,6,21,10,8,11,12,36,17,16,15,18,40,24,21,23,24,24,29,16,32,31,10,30,35,32,18,39,12,20]
import statistics as stats
data=[32,6,21,10,8,11,12,36,17,16,15,18,40,24,21,23,24,24,29,16,32,31,10,30,35,32,18,39,12,20]
median=stats.median(data)
print("Median:",median)


# In[3]:


#3.identify the mode of following dataset?
#data=[21,19,62,21,66,28,66,48,79,59,28,62,63,63,48,66,59,66,94,79,19,94]
import statistics
data=[21,19,62,21,66,28,66,48,79,59,28,62,63,63,48,66,59,66,94,79,19,94]
mode=statistics.mode(data)
print("Mode:",mode)


# In[7]:


#4.Given a dataset , calculate the mean, median,mode. interpretthe result and dtermine which measures of central tendency is most appropriate for the dataset.
#Test scores of 10 students :[65,70,75,80,85,90,95,100,105,110]
import statistics
data=[65,70,75,80,85,90,95,100,105,110]
mean=statistics.mean(data)
print("Mean:",mean)
median=statistics.median(data)
print("Median",median)
try:
    mode=statistics.mode(data)
except  statistics.StatisticsError:
    mode=="No mode"
print("Mode:",mode)


# In[14]:


#5.calculate the mean, median, mode for  following dataset. Then add an outlier value 100 and recalculate the measures.Discuss how outliers affect the mean compared to median and mode.
#original dataset: [50,52,53,55,57,60,62,64,65]
#Modified dataset with outlier:[50,52,53,55,57,60,62,64,65,100]
import statistics
od=[50,52,53,55,57,60,62,64,65]
md=[50,52,53,55,57,60,62,64,65,100]
mean_od=statistics.mean(od)
mean_md=statistics.mean(md)
median_od=statistics.median(od)
median_md=statistics.mean(md)
try:
    mode_od=statistics.mode(od)
    mode_md=statistics.mode(md)
except  statistics.StatisticsError:
    mode_od="No mode"
    mode_md="No mode"
print("original_Mean:",mean_od)
print("Modified_Mean:",mean_md)
print("original_Median:",median_od)
print("Median_Median:",median_md)
print("original_Mode:",mode_od)
print("Median_Mode:",mode_md)


# In[16]:


#6.Calculate the mean and median for the following two datasets and discuss the relationships the two measures for symmetric and skewed distributations 
#Symmetric Datasets:[5,10,15,20,25]
#skewed Datasets:[5,7,10,20,100]
import statistics as stats
sym_data = [5, 10, 15, 20, 25]
skew_data = [5, 7, 10, 20, 100]
mean_sym = stats.mean(sym_data)
median_sym = stats.median(sym_data)
mean_skew = stats.mean(skew_data)
median_skew = stats.median(skew_data)
print("Symmetric Dataset:", sym_data)
print("Mean (symmetric):", mean_sym)
print("Median (symmetric):", median_sym)
print("\nSkewed Dataset:", skew_data)
print("Mean (skewed):", mean_skew)
print("Median (skewed):", median_skew)


# In[6]:


#7. A teacher recorded the marks of 15  students in a final exam. Calculate the mean, median, mode and interpret what these mesures suggest about class performance.
#Dataset=[45,50,50,60,65,70,70,70,75,80,85,90,95,100,100]
import statistics as stats
data=[45,50,50,60,65,70,70,70,75,80,85,90,95,100,100]
mean=stats.mean(data)
median=stats.median(data)
mode=stats.mode(data)
print("Mean:",mean)
print("Median:",median)
print("Mode",mode)
print("Interpretation:\n")
print("The mean score of a class is:",mean,"it means class performance is good")
print("the median score of a class is:",median,"it means half scored below and half scored above value")
print("the mode score of a class is:",mode,"it means most frequently occured among class")


# In[10]:


#8.Calculate the mode for the following dataset of colors chosen by a group of 20 people. Discuss how mode can be useful when analyzing categorical data.
#Data=["Red","Blue","Green","Blue","Red","Blue","Red","Yellow","Green","Green","Blue","Red","Yellow","Yellow","Red","Blue","Green","Yellow","Blue","Red"]
import statistics as stats
Data=["Red","Blue","Green","Blue","Red","Blue","Red","Yellow","Green","Green","Blue","Red","Yellow","Yellow","Red","Blue","Green","Yellow","Blue","Red"]
mode=stats.mode(Data)
print("Mode is:",mode)


# In[51]:


#9.calculate the range, variance and standard deviation of following dataset.
#Monthly income of 15 individuals:[2000,2500,2700,2800,3000,3200,3500,4000,4200,4500,4700,5000,5200,5500,6000]
import numpy as np
import pandas as pd
from math import sqrt
data=[2000,2500,2700,2800,3000,3200,3500,4000,4200,4500,4700,5000,5200,5500,600]
df=pd.DataFrame(data)
df
df=df.rename(columns={0:"income"})
df["μ"]=df["income"].mean()
df["income-μ"]=df["income"]-df["μ"]
df
df["(income-μ)^2"]=df["income-μ"]**2
print(df)
range=df["income"].max()-df["income"].min()
print("range is:",range)
variance=df["(income-μ)^2"].mean()
print("varaiance is:",variance)
std= sqrt(df["(income-μ)^2"].mean())
print("standard deviation is:",std)


# In[58]:


#10.Calculate the range, variance and standard deviation of following dataset. Then, introduce an outlier (100) to the dataset and recalculate the measues of dispersion. discuss how the outlier affect the spread the data.
#data=[50,55,60,62,65,70,75,80,85,90]
import numpy as np
import pandas as pd
from math import sqrt
dataset=[50,55,60,62,65,70,75,80,85,90]
df=pd.DataFrame(dataset)
df
df=df.rename(columns={0:"Data"})
df["μ"]=df["Data"].mean()
df["Data-μ"]=df["Data"]-df["μ"]
df["(Data-μ)^2"]=df["Data-μ"]**2
print(df)
range=df["Data"].max()-df["Data"].min()
print("range is:",range)
variance=df["(Data-μ)^2"].mean()
print("Vaiance is:",variance)
std= sqrt(df["(Data-μ)^2"].mean())
print("standard deviation is:",std)


# In[ ]:
#11.calculate the standard deviation for three different groups of data each representing the number of sales made by employees in a company during week. compare the standard deviation and discuss the differences.
#sales1:[5,7,10,12,15]
#sales2:[1,2,3,8,9]
#sales3:[10,15,20,25,30]
import numpy as np
sales1=[5,7,10,12,15]
sales2=[1,2,3,8,9]
sales3=[10,15,20,25,30]
std1=np.std(sales1)
std2=np.std(sales2)
std3=np.std(sales3)
print("standard deviation for group1 is:",std1)
print("standard deviation for group2 is:",std2)
print("standard deviation for group3 is:",std3)

# In[ ]:
#12.calculate the quartiles for the following datasets.
#data=[10,12,14,16,18,20,22,25,30,35,40,50]
data=[10,12,14,16,18,20,22,25,30,35,40,50]
Q1=np.percentile(data,25)
Q2=np.percentile(data,50)
Q3=np.percentile(data,75)
print("Q1 (25th percentile) is:",Q1)
print("Q2 (median) is:",Q2)
print("Q3 (75th percentile) is:",Q3)

# In[ ]:
#13.calculate the interquartile range(IQR) for the following dataset and identify the potential outliers using the 1.5*IQR rule
#data=[10,12,14,16,18,20,22,25,30,35,40,50]
import numpy as np
data=[10,12,14,16,18,20,22,25,30,35,40,50,100]
Q1=np.percentile(data,25)
Q3=np.percentile(data,75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers=[x for x in data if x<lower_bound or x>upper_bound]
print("Q1 (25th percentile) is:",Q1)
print("Q3 (75th percentile) is:",Q3)
print("interquartile range(IQR) is:",IQR)
print("lower bound is:",lower_bound)
print("upper bound is:",upper_bound)
print("potential outliers is:",outliers)

# In[ ]:
#14.Given the following dataset representing number of products sold in a store overe a week, calculate the interquartile and identify the outliers.
# data=[2,4,5,7,10,12,15,18,20,25]
import numpy as np
data=[2,4,5,7,10,12,15,18,20,25]
Q1=np.percentile(data,25)
Q3=np.percentile(data,75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3*1.5*IQR
outliers=[x for x in data if x<lower_bound or x>upper_bound]
print("Q1 (25th percentile) is:",Q1)
print("Q3 (75th percentile) is:",Q3)
print("interquartile range(IQR) is:",IQR)
print("lower bound is:",lower_bound)
print("upper bound is:",upper_bound)
print("potential outliers is:",outliers)

# In[ ]:
#15.You are given the following test scores of a 20 students in a class. Calculate the interquartile and  identify outliers.
#scores=[34,38,45,45,49,50,53,54,56,58,61,62,65,68,70,72,75,78,80,85]
#Calculate the first Quartile(Q1), third Quartile(Q3)and IQR
#identify the potential outliers based on the 1.5*IQR rule.
import numpy as np
scores=[34,38,45,45,49,50,53,54,56,58,61,62,65,68,70,72,75,78,80,85]
Q1=np.percentile(scores,25)
Q3=np.percentile(scores,75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
outliers=[x for x in scores if x<lower_bound or x>upper_bound]
print("Q1 (25th percentile) is:",Q1)
print("Q3 (75th percentile) is:",Q3)
print("interquartile range(IQR) is:",IQR)
print("lower bound is:",lower_bound)
print("upper bound is:",upper_bound)
print("potential outliers is:",outliers)

