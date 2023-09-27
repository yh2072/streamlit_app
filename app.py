import streamlit as st

x = st.slider('select a number')
st.write(x,"squared is", x * x)
