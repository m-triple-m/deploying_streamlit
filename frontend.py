import streamlit as st
import pandas as pd
import plotly.express as px

st.title('First Frontend App')

sidebar = st.sidebar

name = sidebar.text_input("Enter Your name")
btn = sidebar.button('Submit')


if btn:
    st.header(f'You entered {name}')


df = pd.read_csv('Pokemon.csv')

st.dataframe(df)

st.plotly_chart(px.bar(df, x="Name", y="Attack", color='Type 1'))
st.plotly_chart(px.scatter_3d(
    df, x="Attack", y="Defense", z="Sp. Atk", color='Type 1'))
