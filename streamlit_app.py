import streamlit as st
import pandas as pd
import altair as alt

@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
    return pd.read_csv(url)

# load the dataset
df = load_data()

# title of the app
st.title("Demo Wizualizacji w Streamlit")

# selectbox for user to choose a origin of car
origin = st.selectbox(
    'Wybierz pochodzenie samochodu:',
    df['origin'].unique())

# filter dataframe based on user choice
df_filtered = df[df['origin'] == origin]

# display a scatter plot using altair
scatter_plot = alt.Chart(df_filtered).mark_circle().encode(
    x='horsepower',
    y='mpg',
    color='origin',
    tooltip=['name', 'horsepower', 'mpg']
).interactive()

st.altair_chart(scatter_plot, use_container_width=True)
