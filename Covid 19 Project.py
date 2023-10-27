#!/usr/bin/env python
# coding: utf-8

# In[108]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[163]:


dataset_1 = pd.read_csv('18th_june_to_20_august_v2.csv')

dataset_1.head(10)


# In[110]:


# sort_data based on the regions


# In[111]:


regional_record = dataset_1.sort_values(by = 'region')
regional_record.reset_index()


# #  1.What is the total amount of accumulated cases recorded in every region?

# In[112]:


regional_accumulated_cases=regional_record.groupby('region').agg({'accum_cases': 'sum'})


# # 2.Which region had the most cases?

# In[113]:


sorted_regional_accumulated_cases=regional_accumulated_cases.sort_values(by ='accum_cases', ascending = False)
sorted_regional_accumulated_cases


# In[114]:


#  Accra experienced the most accumulated cases


# # 3.Plot the accumulated cases in a barplot

# In[115]:


sorted_regional_accumulated_cases.reset_index(inplace = True)
sorted_regional_accumulated_cases


# In[116]:


cases=list(sorted_regional_accumulated_cases['accum_cases'])
regions = list(sorted_regional_accumulated_cases['region'])
regions


# In[117]:


sns.set(rc= {'figure.figsize': (10,10)})
sns.barplot(x=regions, y = cases, data=sorted_regional_accumulated_cases)
plt.xticks(rotation = 90)
plt.ylabel('Total Number of Accumulated Cases')
plt.xlabel('Regions')
plt.title('Distribution of Accumulated Cases Across Regions in Ghana')
plt.show()


# # 4.Indicate the above distribution using donut plot

# In[146]:


myexplode=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.2,0.5]
plt.pie(cases, labels= regions, radius = 1,explode = myexplode, autopct= '%0.2f%%')
plt.pie([1], colors = ['w'], radius = 0.3)
plt.title('Distribution of accumulated cases across Ghana')


plt.show()


# # 5.Which day had the most new cases across Ghana?

# In[118]:


new_cases=dataset_1.groupby('date').agg({'new_case': 'max'})


# In[119]:


most_new_cases= new_cases.sort_values(by = 'new_case', ascending = False)
most_new_cases= new_cases.sort_values(by = 'new_case', ascending = False).reset_index()


# In[120]:


# 2020-07-16 experienced the most new cases, whereas 2020-06-27 experienced the least cases


# # 6. Illustrate the found result in a diagram

# In[158]:


new_cases=dataset_1.groupby('date').agg({'new_case': 'max'}).reset_index()
sns.lineplot(x= 'date', y = 'new_case', data= new_cases)
plt.xticks(rotation= 90)
plt.title('Progression of new cases by days')
plt.show()


# # 7.Which day experienced the most recovery
# 

# In[133]:


dataset_1.groupby('date').agg({'recovered': 'sum'}).sort_values(by = 'recovered', ascending= False)


# In[122]:


# 2020-08-19  experienced the most recoveries


# # 8.Indicate by diagram the distribution of the active cases as the days went by

# In[148]:


active_cases=dataset_1.groupby('date').agg({'active_cases':'sum'}).reset_index()
active_cases
#active_cases.sort_values(by = 'active_cases', ascending = False)


# In[149]:


sns.lineplot(x='date', y = 'active_cases', data= active_cases)
plt.title('Progression of active cases')
plt.xticks(rotation = 90)
plt.show()


# #                                                  The End
