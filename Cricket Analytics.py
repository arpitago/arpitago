#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


ball=pd.read_csv(r'C:\Users\arpit\OneDrive\Documents\Cricket Analytics\Ball_by_Ball.csv')
match = pd.read_csv(r'C:\Users\arpit\OneDrive\Documents\Cricket Analytics\Match.csv')
player = pd.read_csv(r'C:\Users\arpit\OneDrive\Documents\Cricket Analytics\Player.csv')
player_match = pd.read_csv(r'C:\Users\arpit\OneDrive\Documents\Cricket Analytics\Player_Match.csv')
season=pd.read_csv(r'C:\Users\arpit\OneDrive\Documents\Cricket Analytics\Season.csv')
team=pd.read_csv(r'C:\Users\arpit\OneDrive\Documents\Cricket Analytics\Team.csv')


# Important information about the imported data
# 

# In[8]:


print(team['Team_Name'].count(), ' teams have participated till now in IPL from 2008 to 2016')


# In[9]:


print(player['Player_Name'].nunique(), 'players and umpires participated in IPL from 2008 to 2016')


# In[10]:


print('Total',match['Match_Id'].nunique(),' matches have been played in IPL from 2008 to 2016')


# Number of matches played in each season:

# In[34]:


plt.figure(figsize=(10,4))
sns.countplot(x='Season_Id',data=match)
#sns.set_context("talk")
#sns.set_color_codes(palette='deep')
plt.xticks(rotation='horizontal')
plt.ylabel("Number of Matches",fontsize = 20, weight = 'bold')
plt.xlabel("Season Number",fontsize = 20, weight = 'bold')
plt.title("Number of matches played in each season",fontsize=20,weight='bold')

plt.show()


# In[25]:


match['Season_Id'].value_counts()


# Number of matches played in each stadium:

# In[55]:


plt.figure(figsize=(10,12))
sns.countplot(y='Venue_Name',data=match)
#plt.yticks(rotation='horizontal')
plt.xlabel("Number of Matches",fontsize=25,weight='bold')
plt.ylabel("Stadium Name",fontsize=25, weight ='bold')
plt.title("Number of matches played in each stadium:",fontsize=25,weight='bold')
plt.show()
match['Venue_Name'].value_counts()


# Number of Matches played in each city:

# In[58]:


plt.figure(figsize=(10,10))
sns.countplot(y='City_Name',data=match)
plt.xlabel("Number of matches played",fontsize=20,weight='bold')
plt.ylabel("City",fontsize=20,weight='bold')
plt.title("Number of matches played in each city",fontsize=20,weight='bold')
plt.show()
match['City_Name'].value_counts()


# In[ ]:




