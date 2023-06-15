# import streamlit module
import streamlit as st

# title of the app
st.title("Prosta Aplikacja Streamlit")

# text input field
user_input = st.text_input("Wpisz coś tutaj")

# display user input
st.write(f"Twoje wprowadzone dane: {user_input}")

# multiple options select box
option = st.selectbox(
    'Wybierz jedną z opcji:',
     ('Opcja 1', 'Opcja 2', 'Opcja 3'))

# display selected option
st.write(f"Twoja wybrana opcja: {option}")
