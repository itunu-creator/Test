import streamlit as st
from PIL import Image

img = Image.open("Subject 1 (2).jpg")
st.image(img.resize((300,200)))

st.header("My Crazy App")
st.subheader("introducing")
st.number_input("Input any number", step=1)
st.text_input("Fill in your name")

st.date_input("Select your year of birth")

st.checkbox("Do you agree")
st.selectbox("Gender",['Male','Female','Others'])
st.select_slider("input",[2,4,6,8,10])
st.radio("Gender",['Male','Female','Others'])

st.sidebar.radio("Genders",['Male','Female','Others'])