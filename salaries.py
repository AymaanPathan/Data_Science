#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # SF Salaries Exercise - Solutions
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[6]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[7]:


sal = pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **

# In[8]:


sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[9]:


sal.info() # 148654 Entries


# **What is the average BasePay ?**

# In[10]:


sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[11]:


sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[12]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[13]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[14]:


sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()] #['EmployeeName']
# or
# sal.loc[sal['TotalPayBenefits'].idxmax()]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[15]:


sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].min()] #['EmployeeName']
# or
# sal.loc[sal['TotalPayBenefits'].idxmax()]['EmployeeName']

## ITS NEGATIVE!! VERY STRANGE


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[16]:


sal.groupby('Year').mean()['BasePay']


# ** How many unique job titles are there? **

# In[17]:


sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[18]:


sal['JobTitle'].value_counts().head(5)


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[19]:


sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1) # pretty tricky way to do this...


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[20]:


def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False


# In[21]:


sum(sal['JobTitle'].apply(lambda x: chief_string(x)))


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[22]:


sal['title_len'] = sal['JobTitle'].apply(len)


# In[23]:


sal[['title_len','TotalPayBenefits']].corr() # No correlation.


# In[ ]:




