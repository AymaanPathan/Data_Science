#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1d array
import numpy as np
a=np.arange(0,10)
a


# In[3]:


#2d array
b=np.arange(0,9).reshape(3,3)
b


# In[4]:


#3d array
c=np.arange(0,12).reshape(3,2,2)
c


# In[5]:


#to know the dimensions
print(a.ndim)
print(b.ndim)
print(c.ndim)


# In[6]:


marks=np.random.randint(0,100,20)
marks


# In[7]:


aes=np.sort(marks)
aes


# In[8]:


#deep copying
co=np.copy(aes)
co


# In[9]:


#
identity=np.eye(5).reshape(25)
identity


# In[10]:


identity=np.eye(5).flatten()
identity


# In[11]:


identity=np.eye(5).ravel()
identity


# In[12]:


get_ipython().run_line_magic('pinfo', 'np.ravel')


# In[13]:


get_ipython().run_line_magic('pinfo', 'identity.flatten')


# In[14]:


np.append(b,[[13,11,10]],axis=0)


# In[15]:


np.eye(4)+4


# In[16]:


farr=np.random.uniform(1,20,5)
farr


# In[17]:


np.ceil(farr)


# In[18]:


np.floor(farr)


# In[19]:


np.round(farr,decimals=3)


# In[20]:


mat=np.arange(0,25).reshape(5,5)
mat


# In[21]:


np.min(mat)


# In[22]:


np.max(mat)


# In[23]:


np.std(mat)


# In[24]:


null_vector=np.arange(0,11,dtype=float)
null_vector


# In[25]:


null_vector[:]='NaN'
null_vector


# In[26]:


null_vector[6]=200
null_vector


# In[27]:


#1d array vector
arr_vector=np.arange(100,151)
arr_vector


# In[28]:


#To reverse an array
np.flip(arr_vector)


# In[29]:


#returns indices for a condtion
list=[1,0,2,0,0,4,0,8]
arr=np.array(list)
np.where(arr>0)


# In[30]:


n=np.ones(100).reshape(10,10)
n[1:9,1:9]=0
n


# In[31]:


import numpy as np
np.linspace(0,1,10)


# In[32]:


get_ipython().run_line_magic('pinfo', 'np.random.uniform')


# In[33]:


import numpy as np
list=[1,2,3]
np.array(list)


# In[ ]:





# In[ ]:




