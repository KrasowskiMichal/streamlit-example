# import required modules
import streamlit as st
import pandas as pd
from sklearn import datasets

# load Iris dataset from sklearn
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# renaming species for better understanding
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# title of the app
st.title("Demo Wizualizacji w Streamlit")

# selectbox for user to choose species
species = st.selectbox(
    'Wybierz gatunek:',
    df['species'].unique())

# filter dataframe based on user choice
df_filtered = df[df['species'] == species]

# plot
st.write(f"Wykres punktowy dla gatunku: {species}")
st.altair_chart(st.altair.vega_lite.v4.api.Chart(df_filtered).mark_circle().encode(
    x='sepal length (cm)',
    y='sepal width (cm)',
    color='species',
    tooltip=['sepal length (cm)', 'sepal width (cm)']
).interactive())
