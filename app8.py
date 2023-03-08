#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install streamlit


# In[8]:


import streamlit as st
import pandas as pd
import numpy as np
import os

# In[9]:


HairEye = pd.read_csv("HairEyeColor.csv")


# In[10]:


st.title("Hair Eye Colour Database")


# In[ ]:


InputHair = st.sidebar.selectbox("Select Hair Colour", ("Brown", "Black", "Blond", "Red"))


# In[ ]:


HairEyeSelect = HairEye[HairEye["Hair"] == InputHair]


# In[ ]:


st.dataframe(HairEyeSelect)


# In[15]:


import kaggle

os.environ['KAGGLE_USERNAME'] = "'rickwolbertus"
os.environ['KAGGLE_KEY'] = "e5855257a16718159038159ac864b8f7"



# In[2]:


get_ipython().system('kaggle datasets download -d sunayanagawde/countrywise-covid-cases')


# In[4]:


from zipfile import ZipFile

with ZipFile('countrywise-covid-cases.zip', 'r') as f:
    f.extractall()


# In[7]:


covid = pd.read_csv("Country-wise-COVID-cases.csv")


# In[ ]:


st.dataframe(covid)

