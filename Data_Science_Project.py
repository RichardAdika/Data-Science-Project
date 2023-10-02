#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dataset=pd.read_csv('WordnetVerbs.csv')
dataset.head()


# ### How many elements does this dataframe have

# In[2]:


dataset.info()


# In[3]:


dataset.shape


# In[4]:


#DataFrame has 3730 elements


# ### What is the definition of the word abscond
# 

# In[5]:


dataset.loc[dataset['Word']== 'abscond', 'Definition']


# In[6]:


# abscond means to run away


# ### What is the highest possible count of a word

# In[7]:


dataset['Count'].max()


# In[8]:


max_count=dataset['Count'][0]
for counts in dataset['Count']:
    if counts > max_count:
        max_count= counts
print(max_count)
        


# In[9]:


# The highest possible count of a word is 53


# In[10]:


dataset.loc[dataset['Count']== 53, 'Word']


# In[11]:


### Which words have a count of 2
count_3=dataset.loc[dataset['Count']== 2, 'Word']
for words in count_3:
    print(list(count_3))


# In[12]:


### What is the highest length of a word 


# In[13]:


max_length=len(dataset['Word'][0])
for word in dataset['Word']:
    if len(word)> max_length:
        a = word
        max_length= len(word)
        
print(f'{a}: {max_length}')


        


# In[14]:


dataset.describe()


# In[15]:


# highest length of word is 53


# ### what is the most common count?

# In[16]:


dataset['Count'].value_counts(ascending = False)


# In[17]:


dataset['Count'].describe()
dataset['Count'].mode()


# In[ ]:


# 4 is the most common count


# ### How many words have a count of 10

# In[24]:


dataset.loc[dataset['Count']== 10, 'Word'].count()


# In[ ]:


# 144 words have a count of 10


# In[26]:


dataset.loc[dataset['Count']== 10].shape


# In[31]:


dataset.query('Count ==10').sort_values(by='Word').count()


# In[ ]:





# ### Project 2: Querying and Filtering Pokemon Data

# In[1]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


dataset= pd.read_csv('pokemon_data.txt')
dataset.head()


# ### 1. How many Pokemons exist with an Attack value greater than 150

# In[7]:


dataset.loc[dataset['Attack']> 150, 'Name'].count()


# In[11]:


dataset.query('Attack> 150').count()


# In[ ]:


# 18 Pokemons have an attack greater than 150


# ### 2. Select all the pokemons with speed of 10 or less

# In[22]:


less_than_10=dataset.loc[dataset['Speed']<= 10, 'Name']
list(less_than_10) 


# In[23]:


#['Shuckle', 'Trapinch', 'Bonsly', 'Munchlax', 'Ferroseed'] is the list of pokemons with speed less than 11


# ### 3. How many pokemons have a Sp.Def value of 25 or less

# In[28]:


dataset.loc[dataset['Sp. Def']<=25, 'Name'].count()


# ### Select all the legendary Pokemons

# In[36]:


a=dataset.loc[dataset['Legendary'], 'Name']
list(a)


# In[39]:


len(a)


# In[40]:


# 65 ledendary pokemons


# ### Find the outlier

# In[47]:


ax= sns.scatterplot(data = dataset, x = 'Defense', y= 'Attack')
ax.annotate("who's this guy", xy = (228,10), xytext = (150,10), color = 'red', arrowprops= dict(arrowstyle= '->', color = 'red'))


# In[50]:


dataset.loc[(dataset['Attack']< 25) & (dataset['Defense']> 200), 'Name']


# In[ ]:


#Shuckle is the outlier 


# In[74]:


a=dataset.loc[dataset['Defense'], 'Defense'].sort_values(by= 'Defense', ascending = False).head(50)
b = dataset.loc[dataset['Attack']].sort_values(by = 'Attack', ascending= True).head(50)
c= pd.merge(a,b, how= 'inner')
dataset.loc[dataset['Name']== 'Shuckle']


# In[75]:


a


# In[ ]:




