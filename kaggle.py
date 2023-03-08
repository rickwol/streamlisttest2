import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import streamlit as st

import os

os.environ['KAGGLE_USERNAME'] = "'rickwolbertus"
os.environ['KAGGLE_KEY'] = "e5855257a16718159038159ac864b8f7"

dataset_download_files("adiamaan/modi-speeches", path="./data", unzip=True)
df = pd.read_csv("./data/modi_speeches.csv")
st.dataframe(df)
