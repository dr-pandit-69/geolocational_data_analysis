import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing, cluster
import scipy
import folium
import geopy
import requests
from streamlit_folium import st_folium
st.set_page_config( page_icon="📈")

st.markdown("<h3 style='text-align: center; color:white;'>Data Analysis & Cleaning</h3>", unsafe_allow_html=True)
st.text("")



st.markdown("<h4 style='text-align: center; color:white;'>Dataframe after reading data from CSV", unsafe_allow_html=True)
st.text("")
st.sidebar.header("Data Analysis📈")



df=pd.read_csv('food_coded.csv')
st.write(df)
missing_val_cols=[]
for col in df.columns:
    if df[col].isnull().any():
        missing_val_cols.append(col)


df['calories_day'].fillna(1,inplace=True)                # 19 missing values
df['comfort_food_reasons_coded'].fillna(9,inplace=True)  # 19 missing values
df['cuisine'].fillna(6,inplace=True)                     # 17 missing values
df['employment'].fillna(4,inplace=True)                  # 09 missing values 
df['exercise'].fillna(5,inplace=True)                    # 13 missing values
df['type_sports'].fillna('Nothing',inplace=True)         # 21 missing values
st.markdown("<h4 style='text-align: center; color:white;'>Dataframe after filling missing values", unsafe_allow_html=True)
st.text("")
st.write(df)
for i in missing_val_cols:
    df = df[~df[i].isnull()]

req_cols = ['Gender', 'breakfast', 'cook', 'cuisine',
            'eating_out', 'employment', 'exercise',
            'fav_food', 'grade_level', 'income',
            'marital_status', 'on_off_campus', 'pay_meal_out', ]

df2 = df[req_cols]

df=df2





req_cols = ['Gender', 'breakfast', 'cook', 'cuisine',
            'eating_out', 'employment', 'exercise',
            'fav_food', 'grade_level', 'income',
            'marital_status', 'on_off_campus', 'pay_meal_out' ]



df2 = df[req_cols]

df=df2
st.markdown("<h4 style='text-align: center; color:white;'>Final Dataframe after removing unnecessary columns & processing", unsafe_allow_html=True)
st.text("")
st.write(df)
st.text("")
