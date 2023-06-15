# import required modules
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# load Iris dataset
df = sns.load_dataset('iris')

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
sns.scatterplot(data=df_filtered, x="sepal_length", y="sepal_width", hue="species", ax=ax)
st.pyplot(fig)
