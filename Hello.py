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


st.set_page_config(
    page_title="Geolocational Data Analysis",
    page_icon="📊",
)


st.sidebar.success("Select Page")

st.set_option('deprecation.showPyplotGlobalUse', False)
st.markdown("<h1 style='text-align: center; color:#CBC3E3;'>Geolocational Data Analysis</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color:#CBC3E3;'>Developed by Subrahmanyam B H V S P</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color:white;'>This was done as a part of a Data Science Assignment, where new residents of a city are offered the best residences based on their preferences ", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color:white;'>Foursquare API Key is needed to run the last part of the project ", unsafe_allow_html=True)
st.markdown("<div></div>",unsafe_allow_html=True)
st.text("")
st.text("")
url = ""

