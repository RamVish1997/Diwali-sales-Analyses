#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# read the data if there is any error utf-8 convert the csv in utf8

df = pd.read_csv(r"C:\Users\ramvi\Downloads\Diwali Sales Data.csv")
df


# In[3]:


# check the size of dataset
df.shape


# In[5]:


df.info(b)


# In[15]:


# amount has null values
df.Amount.isna().sum()

df = df.dropna()


# In[7]:


# since there is no null values in data lets check the noise

for i in df.columns:
    print(i)
    print(df[i].unique(),"\n")


# In[11]:


# in state Andhra\xa0Pradesh just remove the xa0
# rest all are good to go

# lets deal here itself
df.State = df.State.replace("Andhra\xa0Pradesh","Andhra Pradesh")

# lets check 
df.State.unique()

There is no correction in the data; we will move to the analytical part.
# # 

# In[19]:


# lets decribe to understand the numerical feature
# need to remove user_id and marital status . its not making any sense to data here

df.drop(["User_ID","Marital_Status"],axis=1).describe()


# # 

# # Exploratory Data Analysis¶

# # Gender

# In[20]:


# plotting a bar chart for Gender and it's count so we can understand the trend
# order count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[21]:


# plotting a bar chart for gender vs total amount
# Total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# The number of orders placed by female customers is twice as high as that of male customers. This trend is further reflected in the total amount of purchases made by each gender group.

# # 

# # Age

# In[22]:


# plotting a bar chart for Age and it's count so we can understand the trend
# order count

ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[23]:


# plotting a bar chart for Age vs total amount
# Total Amount vs Age Group

sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# The age segment of 26-35 demonstrates the highest total expenditure, highlighting a significant purchasing power within this group.

# # 

# # State

# In[25]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[27]:


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(16,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# While Uttar Pradesh boasts the highest number of orders, it also maintains a substantial presence in terms of total sales amount, reaffirming its significant contribution to overall revenue generation.

# # 

# # Marital Status

# In[29]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(5,3)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[30]:


Marital_sales = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = Marital_sales, x = 'Marital_Status',y= 'Amount', hue='Gender')


# Unmarried women display a higher purchasing inclination compared to other demographic groups, suggesting a distinct consumer behavior pattern influenced by marital status.

# # 

# # Occupation

# In[31]:


# ploting a bar chart to understand the trends of buying behavir by occupation 

sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[32]:


Sales_by_occupation = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = Sales_by_occupation, x = 'Occupation',y= 'Amount')


# The graphs indicate that a significant portion of buyers are employed in the IT, healthcare, and aviation sectors, suggesting a notable consumer presence from these industries.

# # 

# # Category

# In[37]:


# ploting bar chart to find the trend in product categories

sns.set(rc={'figure.figsize':(25,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[38]:


Sales_by_category = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = Sales_by_category, x = 'Product_Category',y= 'Amount')


# In terms of the number of orders, the clothing and food categories demonstrate comparable figures, with food slightly lagging behind clothing. However, when considering the total sales amount, the food category surpasses all other categories, emerging as the top revenue generator with the highest overall sales.
# 

# # 

# # Product

# In[40]:


sales_by_product = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_by_product, x = 'Product_ID',y= 'Orders')


# In[41]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# These products demonstrate a strong demand and significant customer preference, contributing to their prominent position in terms of order numbers.

# # 

# # Conclusion

# Insights reveal that married women aged 26-35 years, employed in the IT, healthcare, and aviation sectors in Uttar Pradesh, Maharashtra, and Karnataka, display a higher propensity for purchasing products from the food, clothing, and electronics categories. This indicates a distinct consumer behavior pattern influenced by demographic factors and occupational preferences.
