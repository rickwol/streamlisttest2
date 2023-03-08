#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install streamlit


# In[6]:


import streamlit as st
import pandas as pd
import numpy as np


# In[ ]:


HairEye = pd.read_csv("HairEyeColor.csv")


# In[ ]:


st.title("Hair Eye Colour Database")


# In[ ]:


InputHair = st.sidebar.selectbox("Select Hair Colour", ("Brown", "Black", "Blond", "Red"))


# In[ ]:


HairEyeSelect = HairEye[HairEye["Hair"] == InputHair]


# In[ ]:


st.dataframe(HairEyeSelect)


# In[1]:


import kaggle


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

