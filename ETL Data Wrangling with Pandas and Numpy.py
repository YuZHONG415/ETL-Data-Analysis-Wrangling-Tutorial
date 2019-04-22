#!/usr/bin/env python
# coding: utf-8

# ## Pandas is a Python library that primarily adds two new data types in Python：
# - Series: a sequence of items, where each item has a unique label, called an index; 
# - Dataframe: is a table of data, each row has a unique label, called row index, 
#     and each column has a unique label, called column index
# - Each column in the dataframe can be considered as a Series.
# 
# These data types use NumPy library. NumPy primarily adds the ndarry datatype to Pandas.
# ndarry is similar to a Python list, which stores ordered data, but it is different in three aspects:
# - Each element has the same data type
# - Elements are stored contiguously (immediately after each other)
# - The total size of an ndarray is fixed

# In[1]:


get_ipython().system(' python --version')


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### Handling NA
# 
# - Count how many NA,or Nans What percentage of the data row columns ?
# - Decide if data is recoverable or not
# - if yes, get new data to update or augment frame 
# - if no, then you may have to average or fill in or use sampling
# - You may need to impute the data. Refer to Mice package in R. Use R then save R's df then read into Pandas.
# - If the NA's are approx 1 -5 % of Total data then you might be able to remove. If the data id OBVIOUSLY WRONG like negative prices for example when it is not expected remove the rows or change the data items appropriately.
# 
# Warning none == none but np.nan!=np.nan

# In[3]:


a=np.nan
b=np.nan
a==b


# In[4]:


c=None
d=None
c==d


# ##### First Step : ISNULL()  Count How Many NA or Null in the data

# In[5]:


df= pd.read_csv("ozone.csv")


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


# the sum of NA in the dataframe
df.isnull().sum()


# In[9]:


# the percentage of NA in the dataframe
round((df.isnull().sum()/len(df))*100,2)


# In[10]:


# Use loc to assign a new value in the dataframe and examplify None is treated as NA
df.loc[4,'Temp']= None
print(df.loc[3:5,:])
df.isnull().sum()


# In[14]:


# Use a mask to see the missing values or vice versa
Mask = df.loc[:,:].isnull()
# To see the entries with NA in Ozone column
df[Mask.loc[:,'Ozone']]
#df.loc[Mask.loc[:,'Ozone']]


# In[80]:


# To see the entires Solar.R is not null
df.loc[Mask['Solar.R']!= True]
# To see all the missing values
df[(Mask['Ozone']==True) | (Mask['Solar.R']==True) | (Mask['Temp']==True)]
# To see all the non-null values
df[(Mask['Ozone']!=True) & (Mask['Solar.R']!=True) & (Mask['Temp']!=True)]
# also check notnull() function


# In[81]:


# stats check of dataframe
df.describe()


# In[85]:


# customized stats check
df.describe(percentiles=[0.125,0.25,0.5,0.75])


# ### Filetring Out Missing Values dropna()

# In[86]:


cleaned = df.dropna(axis=0,inplace=False) # axis=1 will drop the entire column with NA
cleaned.info()


# In[93]:


# drop columns
df.dropna(axis=1,inplace=False).head()
df.drop(labels=['Ozone','Solar.R','Temp'],axis=1,inplace=False).head()


# In[95]:


# drop rows
df.drop(labels=np.arange(0,5),axis=0,inplace=False).head()


# ##### df.dropna(how='all'/'any',axis=0/1,inplace=True/False)

# ### Filling in Missing Values

# In[99]:


df2=pd.DataFrame(np.random.randn(6,3))
df2.iloc[4:,2]=None
df2.iloc[2:,1]=None
df2


# In[100]:


# Use fillna() funcion to fill NA with a specific value
df2.fillna(0)


# In[101]:


# fill NA with prespecified values by column index
df2.fillna({1:7,2:77})


# In[106]:


df2[4]=[0.0343,0.244,-0.936,None,0.7128,1.415]
# fill na with the mean of non na's in the column
df2.fillna(value=df2.mean())


# ## Data Transformation
# Instead of looping though a dataframe, Pandas favors using vectorized functions that operate column by column.

# ### Remove Duplicates

# In[15]:


df3=pd.DataFrame({'Mark':[19,93,0,9,0,4],'Jackson':[19,94,0,3,0,28],'JB':[19,94,0,1,0]+[6]})
df3


# In[16]:


# dataframe.duplicated returns boolean
df3.duplicated()


# In[121]:


# dataframe.unique() to check the unique values in a column/ array
df3.JB.unique()


# In[122]:


# get the number of unique values in a column
df3.Jackson.nunique()


# #### drop_duplicates() function

# In[123]:


df3.drop_duplicates(inplace=False)
# by default the drop_duplicates() function will drop the duplicated rows


