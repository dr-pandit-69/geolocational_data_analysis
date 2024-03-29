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
from streamlit_folium import st_folium,folium_static



st.set_page_config( page_icon="🌍")

st.markdown("<h3 style='text-align: center; color:white;'>Map Data after Clustering</h3>", unsafe_allow_html=True)
st.text("")

st.sidebar.header("Geolocational Data Analysis🌏🗺️")

def api_call(long,lat,query,api_key):
    
    url = "https://api.foursquare.com/v3/places/nearby?ll=17.3972%2C78.4902&query=Hotel&limit=50"

    headers = {
    "Accept": "application/json",
    "Authorization": api_key     
    }

    long_lat=f"ll={long}%2C{lat}"

    return (requests.request("GET",f"https://api.foursquare.com/v3/places/nearby?{long_lat}&query={query}&limit=50" , headers=headers)).json()





api_key = st.text_input('Please Enter the API Key', 'fsq3PJQb14rPXGmdCfpBf67rqC+2Ut76186Cb4z2Vlo3R2A=')
st.write('The current Foursquare API Key is', api_key)

long = st.text_input('Please Enter the Longitude', '28.352416')
lat= st.text_input('Please Enter the Latitude', '76.134185')
st.write('The current Longitude & Latitudes are', long,lat)





results_food1 = api_call(api_key,long,lat,"restaurant")

results_food2=api_call(long,lat,"cafe",api_key)
results_food = {**results_food1,**results_food2}
results_gym=api_call(long,lat,"gym",api_key)
results_lodgings=api_call(long,lat,"hotel",api_key)
results_lodgings.update((api_call(long,lat,"lodge",api_key)))
results_lodgings.update((api_call(long,lat,"hostel",api_key)))

venues_food=pd.json_normalize(results_food['results'])
venues_gym=pd.json_normalize(results_gym['results'])
venues_lodg=pd.json_normalize(results_lodgings['results'])
req_cols=['fsq_id', 'categories', 'chains', 'distance', 'link', 'name',
       'timezone', 'geocodes.main.latitude', 'geocodes.main.longitude',
       'location.country', 'location.cross_street',
       'location.formatted_address', 'location.locality', 'location.postcode',
       'location.region',
       'location.address_extended']


req_cols2=[ 'geocodes.main.latitude', 'geocodes.main.longitude', 'name', 'categories','distance']
Vf=venues_food[req_cols]
Vg=venues_gym[req_cols]
Vl=venues_lodg[req_cols]

f=['geocodes.main.latitude', 'geocodes.main.longitude']
X = Vf[f]
max_k = 10
## iterations
distortions = [] 
for i in range(1, max_k+1):
    if len(X) >= i:
       model = cluster.KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
       model.fit(X)
       distortions.append(model.inertia_)
## best k: the lowest derivative
k = [i*100 for i in np.diff(distortions,2)].index(min([i*100 for i 
     in np.diff(distortions,2)]))
## plot
fig, ax = plt.subplots()
ax.plot(range(1, len(distortions)+1), distortions)
ax.axvline(k, ls='--', color="red", label="k = "+str(k))
ax.set(title='The Elbow Method', xlabel='Number of clusters', 
       ylabel="Distortion")
ax.legend()
ax.grid(True)

f=['geocodes.main.latitude', 'geocodes.main.longitude']
X = Vg[f]
max_k = 10
## iterations
distortions = [] 
for i in range(1, max_k+1):
    if len(X) >= i:
       model = cluster.KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
       model.fit(X)
       distortions.append(model.inertia_)
## best k: the lowest derivative
k = [i*100 for i in np.diff(distortions,2)].index(min([i*100 for i 
     in np.diff(distortions,2)]))
## plot
fig, ax = plt.subplots()
ax.plot(range(1, len(distortions)+1), distortions)
ax.axvline(k, ls='--', color="red", label="k = "+str(k))
ax.set(title='The Elbow Method', xlabel='Number of clusters', 
       ylabel="Distortion")
ax.legend()
ax.grid(True)


f=['geocodes.main.latitude', 'geocodes.main.longitude']
X = Vl[f]
max_k = 10
## iterations
distortions = [] 
for i in range(1, max_k+1):
    if len(X) >= i:
       model = cluster.KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
       model.fit(X)
       distortions.append(model.inertia_)
## best k: the lowest derivative
k = [i*100 for i in np.diff(distortions,2)].index(min([i*100 for i 
     in np.diff(distortions,2)]))
## plot
fig, ax = plt.subplots()
ax.plot(range(1, len(distortions)+1), distortions)
ax.axvline(k, ls='--', color="red", label="k = "+str(k))
ax.set(title='The Elbow Method', xlabel='Number of clusters', 
       ylabel="Distortion")
ax.legend()
ax.grid(True)

Vf2=venues_food[req_cols2]
Vf2=Vf2.rename(columns={'geocodes.main.latitude': 'lat', 'geocodes.main.longitude': 'long'})

Vg2=venues_gym[req_cols2]
Vg2=Vg2.rename(columns={'geocodes.main.latitude': 'lat', 'geocodes.main.longitude': 'long'})

Vl2=venues_lodg[req_cols2]
Vl2=Vl2.rename(columns={'geocodes.main.latitude': 'lat', 'geocodes.main.longitude': 'long'})

map = folium.Map(location=[long,lat], zoom_start=13)
for i, row in Vf2.iterrows():
    folium.CircleMarker(location=[row['lat'], row['long']], popup=row["name"]).add_to(map)


map = folium.Map(location=[long,lat], zoom_start=13)
for i, row in Vg2.iterrows():
    folium.CircleMarker(location=[row['lat'], row['long']], color='red', popup=row["name"]).add_to(map)

map = folium.Map(location=[long, lat], zoom_start=13)
for i, row in Vl2.iterrows():
    folium.CircleMarker(location=[row['lat'], row['long']], color='green', popup=row["name"]).add_to(map)

X = Vf2[["lat","long"]]
max_k = 10
## iterations
distortions = [] 
for i in range(1, max_k+1):
    if len(X) >= i:
       model = cluster.KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
       model.fit(X)
       distortions.append(model.inertia_)
## best k: the lowest derivative
k = [i*100 for i in np.diff(distortions,2)].index(min([i*100 for i in np.diff(distortions,2)]))
## plot
fig, ax = plt.subplots()
ax.plot(range(1, len(distortions)+1), distortions)
ax.axvline(k, ls='--', color="red", label="k = "+str(k))
ax.set(title='The Elbow Method', xlabel='Number of clusters', 
       ylabel="Distortion")
ax.legend()
ax.grid(True)


k = 7
model = cluster.KMeans(n_clusters=k, init='k-means++')
X = Vf2[["lat","long"]]
## clustering
dtf_X = X.copy()
dtf_X["cluster"] = model.fit_predict(X)
## find real centroids
closest, distances = scipy.cluster.vq.vq(model.cluster_centers_, 
                     dtf_X.drop("cluster", axis=1).values)
dtf_X["centroids"] = 0
for i in closest:
    dtf_X["centroids"].iloc[i] = 1
## add clustering info to the original dataset
Vf2[["cluster","centroids"]] = dtf_X[["cluster","centroids"]]

fig, ax = plt.subplots()
sns.scatterplot(x="lat", y="long", data=Vf2, 
                palette=sns.color_palette("bright",k),
                hue='cluster', size="centroids", size_order=[1,0],
                legend="brief", ax=ax).set_title('Clustering (k='+str(k)+')')
th_centroids = model.cluster_centers_
ax.scatter(th_centroids[:,0], th_centroids[:,1], s=50, c='black', 
           marker="x")

model = cluster.AffinityPropagation()


X = Vg2[["lat","long"]]
max_k = 10
## iterations
distortions = [] 
for i in range(1, max_k+1):
    if len(X) >= i:
       model = cluster.KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
       model.fit(X)
       distortions.append(model.inertia_)
## best k: the lowest derivative
k = [i*100 for i in np.diff(distortions,2)].index(min([i*100 for i in np.diff(distortions,2)]))
## plot
fig, ax = plt.subplots()
ax.plot(range(1, len(distortions)+1), distortions)
ax.axvline(k, ls='--', color="red", label="k = "+str(k))
ax.set(title='The Elbow Method', xlabel='Number of clusters', 
       ylabel="Distortion")
ax.legend()
ax.grid(True)

k = 6
model = cluster.KMeans(n_clusters=k, init='k-means++')
X = Vg2[["lat","long"]]
## clustering
dtf_X = X.copy()
dtf_X["cluster"] = model.fit_predict(X)
## find real centroids
closest, distances = scipy.cluster.vq.vq(model.cluster_centers_, 
                     dtf_X.drop("cluster", axis=1).values)
dtf_X["centroids"] = 0
for i in closest:
    dtf_X["centroids"].iloc[i] = 1
## add clustering info to the original dataset
Vg2[["cluster","centroids"]] = dtf_X[["cluster","centroids"]]

model = cluster.AffinityPropagation()

X = Vl2[["lat","long"]]
max_k = 10
## iterations
distortions = [] 
for i in range(1, max_k+1):
    if len(X) >= i:
       model = cluster.KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
       model.fit(X)
       distortions.append(model.inertia_)
## best k: the lowest derivative
k = [i*100 for i in np.diff(distortions,2)].index(min([i*100 for i in np.diff(distortions,2)]))
## plot
fig, ax = plt.subplots()
ax.plot(range(1, len(distortions)+1), distortions)
ax.axvline(k, ls='--', color="red", label="k = "+str(k))
ax.set(title='The Elbow Method', xlabel='Number of clusters', 
       ylabel="Distortion")

k = 5
model = cluster.KMeans(n_clusters=k, init='k-means++')
X = Vl2[["lat","long"]]
## clustering
dtf_X = X.copy()
dtf_X["cluster"] = model.fit_predict(X)
## find real centroids
closest, distances = scipy.cluster.vq.vq(model.cluster_centers_, 
                     dtf_X.drop("cluster", axis=1).values)
dtf_X["centroids"] = 0
for i in closest:
    dtf_X["centroids"].iloc[i] = 1
## add clustering info to the original dataset
Vl2[["cluster","centroids"]] = dtf_X[["cluster","centroids"]]

fig, ax = plt.subplots()
sns.scatterplot(x="lat", y="long", data=Vl2, 
                palette=sns.color_palette("bright",k),
                hue='cluster', size="centroids", size_order=[1,0],
                legend="brief", ax=ax).set_title('Clustering (k='+str(k)+')')
th_centroids = model.cluster_centers_
ax.scatter(th_centroids[:,0], th_centroids[:,1], s=50, c='black', 
           marker="x")

x, y = "lat", "long"
color = "cluster"
popup = "name"
marker = "centroids"
location = [long,lat]
data = Vf2.copy()
## create color column
lst_elements = sorted(list(Vf2[color].unique()))
lst_colors = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in 
              range(len(lst_elements))]
data["color"] = data[color].apply(lambda x: 
                lst_colors[lst_elements.index(x)])

## initialize the map with the starting location
map_ = folium.Map(location=location, tiles="cartodbpositron",
                  zoom_start=13)
## add points
data.apply(lambda row: folium.CircleMarker(
           location=[row[x],row[y]], 
           color=row["color"], fill=True,popup=row[popup]).add_to(map_), axis=1)

