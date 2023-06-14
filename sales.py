# -*- coding: utf-8 -*-
"""
**********Product Sales Data Analysis**********
**********@author: gulsen************
"""
""" *********************************************************************** """
""" 
Libraries
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime

""" *********************************************************************** """
"""
Data import
"""

data=pd.read_csv(r'C:\Users\LENOVO\Desktop\data_science\Sales_Data\sales.csv')

data.shape



""" *********************************************************************** """


"""
Data Preparation
"""


data['Date'].unique()

data.info()

data['DATE']=pd.to_datetime(data['Date'])

data.insert(17, "YEAR",'')

data['YEAR']=pd.to_datetime(data['DATE']).dt.strftime('%Y')

""" *********************************************************************** """

"""
VISUALIZE
"""
f, ax = plt.subplots(figsize=(5,5))
sns.boxplot(x='YEAR', y='Profit', data=data).set(title="Find outlier value")


f, ax = plt.subplots(figsize=(10,10))
sns.stripplot(x='YEAR', y='Profit', data=data, jitter=True)

f, ax = plt.subplots(figsize=(5,5))
sns.barplot(x='YEAR', y='Sales', data=data)

f, ax = plt.subplots(figsize=(10,8))
sns.countplot(x="State", data=data)
plt.xticks(rotation='vertical')
plt.title('WHICH STATE WE GET MORE PROFIT', fontsize=20)
plt.ylabel('Profit', fontsize=20)
plt.xlabel('State', fontsize=20)


sns.displot(data["Product Type"]).set(title='VISUALIZE WHICH PRODUCT TYPE SALES MORE')





