#!/usr/bin/env python
# coding: utf-8

# load Necessary Libraries

# In[12]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ###Basic Graph

# In[75]:


x= np.array([0,1,2,3,4])
y= np.array([0,2,4,6,8])
# Resize your Graph(dpi specifies pixels per inch. When saving probably should use if possible 300 dpi)
plt.figure(figsize = (5,3), dpi = 100)



plt.plot(x,y, label = '2x', color = 'b', linewidth=2, marker= '<', markersize = 10, markeredgecolor = 'red', linestyle = '--')

#line number two
x2 = np.arange(0,4.5,0.5)
#plot part of the graph as line
plt.plot(x2[:6], x2[:6]**2, 'r', label = 'x^2', linestyle = '--')
#plot remainder of graph
plt.plot(x2[4:], x2[4:]**2, 'r', marker= 'o')
#Add a title (specify font parameters with fontdict)
plt.title('My first graph', fontdict = {'fontname': 'Algerian', 'fontsize': 15})
plt.ylabel('Y-axis', fontdict = {'fontname': 'Algerian', 'fontsize': 12})
plt.xlabel ('X-axis',fontdict = {'fontname': 'Algerian', 'fontsize': 12})
#X,Y axis Tickmark(scale of your graph)
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8])
plt.legend()

#save figure(dpi 300 is good when saving so graph has high resolution)
plt.savefig('mygraph.png', dpi = 300)
#show plot
plt.show()


# #BAR CHART
# 

# In[11]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
labels = ['A','B', 'C']
values = [1,4,2]

bars=plt.bar(labels, values)
patterns = ['/', 'ox', '+']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
plt.yticks=([1,2,3,4])


#bars[0].set_hatch('*')
#bars[1].set_hatch('/')
#bars[2].set_hatch('xo')
plt.figure(figsize = (6,4))
plt.show()


# Real World Examples
# 

# In[102]:


dataset = pd.read_csv('gas_prices.txt')
#countries = dataset.drop(columns = 'Year')
#year = dataset['Year']
plt.figure(figsize=(8,5), dpi = 300)
plt.title('Gas prives over Time (in USD)',fontdict={'fontweight': 'bold','fontname': 'Algerian', 'fontsize': 22},)

#plt.plot(dataset.Year,dataset.USA,'b--', marker = 'o', label = 'USA')
#plt.plot(dataset.Year, dataset.Canada, marker = 'o', label = 'Canada')
#plt.plot(dataset.Year, dataset['South Korea'], marker = 'o', label = 'South Korea')
#plt.plot(dataset.Year, dataset.Australia, 'y--')
countries_to_look_at= ['Australia', 'USA', 'Canada']
for country in dataset:
    if country in countries_to_look_at:
        plt.plot(dataset.Year, dataset[country])
plt.xlabel('Year')
plt.ylabel('US Dollars')
#for data in dataset:
#    if data != 'Year':
#        plt.plot(dataset.Year,dataset[data])
#plt.legend()
plt.show()

plt.savefig('Gas_price_figure.png', dpi = 300)


# ### LOAD FIFA DATA

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('fifa_data.txt')


# ### Histogram

# In[20]:


bins = [40,50,60,70,80,90,100]
plt.hist(dataset.Overall, bins,color = '#abcdef')
plt.xticks(bins)
plt.ylabel('Number of players')
plt.xlabel('Player Ratings')
plt.title('Distribution of player Skills in Fifa 2018', fontdict= {'fontweight': 'bold','fontname':'Algerian'})
plt.show()


# ### Pie Charts

# In[43]:


dataset['Preferred Foot']
Right = dataset.loc[dataset['Preferred Foot']== 'Right'].count()[0]
Left = dataset.loc[dataset['Preferred Foot']== 'Left'].count()[0]
labels = ['Right', 'left']
color = ['cyan', '#abcdef']
plt.pie([Right,Left],labels= labels, colors =color, autopct = '%.2f%%')
plt.title('Prefeered Foot of Fifa players', fontdict= {'fontname':'Algerian', 'fontweight': 'bold'})
plt.show()


# In[80]:


#converting weight to float by removing lbs
dataset.Weight= [int(x.strip('lbs')) if type(x) ==str else x for x in dataset.Weight]
light = dataset.loc[dataset.Weight < 125].count()[0]
light_medium = dataset.loc[(dataset.Weight> 125) & (dataset.Weight < 150)].count()[0]
medium = dataset.loc[(dataset.Weight>= 150) & (dataset.Weight < 175)].count()[0]
medium_heavy= dataset.loc[(dataset.Weight>= 175) & (dataset.Weight < 200)].count()[0]
heavy = dataset.loc[(dataset.Weight>= 200)].count()[0]
weight = [light, light_medium, medium, medium_heavy, heavy]
explode = [.4,0.2,0,0,.4]
plt.style.use('ggplot')
label = ['light', 'light_medium', 'medium', 'medium_heavy', 'heavy']
plt.pie(weight, labels = label, autopct = '%.2f%%', pctdistance = 0.8, explode= explode)
plt.title('Weight Distribution of Fifa 2018 players(In Pounds)')
plt.show()


# ### Box and Whiskers Chart

# In[19]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dataset = pd.read_csv('fifa_data.txt')
plt.figure(figsize= (4,7))
plt.style.use('default')
barcelona = dataset.loc[dataset.Club == 'FC Barcelona']['Overall']
madrid = dataset.loc[dataset.Club =='Real Madrid']['Overall']
united = dataset.loc[dataset.Club== 'Manchester United']['Overall']
labels = ['FC Barcelona', 'Real Madrid','Manchester United']
boxes =plt.boxplot([barcelona, madrid, united], labels = labels,medianprops ={'linewidth':2}, patch_artist = True)#change fill colour)
#set edge color
for box in boxes['boxes']:
    box.set(color= 'cyan', linewidth = 2)
    
    
plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA Overall ratings')
plt.show()

