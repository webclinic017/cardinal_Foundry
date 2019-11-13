#!/usr/bin/env python
# coding: utf-8

# ### Dependencies 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as spstats
get_ipython().run_line_magic('matplotlib', 'inline')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# Merged Data

# In[3]:


df = pd.read_csv('df.csv')


# Converting to datetime

# In[16]:


df[['order_estimated_delivery_date','order_purchase_timestamp','review_creation_date','review_answer_timestamp','review_answer_timestamp','shipping_limit_date','order_approved_at','order_delivered_carrier_date','order_delivered_customer_date']] = df[['order_estimated_delivery_date','order_purchase_timestamp','review_creation_date','review_answer_timestamp','review_answer_timestamp','shipping_limit_date','order_approved_at','order_delivered_carrier_date','order_delivered_customer_date']].apply(pd.to_datetime, format='%Y-%m-%d %H:%M:%S')


# Rearraging Columns 

# In[30]:


df = df.reindex(columns=['order_id', 'product_id', 'seller_id','customer_id', 'order_item_id','customer_unique_id', 'shipping_limit_date', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date','review_creation_date','review_answer_timestamp', 'price', 'freight_value', 'customer_zip_code_prefix', 'customer_city', 'customer_state', 'seller_zip_code_prefix', 'seller_city', 'seller_state', 'order_status', 'payment_sequential', 'payment_type', 'payment_installments', 'payment_value', 'review_id', 'review_score', 'review_comment_title', 'review_comment_message', 'product_category_name', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm'])


# Missing Values
# 
# 

# In[31]:


df.isna().sum().sort_values(ascending=False)


# In[ ]:


df.product_photos_qty.fillna(0,inplace=True)


# Descriptive Statistics

# In[9]:


df.describe().round(2).T


# In[10]:


df.corr() 


# Example

# In[27]:


temp1=df.groupby('customer_state')['price'].agg(['sum']).round(2).sort_values(by='customer_state',ascending=False)
temp1


# In[22]:


temp1.plot(kind='bar', figsize = (15,12),fontsize = 15)


# In[13]:


df.groupby('payment_type').price.agg(['describe','sum']).round(2)


# In[14]:


df.groupby('product_category_name').price.value_counts()


# In[15]:


df.order_status.value_counts()


# Sellers

# In[36]:


help(df)


# In[ ]:




