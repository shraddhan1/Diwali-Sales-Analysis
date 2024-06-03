#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install seaborn')
get_ipython().system('pip install numpy')
get_ipython().system('pip install matplotlib')


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns



# In[3]:


get_ipython().system('pip3 install --upgrade pandas')


# In[4]:


df = pd.read_csv(r'D:\config_pc\Diwali Sales Data.csv', encoding='unicode_escape')


# In[5]:


df.shape  #shows rows and columns


# In[6]:


df.head()  #shows top 5 most rows


# In[7]:


df.head(10)  #shows top 10 rows 


# In[8]:


df.info()  #gives all information as Status and unnamed1 is 0


# In[9]:


df.drop(['Status','unnamed1'], axis=1, inplace=True) 
#delete columns name status and unamed 
#axis=1 shows that the vertical rows(akhi ubhi columns)
#inplace=True means ctrl+s=inplace in jupyter


# In[10]:


df.info() #we remove that 2 columns


# In[11]:


pd.isnull(df) #false hai means null nahi hai


# In[12]:


pd.isnull(df).sum() #Amount column has 12 null values


# In[13]:


df.shape #to check rows before delete null values


# In[14]:


df.dropna(inplace=True)

#delete null values


# In[15]:


df.shape #check rows after delete null values


# In[16]:


pd.isnull(df).sum()  #we see now Amount column has no null values


# In[17]:


# to change data type as Amount has float data type to int

df['Amount'] = df['Amount'].astype('int')

#[column nam]    [column nam].astype('change data type') 


# In[18]:


df['Amount'].dtypes  #check the datatype


# In[19]:


df.columns  #show the all columns name


# In[20]:


df.rename(columns={'Marital_Status': 'shaadi'})  
#rename the column name or change column name
# if we want to save this column name then we write inplace=True


# In[21]:


df.describe() # return the data in dataframe(count,mean,std,min,max,etc.)


# In[22]:


#use describe() for specific columns
df[['Age','Orders']].describe()


# # Data Analysis

# # Gender

# In[24]:


df.columns


# In[25]:


# count the gender using countplot(seaborn)
sns.countplot(x='Gender',data=df)  


# In[26]:


ax=sns.countplot(x='Gender',data = df)
for i in ax.containers:
    ax.bar_label(i)
    


# In[27]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[28]:


sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x="Gender", y='Amount',data = sales_gen)


# From above graph most of buyers are females and purchasing power of female is grather than male.

# # Age

# In[29]:


df.columns


# In[30]:


sns.countplot(data = df, x = 'Age Group')


# In[31]:


sns.countplot(data = df, x = 'Age Group', hue = 'Gender' , palette = "Set2")

# hue used to visualize the data of different categories in one plot.
# palette is the RGB color strings


# In[32]:


sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x="Age Group", y='Amount',data = sales_age)


# Most of buyers are age group between 26-35 years feemale

# # State

# In[33]:


df.columns


# In[35]:


#total no. of orders from top 10 states

sales_state = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State',y='Orders')


# In[36]:


# total amount/sales from top 10 states
   
sales_state = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state, x='State',y='Amount')


# From above graphs we can see most of orders & total sales/amount are from Uttarpradesh, Maharashtra, Karantaka respectively

# # Martial_Status

# In[37]:


ax=sns.countplot(data=df , x='Marital_Status')

sns.set(rc={'figure.figsize':(10,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[38]:


sales_state=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x='Marital_Status', y='Gender')


# In[39]:


sales_state=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x='Marital_Status', y='Amount' , hue = 'Gender')


# Most of above buyers are married(women) and they have high purchasing power

# # Occupation

# In[40]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[41]:


sales_state=df.groupby(['Occupation'],as_index = False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation', y = 'Amount')


# most of buyers are working on IT,Health sector and Aviation

# In[42]:


df.columns


# # Product Category

# In[43]:


sns.set(rc={'figure.figsize':(25,6)})
ax = sns.countplot(data = df, x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[44]:


sales_state=df.groupby(['Product_Category'],as_index = False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(33,10)})
sns.barplot(data = sales_state, x = 'Product_Category', y = 'Amount')


# Most sold products are Food, Clothing and Electronics category

# In[45]:


sales_state = df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state, x = 'Product_ID', y = 'Orders')


# In[46]:


# top 10 most sold products (something as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion

#  Married women age group 26-35 years from UP, Maharastra and Karnataka working in IT, Healthcare & Aviation likes buy products from Food, Clothing and Electronics category.
