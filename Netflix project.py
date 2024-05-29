#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import datetime as datetime


# In[2]:


netflix_df = pd.read_csv(r'C:\Users\HP\Documents\netflix_titles.csv')
netflix_df.head(2)


# In[3]:


netflix_df.info()


# In[4]:


netflix_df.describe()


# In[5]:


print(netflix_df.isnull().sum())


# In[6]:


netflix_df.shape


# In[7]:


netflix_df = netflix_df.dropna()
print(netflix_df.isnull().sum())


# In[8]:


#print out duplicates

duplicates = netflix_df[netflix_df.duplicated()]
print('Number of duplicates:', duplicates)


# In[9]:


netflix_df.columns


# In[10]:


len(netflix_df)


# In[11]:


#Movies and Tv Shows
sns.countplot(x='type', data=netflix_df)

plt.title('Movies and Tv Shows Counts')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()


# In[12]:


#Rating of Tv Shows and Movies

ax=sns.countplot(x='rating',data=netflix_df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
plt.title('Ratings')
plt.xlabel('Ratings')
plt.ylabel('Count')
plt.show()


# In[13]:


#Relationship Between Type and Rating

ax=sns.countplot(x='rating', hue='type', data=netflix_df)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
plt.title('Relationship Between Type and Rating')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()


# In[14]:


#Casts in shows

get_ipython().system('pip install wordcloud')
from wordcloud import WordCloud

print('WordCloud installed!')


# In[15]:


fig=plt.figure(figsize=(15, 5))
text = ' '.join(netflix_df['cast'].astype(str))
wordcloud = WordCloud(background_color = 'black', width = 1920, height = 1080)
wordcloud.generate(text)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()


# In[16]:


netflix_df.head(2)


# In[17]:


#Top 10 Content Producing countries
top_countries = netflix_df['country'].value_counts().iloc[:10].index
ax = sns.countplot(x='country', data=netflix_df,order=top_countries, palette='dark:red')

ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
plt.title('Top Content Producing Countries', size=21)
plt.xlabel('Country')
plt.ylabel('Title')
plt.show


# In[18]:


topcountries = netflix_df['country'].value_counts().index
topcountries


# In[19]:


get_ipython().system('pip install geopandas')
import geopandas as gpd


# In[20]:


import plotly.graph_objs as go
from plotly.offline import iplot


# In[21]:


topcountries = netflix_df['country'].value_counts()

data=go.Choropleth(
    locationmode='country names',
    locations=topcountries.index,
    z=topcountries.values)

iplot([data])


# In[22]:


netflix_df.head(2)


# In[23]:


#Top genres with largest number of content titles

top_genres = netflix_df['listed_in'].value_counts().iloc[:10].index
ax = sns.countplot(x='listed_in', data=netflix_df, order=top_genres, palette='dark:red')

ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
plt.title('Top Genres with Largest Number of Content Titles')
plt.xlabel('Genres')
plt.ylabel('Count')
plt.show()


# In[24]:


#Rating Movies and Tv Shows
top_genres = netflix_df['listed_in'].value_counts().iloc[:10].index
ax = sns.countplot(x='listed_in',hue='type', data=netflix_df, order=top_genres, palette='dark:red')

ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
plt.title('Rating Movies and Tv Shows')
plt.xlabel('Genres')
plt.ylabel('Count')
plt.show()


# 

# In[25]:


#Comparison of Ratings Between United States and India
fig = plt.figure(figsize=(15, 5))

ax0 = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)

#Subplot 1
US = netflix_df[netflix_df['country']=='United States']['listed_in'].value_counts().iloc[:10].index
ax0 = sns.countplot(x='listed_in',hue='type', data=netflix_df[netflix_df['country']=='United States'], order=US, palette='dark:red', ax=ax0)
ax0.set_xticklabels(ax0.get_xticklabels(), rotation=90, ha='right')
ax0.set_title('Top Genres in US')
ax0.set_xlabel('Genres')
ax0.set_ylabel('Count')


#Subplot 2
India = netflix_df[netflix_df['country']=='India']['listed_in'].value_counts().iloc[:10].index
ax1 = sns.countplot(x='listed_in',hue='type', data=netflix_df[netflix_df['country']=='India'], order=India, palette='dark:red', ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90, ha='right')
ax1.set_title('Top Genres in India')
ax1.set_xlabel('Genres')
ax1.set_ylabel('Count')


plt.show()


# In[26]:


netflix_df.head(2)


# In[27]:


#The Number of Titles in the Last 10 years

fig = plt.figure(figsize=(15, 5))

netflix_year = netflix_df['release_year'].value_counts()
netflix_year = pd.DataFrame(netflix_year).reset_index()
netflix_year.columns = ['release_year', 'title']

sns.barplot(x='release_year',
            y='title',
            color='darkgrey',
            data=netflix_year.head(10),
            )

plt.title('The Number of Titles in the Last 10 Years')
plt.show()


# In[28]:


#Top 5 Longest Titles

fig = plt.figure(figsize=(10, 5))

duration = netflix_df['duration'].value_counts()
duration = pd.DataFrame(duration).reset_index()
duration.columns=['duration', 'title']

sns.barplot(x='duration', y='title', data=duration.head(5), color='red')
plt.title('Top 5 Durations Based on the Number of Titles')
plt.show()


# In[29]:


#The Percentage of Content Types

netflix_content = netflix_df['type'].value_counts()
netflix_content.plot(kind='pie',
                    figsize=(10, 6),
                    autopct='%1.1f%%',
                    startangle=90,
                    shadow=True,
                    colors=['darkgrey','red'])

plt.title('Percentage of Content Types')
plt.axis('equal')

plt.show()


# In[32]:


#Directors with the Highest Number of Titles

directors = netflix_df['director'].value_counts()
directors = pd.DataFrame(directors).reset_index()
directors.columns = ['director', 'title']


fig=plt.figure(figsize=(10, 6))
ax=sns.barplot(x='director', y='title', data=directors.head(8), color='red')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
plt.title('Directors With Most Titles')
plt.xlabel('Directors')
plt.ylabel('No of Titles')

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




