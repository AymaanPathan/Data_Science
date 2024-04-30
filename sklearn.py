#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[5]:


train = pd.read_csv("titanic_train.csv")


# In[7]:


train.head()


# In[8]:


train['Age']=train['Age'].fillna(method='ffill')


# In[9]:


sns.heatmap(train.isnull())


# In[10]:


train.drop('Cabin',axis = 1, inplace = True)


# In[11]:


train.head()


# In[12]:


sex = pd.get_dummies(train['Sex'])


# In[13]:


train.drop(['Sex','Embarked','Name','Ticket'],axis = 1, inplace = True)


# In[14]:


sex


# In[15]:


from sklearn.model_selection import train_test_split


# In[16]:


train.drop('Survived', axis = 1)


# In[17]:


x_train, x_test, y_train, y_test = train_test_split(train.drop('Survived',axis = 1),train['Survived'], test_size = 0.30,
                                                   random_state = 101)


# In[18]:


from sklearn.linear_model import LogisticRegression


# In[19]:


logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)


# In[20]:


prediction = logmodel.predict(x_test)


# In[21]:


prediction


# In[22]:


from sklearn.metrics import classification_report, confusion_matrix


# In[25]:


print(classification_report(y_test,prediction))


# In[27]:


print(confusion_matrix(y_test,prediction))


# In[33]:


from sklearn.tree import DecisionTreeClassifier


# In[34]:


dtree = DecisionTreeClassifier()


# In[35]:


dtree.fit(x_train,y_train)


# In[39]:


predict_tree = dtree.predict(x_test)


# In[40]:


from sklearn.metrics import classification_report,confusion_matrix


# In[41]:


print (classification_report(y_test,prediction))


# In[44]:


print (confusion_matrix(y_test, prediction))


# In[45]:


from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(x_train,y_train)


# In[46]:


rfc


# In[47]:


rfc_pred = rfc.predict(x_test)


# In[48]:


print(confusion_matrix(y_test,rfc_pred))


# In[49]:


print (classification_report(y_test,rfc_pred))


# In[ ]:




