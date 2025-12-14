#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Find the mean of first 10 odd integers?
import statistics as stats
n=list(range(1,20,2))
mean=stats.mean(n)
print("Mean:",mean)


# In[2]:


#2.what is the median of following dataset?
#data=[32,6,21,10,8,11,12,36,17,16,15,18,40,24,21,23,24,24,29,16,32,31,10,30,35,32,18,39,12,20]
import statistics
data=[32,6,21,10,8,11,12,36,17,16,15,18,40,24,21,23,24,24,29,16,32,31,10,30,35,32,18,39,12,20]
median=statistics.median(data)
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


# In[ ]:




