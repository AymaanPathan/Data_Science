#!/usr/bin/env python
# coding: utf-8
Pandas
# In[208]:


#to store marks of students in a series
import pandas as pd
marks_list=[81,75,81]
labels=['DSA','java','Python']
a=pd.Series(data=marks_list, index=labels)
print(a)


# In[209]:


dict={"Name":"Aymaan Pathan","Rollno":22000545, "Program":"BCA"}
s=pd.Series(dict)
s


# In[210]:


s.values


# In[211]:


import numpy as np
b=np.random.randint(0,100,(4,3))
b


# In[212]:


s.keys()


# In[214]:


s=pd.DataFrame(data=b,index=["person1","person2","person3","Person4"],columns=["DSA","Software-Testing",".NET"])
s


# In[216]:


s["Total"]=s["DSA"]+s["Software-Testing"]+s[".NET"]
s


# In[217]:


s["Percentage"]=s["Total"]/300*100
s


# In[218]:


s.loc[["person1","person2"]]


# In[219]:


s.tail(1)


# In[220]:


s.loc["person1"]


# In[221]:


s.loc["person2":]


# In[222]:


s.iloc[2:3]


# In[223]:


s.drop("Percentage",axis=1)


# In[225]:


s.drop("DSA",axis=1,inplace=True)


# In[ ]:





# In[227]:


s


# In[228]:


s.drop("Total",axis=1,inplace=True)


# In[229]:


s


# In[230]:


s.drop("person1",axis=0)


# In[231]:


#create a dataframe which has productid, product name, product price
import pandas as pd
product_id=[101,102,103,104,105]
product_name=["shampoo","bottle","pen","fruit","disc"]
product_price=[200,300,400,500,250]
df=pd.DataFrame(data=[product_id,product_name,product_price],index=["product_id","product_name","product_price"])


# In[232]:


df1=df.transpose()


# In[233]:


df1


# In[234]:


#to access each column
for d in df1:
    print(df1[d])


# In[235]:


#to access individual rows
for i in df1.iterrows():
    print(i)


# In[236]:


df1.iloc[0]


# In[237]:


df1.loc[:3,["product_name"]]


# In[238]:


s


# In[240]:


s.loc[s["Software-Testing"]<40,"Software-Testing"]=41
s


# In[241]:


df1.isnull()
#returns true for the places where null value exists. 


# In[242]:


df1.dropna() #drops the rows where null value exists. we can use the axis=1 attribute to drop  column


# In[243]:


df1.notnull() #returns true when the values are not null(NaN or none)


# In[244]:


df1.dropna(thresh=2) # drops the rows which exceeds the thresh. thresh=2 will keep the rows that has 1 NaN value but will delete for two more


# In[245]:


df1.fillna(value=4) # it will fill value 4 wherever Nan is
'''Methods in fillna are:-
ffil= it will fill the value of the data that was before the NaN value
bfill will give NaN the value that comes after the NaN value'''


# In[247]:


import numpy as np
df=pd.read_csv("Salaries.csv")


# In[248]:


df=df.replace("Not Provided", np.nan)


# In[249]:


df


# In[250]:


df=df.replace("Not provided", np.nan)
df


# In[251]:


df['BasePay']=df['BasePay'].astype('float')


# In[252]:


df.info()


# In[253]:


df['BasePay'].mean()


# In[254]:


df['OvertimePay']=df['OvertimePay'].astype('float')


# In[255]:


df['OvertimePay'].max()

# Merging, Joining and Concatenating
# In[256]:


import pandas as pd
import numpy as np


# In[257]:


A=pd.DataFrame(data=np.random.randint(0,100,(3,3)),index=[1,2,3], columns=[1,2,3])
A


# In[258]:


B=pd.DataFrame(data=np.random.randint(0,100,(3,3)),index=[4,5,6], columns=[1,2,3])
B


# In[259]:


C=pd.DataFrame(data=np.random.randint(0,100,(3,3)),index=[7,8,9], columns=[1,2,3])
C


# In[260]:


display(A, B, C,pd.concat([A,B,C]))


# In[261]:


left= pd.DataFrame({'key':['K0','K2','K5','K3'],
                   'A':['A0','A2','A5','A3'],
                   'B':['B0','B2','B5','B3']})

right= pd.DataFrame({'key':['K0','K1','K2','K9'],
                   'C':['C0','C1','C2','C9'],
                   'D':['D0','D1','D2','D9']})


# In[262]:


display(left, right, pd.merge(left, right, how='inner', on=['key']))


# In[263]:


pd.merge(left, right, how='outer', on=['key'])


# In[264]:


pd.merge(left, right, how='left', on=['key'])


# In[265]:


pd.merge(left, right, how='right', on=['key'])


# In[266]:


#Join
left.set_index('key',inplace=True)


# In[267]:


right.set_index('key',inplace=True)


# In[268]:


left.join(right,how='inner')


# In[269]:


left.join(right,how='outer')


# In[270]:


left.join(right,how='left')


# In[271]:


left.join(right,how='right')


# In[ ]:





# In[ ]:




