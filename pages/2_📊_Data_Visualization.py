import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



st.set_page_config( page_icon="📊")

st.markdown("<h3 style='text-align: center; color:white;'>Data Exploration & Visualisation</h3>", unsafe_allow_html=True)
st.text("")

st.sidebar.header("Data Visualisation📊")




df=pd.read_csv('food_coded.csv')

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

sns.set(font_scale=2)

sns.set(rc = {'figure.figsize':(30,15)})
ax=sns.boxplot(data=df)
plt.title('Boxplot represention of the Dataset')
ax.set_ylim(0,7)
ax.set_yticks(range(0,7))


st.text("")
st.markdown("<h4 style='text-align: center; color:white;'>Boxplot representation of the Dataset", unsafe_allow_html=True)
st.text("")
st.pyplot(ax.plot())


sns.set(rc = {'figure.figsize':(10,15)})
ax=sns.countplot(x='marital_status', hue='Gender', data=df, palette=['pink','blue'])
ax.set_ylim(0,40)
ax.set_yticks(range(0,40,2))
plt.xticks([0,1],['Single','In a relationship'])
plt.legend(title='Gender', loc='upper left', labels=['Female', 'Male'])
plt.title('Count of Marital Status of All the Males and Females')


st.markdown("<h4 style='text-align: center; color:white;'>Marital Status Plots", unsafe_allow_html=True)
st.text("")
st.pyplot(ax.plot())

labels = ['Oatmeal', 'Donut']
sizes = [10, 5]
colors = ['orange', 'pink']
patches, texts = plt.pie(sizes, labels=labels, colors = colors, shadow = True,startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.title('Breakfast Preference')


st.markdown("<h4 style='text-align: center; color:white;'>Breakfast Preferences Plot", unsafe_allow_html=True)
st.text("")
st.pyplot(plt.show())

objects = ('Daily', '2-3 times/w', 'Not often', 'On holidays', 'Never')
y_pos = np.arange(len(objects))
performance = [13, 34, 49, 18, 8]
 
plt.bar(y_pos, performance, align='center', alpha=0.7, color='#ffc000')
plt.xticks(y_pos, objects)
plt.ylabel('Frequency')
plt.title('How often do you cook?')
 


st.markdown("<h4 style='text-align: center; color:white;'>Cooking Frequencies Plot", unsafe_allow_html=True)
st.text("")
st.pyplot(plt.show())


sns.set(rc = {'figure.figsize':(10,10)})
objects = ('Daily', '2-3 times/w', 'Not often', 'On holidays', 'Never')
y_pos = np.arange(len(objects))

ax=sns.countplot(x='cook', hue='Gender', data=df, palette=['pink','blue'])
plt.legend(title='Gender', loc='upper left', labels=['Female', 'Male'])

plt.xticks(y_pos, objects)
ax.set_yticks(range(0,30,2))

plt.title('Count of Cooking Frequency of Males and Females')


st.markdown("<h4 style='text-align: center; color:white;'>Cooking Frequencies by Gender Plot", unsafe_allow_html=True)
st.text("")
st.pyplot(ax.plot())

sns.set(rc = {'figure.figsize':(10,10)})
objects = ('< 15k $', '15k-30k $', '30k-50k $', '50k-70k $', '70k-100k $', '> 100k $')
y_pos = np.arange(len(objects))

ax=sns.countplot(x='income', hue='Gender', data=df, palette=['pink','blue'])
sns.set(font_scale=2)
plt.legend(title='Gender', loc='upper left', labels=['Female', 'Male'],fontsize=10)

plt.xticks(y_pos, objects)
#plt.rcParams.update({'font.size': 300})



plt.title('Genderwise Income Comparison')

st.markdown("<h4 style='text-align: center; color:white;'>Genderwise Income Comparison", unsafe_allow_html=True)
st.text("")
st.pyplot(ax.plot())


st.markdown("<h4 style='text-align: center; color:white;'Pairplot of the Dataset", unsafe_allow_html=True)
st.text("")
st.pyplot(sns.pairplot(df))

st.markdown("<h4 style='text-align: center; color:white;'Heatmap of the dataset", unsafe_allow_html=True)
st.text("")
fig, ax = plt.subplots()
plt.title('Heatmap represention of the Dataset')
sns.heatmap(df, ax=ax)
sns.set(rc = {'figure.figsize':(30,15)})
st.write(fig)




