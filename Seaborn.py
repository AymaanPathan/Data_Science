#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[109]:


df2=pd.DataFrame(np.random.randint(1,100,(4,3)),index=["Aymaan","Jack","BOB","sanaya"],columns=["DSA","Php",".net"])
df2


# In[110]:


x =df2.index
y =df2["Php"]
plt.subplot(1,2,1)
plt.plot(x, y,"g^-")
plt.xlabel("marks")
plt.ylabel("students")
plt.title("php marks ")
plt.grid(color='b', linestyle='--' )
plt.ylim(0,100)
plt.legend(['First line', 'Second line'])
plt.show()




x =df2.index
y =df2["DSA"]
plt.subplot(1,2,1)
plt.plot(x, y,"r", marker='*', linestyle='-',data=df2)
plt.xlabel("marks")
plt.ylabel("students")
plt.title("DSA marks ")
plt.grid(color='r', linestyle='--' )


# In[111]:


#legend
x =df2.index
y =df2["Php"]
plt.plot(x, y,"g^-")
plt.xlabel("student name")
plt.ylabel("student marks")
plt.title(" marks ")
y =df2["DSA"]
plt.plot(x, y,"r*-")
plt.grid(color='r', linestyle='--' )
plt.ylim(0,100)
y =df2[".net"]
plt.plot(x, y,"y*-")

plt.legend(['Php', 'DSA' ,".net"])


# In[112]:


plt.scatter(np.arange(10),np.arange(10)**2,c=np.arange(10), s=np.arange(10)**3, edgecolor="red"  )
plt.colorbar()


# In[113]:


plt.scatter(np.arange(10),np.arange(10)**2 )
plt.scatter(np.arange(10),np.arange(10)**2.1 )
plt.scatter(np.arange(10),np.arange(10)**2.2 )
plt.scatter(np.arange(10),np.arange(10)**2.3 )
plt.scatter(np.arange(10),np.arange(10)**2.4 )
plt.scatter(np.arange(10),np.arange(10)**2.5 )
plt.scatter(np.arange(10),np.arange(10)**2.6 )
plt.scatter(np.arange(10),np.arange(10)**2.7 )
plt.scatter(np.arange(10),np.arange(10)**2.8 )
plt.scatter(np.arange(10),np.arange(10)**2.9 )
plt.scatter(np.arange(10),np.arange(10)**3 )


# In[114]:


plt.stem([8,3,0,6,0,2,3,2,4,0],markerfmt="r*")
plt.stem([8,7,8,7,0,2,1,7,1,0],markerfmt="g*")


# In[115]:


df1=pd.DataFrame(np.random.randint(1,100,(4,3)),index=["Person1","Person2","Person3","Person4"],columns=["DSA","Php",".net"])
df1


# In[116]:


sns.displot(df1)


# In[117]:


penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")


# In[118]:


sns.jointplot(x=df1["DSA"],y=df1["Php"],data=df1)


# In[119]:


tips = sns.load_dataset("tips")
tips.head()


# In[120]:


sns.distplot(tips['total_bill'])


# In[121]:


sns.displot(tips['total_bill'])


# In[122]:


sns.distplot(tips['total_bill'],kde=False,bins=15)


# In[123]:


#Jointplot
#parameters in jointplot fpr 'kind' are: scatter, reg, resid, kde, hex
sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')


# In[124]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')


# In[125]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')


# In[126]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='resid')


# In[127]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')


# In[128]:


#pairplot: allows us to plot pairwise relationships between variables within a dataset
sns.pairplot(tips)


# In[129]:


sns.pairplot(tips,hue='sex',palette='deep')


# In[ ]:


sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)


# In[ ]:


sns.clustermap(tips.corr())  


# In[ ]:


sns.boxplot(data=tips)


# In[ ]:


sns.barplot(data=tips )


# In[20]:


sns.boxplot(x="day",y="total_bill",hue="smoker",data=tips,palette="coolwarm")


# In[24]:


sns.factorplot(data=tips)


# In[21]:


sns.stripplot(data=tips)


# In[20]:


sns.swarmplot(data=tips)


# In[25]:


titanic=sns.load_dataset("titanic")


# In[26]:


titanic.head()


# In[27]:


sns.jointplot(x=titanic.fare , y=titanic.age ,data=titanic)


# In[28]:


sns.displot(data=titanic.fare)


# In[29]:


sns.boxplot(x=titanic.age ,y=titanic.deck ,data=titanic)


# In[ ]:


sns.swarmplot(data=titanic.pclass)


# In[31]:


sns.countplot(data=titanic)

