# import required modules
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import seaborn as sns

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
fig, ax = plt.subplots()
sns.scatterplot(data=df_filtered, x="sepal length (cm)", y="sepal width (cm)", hue="species", ax=ax)
st.pyplot(fig)
