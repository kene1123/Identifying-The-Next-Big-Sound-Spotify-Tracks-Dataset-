#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


Tracks = pd.read_csv("C:/Users/ty/OneDrive/Pictures/Documents/Spotify Project/tracks.csv")
Tracks


# In[3]:


#Explore rows and column
Tracks.shape


# In[4]:


#Explore data type and blanks
Tracks.info()


# In[5]:


#Check for duplicates
Tracks['id'].duplicated().sum()


# In[6]:


#Converting duration to minutes
Tracks["duration_min"] = Tracks["duration_ms"] / 60000


# In[7]:


#Converting release_date to a date column
Tracks['release_date'] =Tracks['release_date'].apply(
    lambda x: "1/1/" + x 
    if len(x) == 4
    else x)


# In[8]:


Tracks['release_date1']=Tracks['release_date'].apply(
    lambda x: x + '-01'
    if len(x) == 7
    else x)


# In[9]:


Tracks['release_date1']=pd.to_datetime(Tracks['release_date1'],format='mixed')


# In[10]:


#Rounding up all decimal columns to 2 decimal places
floatcols =Tracks.select_dtypes(include='float')
Tracks[floatcols.columns]=floatcols.round(2)


# In[11]:


#Cleaning the artists column
Tracks['artists'] = Tracks['artists'].str.replace(r"\[", "", regex=True)
Tracks['artists'] = Tracks['artists'].str.replace(r"\]", "", regex=True)
Tracks['artists'] = Tracks['artists'].str.replace(r"\'", "", regex=True)
Tracks['artists'] = Tracks['artists'].str.strip().str.title()


# In[12]:


#Cleaning the song name column
Tracks['name'] = Tracks['name'].str.strip().str.title()


# In[13]:


#loading artists dataset
Artists = pd.read_csv("C:/Users/ty/OneDrive/Pictures/Documents/Spotify Project/Artists.csv")


# In[14]:


#Merging to get column genres
Tracks = Tracks.merge(Artists[["name","genres"]],
                               left_on = "artists",
                               right_on = "name",
                                how = "left")


# In[15]:


#filling blank rows in the genre column
Tracks['genres']=Tracks['genres'].fillna("['unknown']")
Tracks['genres']=Tracks['genres'].str.replace("[]","['unknown']")


# In[16]:


#Dropping unwanted columns
Tracks = Tracks.drop(columns=["id_artists", "release_date", "name_y","duration_ms"])


# In[17]:


#Dropping dupicate rows gotten from the cleaning process
Tracks = Tracks.drop_duplicates()


# In[18]:


#Dropping duplicate rows in the id column
Tracks = Tracks.drop_duplicates(subset=["id"])


# In[19]:


Tracks


# In[20]:


Tracks.to_csv(r"C:\Users\ty\Downloads\Tracks_cleaned.csv",index=False)

