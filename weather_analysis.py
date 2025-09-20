#!/usr/bin/env python
# coding: utf-8

# # WEATHER ANALYSIS - TIME SERIES FORECASTING
# 

# ##### 1) DATA IMPORT

# In[4]:


import pandas as pd                                                                 #importing pandas python library


# In[7]:


weather = pd.read_csv("/Users/ezhilan/Desktop/maindataset.csv" ,index_col="DATE")   # importing and reading our data 
                                                                                    # using pandas read_csv function


# In[ ]:


# Using index_column as date column : as it is unique for every row.


# In[9]:


weather                                                          


# ##### 2) DATA CLEANING

# In[10]:


# first thing we want to do is find and fix missing values in our data set.


# In[11]:


weather.apply(pd.isnull).sum()


# In[12]:


# to find which columns have missing values we use 'apply' method on the weather data frame
# and we will pass pandas in the 'null' function which goes column by column through the weather data frame and -
# - look for any null values .
# .sum() gives us the count of all the null values in each column ~ example: PRECIPITATION column has 4 null values.


# In[13]:


core_weather = weather[["PRECIPITATION","HUMIDITY","SUNSHINE","WIND","TMAX","TMIN"]].copy()


# In[14]:


core_weather


# In[15]:


# we are only taking the columns which are necessary to do our activity 
# so we are copying the necessary columns from 'weather' to create a new table with necessary columns called-
# -'core_weather' 


# CHECKING FOR NULL VALUES IN EACH COLUMN
# 

# In[16]:


core_weather[pd.isnull(core_weather["PRECIPITATION"])]


# In[17]:


core_weather[pd.isnull(core_weather["HUMIDITY"])]


# In[18]:


core_weather[pd.isnull(core_weather["WIND"])]


# ##### 3) DATA MANIPULATION

# FILLING NULL VALUES IN EACH COLUMN

# In[19]:


core_weather["PRECIPITATION"] = core_weather["PRECIPITATION"].fillna(0)


# In[20]:


core_weather[pd.isnull(core_weather["PRECIPITATION"])]


# In[21]:


# now in core_weather - 'PRECIPITATION' column has no null values 
# all the null values are replaced to '0' 


# In[22]:


core_weather = core_weather.fillna(method="ffill")


# In[23]:


core_weather.apply(pd.isnull).sum()


# In[24]:


# now we have no null values in any of the columns 
# as we replaced null values to 0 in PRECIPITATION column 
# and we used 'forward fill' method in other columns , which replaces null values by forward values


# VERIFYING THAT WE HAVE CORRECT DATA TYPES 

# In[25]:


core_weather.dtypes


# In[ ]:


# every columns datatype is in object form 
# we have to convert it into numeric datatype
# astype() command is used to convert datatypes 


# In[ ]:


core_weather["PRECIPITATION"] = core_weather["PRECIPITATION"].astype(float)


# In[36]:


core_weather.dtypes


# In[37]:


core_weather["HUMIDITY"] = core_weather["HUMIDITY"].astype(float)
core_weather["SUNSHINE"] = core_weather["SUNSHINE"].astype(float)
core_weather["WIND"] = core_weather["WIND"].astype(float)
core_weather["TMAX"] = core_weather["TMAX"].astype(float)
core_weather["TMIN"] = core_weather["TMIN"].astype(float)


# In[41]:


core_weather.dtypes


# In[ ]:


# every column is converted into numeric datatype as float64


# In[43]:


core_weather.index


# In[44]:


# index is in object datatypes so it acts as string 
# the index values are actually date&time so we have to convert it into date&time index


# In[45]:


core_weather.index = pd.to_datetime(core_weather.index)


# In[46]:


core_weather.index


# In[47]:


# datatype of index is changed into datetime64


# ##### 4) DATA ANALYSIS & VISUALIZATION 

# In[49]:


import matplotlib.pyplot as plt                                  # importing matplotlib library for visualization


# In[50]:


core_weather[["TMAX","TMIN"]].plot()


# In[51]:


core_weather[["WIND"]].plot()


# In[52]:


core_weather[["SUNSHINE"]].plot()


# In[53]:


core_weather[["HUMIDITY"]].plot()


# In[54]:


core_weather[["PRECIPITATION"]].plot()