## add centroids marker
lst_elements = sorted(list(Vf2[marker].unique()))
data[data[marker]==1].apply(lambda row: 
           folium.Marker(location=[row[x],row[y]], 
           draggable=False,  popup=row[popup] ,       
           icon=folium.DivIcon(html=f"""
            <div><svg>
                <circle cx="25" cy="25" r="20" fill="#69b3a2" opacity=".4"/>
                <rect x="20", y="20" width="10" height="10", fill="white", opacity=".5" 
            </svg></div>""")
    ).add_to(map_), axis=1)
## plot the map

st.text("")

st.markdown("<h3 style='text-align: center; color:white;'>Final Map Outputs</h3>", unsafe_allow_html=True)
st.text("")


st.text("")
st.markdown("<h4 style='text-align: center; color:white;'>Map of Nearby Food Venues", unsafe_allow_html=True)
st.text("")
#st_map=st_folium(map_)
st_map=folium_static(map_,width=700,height=350)

x, y = "lat", "long"
color = "cluster"
popup = "name"
marker = "centroids"
location = [long,lat]
data = Vg2.copy()
## create color column
lst_elements = sorted(list(Vg2[color].unique()))
lst_colors = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in 
              range(len(lst_elements))]
data["color"] = data[color].apply(lambda x: 
                lst_colors[lst_elements.index(x)])

## initialize the map with the starting location
map_ = folium.Map(location=location, tiles="cartodbpositron",
                  zoom_start=13)
## add points
data.apply(lambda row: folium.CircleMarker(
           location=[row[x],row[y]], 
           color=row["color"], fill=True,popup=row[popup]).add_to(map_), axis=1)

## add centroids marker
lst_elements = sorted(list(Vg2[marker].unique()))
data[data[marker]==1].apply(lambda row: 
           folium.Marker(location=[row[x],row[y]], 
           draggable=False,  popup=row[popup] ,       
           icon=folium.DivIcon(html=f"""
            <div><svg>
                <circle cx="25" cy="25" r="20" fill="#69b3a2" opacity=".4"/>
                <rect x="20", y="20" width="10" height="10", fill="white", opacity=".5" 
            </svg></div>""")
    ).add_to(map_), axis=1)
## plot the map

st.text("")
st.markdown("<h4 style='text-align: center; color:white;'>Map of Nearby Gyms", unsafe_allow_html=True)
st.text("")
#st_map=st_folium(map_)
st_map=folium_static(map_,width=700,height=350)

x, y = "lat", "long"
color = "cluster"
popup = "name"
marker = "centroids"
location = [long,lat]
data = Vl2.copy()
## create color column
lst_elements = sorted(list(Vl2[color].unique()))
lst_colors = ['#%06X' % np.random.randint(0, 0xFFFFFF) for i in 
              range(len(lst_elements))]
data["color"] = data[color].apply(lambda x: 
                lst_colors[lst_elements.index(x)])

## initialize the map with the starting location
map_ = folium.Map(location=location, tiles="cartodbpositron",
                  zoom_start=13)
## add points
data.apply(lambda row: folium.CircleMarker(
           location=[row[x],row[y]], 
           color=row["color"], fill=True,popup=row[popup]).add_to(map_), axis=1)

## add centroids marker
lst_elements = sorted(list(Vl2[marker].unique()))
data[data[marker]==1].apply(lambda row: 
           folium.Marker(location=[row[x],row[y]], 
           draggable=False,  popup=row[popup] ,       
           icon=folium.DivIcon(html=f"""
            <div><svg>
                <circle cx="25" cy="25" r="20" fill="#69b3a2" opacity=".4"/>
                <rect x="20", y="20" width="10" height="10", fill="white", opacity=".5" 
            </svg></div>""")
    ).add_to(map_), axis=1)
## plot the map

st.text("")
st.markdown("<h4 style='text-align: center; color:white;'>Map of Nearby Hotels/Lodges", unsafe_allow_html=True)
st.text("")

st_map=folium_static(map_,width=700,height=350)