# In[125]:


df3['savage']=[1,2,1,2,1,2]
df3.drop_duplicates(['savage'])
# assign specific column index to drop the row with duplicated values in this column


# ### Transpose Dataframe

# In[126]:


df3.T


# In[129]:


df3.T.drop_duplicates([1])


# ### Transformaing Data Using a Function or Mapping

# In[133]:


df4=pd.DataFrame({'GOT7':['JB','Mark','Jackson','Jinyoung','Youngjae','Bambam','Yugyeom'], 'birthmonth': [1,9,3,9,9,5,11]})
df4


# In[152]:


# using a dict as a map to transform
# create a dictionary
nickname={'JB':'Def','Mark':'XCIII','Jackson':'Sennie','Jinyoung':'JYP','Youngjae':'ARS','Yugyeom':'YG','Bambam':'Doubel B'}
nickname


# In[147]:


track={'JB':'Sunrise','Mark':'OMW','Jackson':'Made It','Jinyoung':'My Youth','Youngjae':'Nobody Knows','Bambam':'Party','Yugyeom':'Fine'
      }
track


# In[153]:


# use the map() 
df4['nickname']=df4['GOT7'].map(nickname) # notice dataframe object has no attribute 'map' 
df4


# In[154]:


df4['Track']=df4['GOT7'].map(lambda x: track[x])
df4


# #### Use apply() to transform dataframe

# In[155]:


df.apply(lambda x: x.max())


# In[158]:


df.apply(lambda x:x.mean())
# or df.apply(lambda x:np.mean(x))


# In[162]:


# apply function to specifc columns
df.iloc[:,1:3].apply(lambda x: x.mean())


# In[169]:


df['max-min']=df.loc[:,['Ozone','Temp']].apply(lambda x: abs(max(x)-min(x)), axis=1)
df.head(10)


# In[170]:


df4.info()


# In[199]:


# create a new function
def seven_or_nothing(content):
    if type(content==int):
        return content + 7
    else: raise(TypeError)


# In[201]:


df4.loc[:,'birthmonth'].apply(seven_or_nothing)


# In[206]:


def seven_forever(dataframe):
    if type(dataframe==object):
        return dataframe + "GOT7"        


# In[207]:


df4.loc[:,'Track'].apply(seven_forever)


# In[212]:


type(df[['Ozone']]) # both column index and row index


# In[214]:


type(df['Ozone']) # only row index


# ## Replacing Values

# In[219]:


# use where function to change/replace values
df[['Ozone']].where((df['Ozone']>20) & (df['Wind']<10), np.nan, axis=0).head(10)


# In[220]:


df[['Ozone']].where((df['Ozone']>20) & (df['Wind']<10), 777 , axis=0).head(10)


# In[223]:


#replace()
df4.replace(['JB','YG'],['Jaebeom','Gyeomy'])


# In[225]:


df4.replace({'JB':'Strawberry Milk','YG':'Ice Choco'})


# ## Rename or Add Columns

# In[226]:


df4.rename(columns={'birthmonth':'Month','Track':'Song'},inplace=False)


# In[227]:


df4.columns=['GOT7','Month','Nickname','Song']
df4


# ## Merge/Join and Concatenate

# In[228]:


df5 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df6 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': [0,1,2]})
df7 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data3': [10,11,12]})
df8 = pd.DataFrame({'key': ['a', 'b', 'd','e','f'],
                    'data4': [0,1,2,3,4]})


# In[229]:


# Merge same shape and keys
# Pandas will merge on the intersection of common named columns or index
pd.merge(df6,df7)


# In[230]:


pd.merge(df6,df7,on='key')


# In[250]:


df6.join(df7.data3,how='inner')


# In[231]:


pd.merge(df5,df6, on='key')


# In[257]:


df5.join(df6,how='outer',lsuffix='_a', rsuffix='_b')


# In[232]:


pd.merge(df5,df6,on='key',how='left')


# In[233]:


pd.merge(df5,df6,on='key',how='right')


# In[234]:


pd.merge(df5,df6,on='key',how='outer')


# ### Concatination of data frames

# In[20]:


DF=pd.DataFrame({'GOT7':['JB','Mark','Jackson','Jinyoung'],'Month':[1,9,3,9]})
DF2=pd.DataFrame({'GOT7':['Youngjae','Bambam','Yugyeom'],'Month':[9,5,11]})


# In[21]:


GOT7=pd.concat([DF,DF2],axis=0,ignore_index=True)
GOT7


# In[22]:


DF3=pd.DataFrame({'Track':['Sunrise','OMW','Made It','My Youth','Nobody Knows','Party','Fine']})


# In[23]:


GOT7=pd.concat([GOT7,DF3],axis=1,ignore_index=False)
GOT7

