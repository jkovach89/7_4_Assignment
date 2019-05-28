#!/usr/bin/env python
# coding: utf-8

# In[66]:


#! python3
# Module 7.4 Data Visualization Assignment
# by Jacob Kovach

import numpy as np, pandas as pd, matplotlib.pyplot as plt, os
get_ipython().run_line_magic('matplotlib', 'inline')
# Get correct directory
os.chdir('/Users/JKovach/Documents/test projects/duptest13_Thinkful_7_4_Assignment')

# import data set as file object
min_wage = pd.read_csv('./Minimum Wage Data.csv', encoding = "ISO-8859-1")
mw_CA = min_wage.loc[lambda state: min_wage['State']=='California', :]
# mw_CA


# In[69]:


# Create new dataframe for the plot
plot_df = pd.DataFrame()
plot_df['Year'] = mw_CA['Year']
plot_df['Hourly Wage'] = mw_CA['High.Value']
plot_df['Hourly Wage (Adjusted)'] = mw_CA['High.2018']

# Create plot of absolute hourly wage vs. 2018 adjusted hourly wage
plt.plot(plot_df['Hourly Wage'], color='green')
plt.plot(plot_df['Hourly Wage (Adjusted)'], color='red')
plt.show()

# This plot shows the relative value of wages. While wages have increased, adjusted wage has decreased slightly


# In[74]:


plt.scatter(x=plot_df['Year'], y=plot_df['Hourly Wage'])
plt.scatter(x=plot_df['Year'], y=plot_df['Hourly Wage (Adjusted)'])
plt.show()

# Below is the same data expressed as a scatter plot


# In[79]:


plot_df['difference_value'] = plot_df['Hourly Wage (Adjusted)']-plot_df['Hourly Wage']

plt.scatter(x=plot_df['Year'], y=plot_df['Hourly Wage'], color='orange')
plt.scatter(x=plot_df['Year'], y=plot_df['Hourly Wage (Adjusted)'], color='blue')
plt.scatter(x=plot_df['Year'], y=plot_df['difference_value'], color='green')
plt.show()

# Below is the same scatter plot with data points for the difference between real and adjusted wage. 
# As expected, the closer to present day, the smaller the difference.


# In[92]:


mw_1968 = min_wage.loc[lambda year: min_wage['Year']==1968, :]
mw_2017 = min_wage.loc[lambda year: min_wage['Year']==2017, :]

plt.scatter(x=mw_2017['State'], y=mw_2017['High.Value'], color='orange')
plt.show()


# In[93]:


min_wage.loc['California', 'High.Value']


# In[ ]:




