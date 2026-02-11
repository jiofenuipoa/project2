import streamlit as st

st.write("Как се казваш?")

name = st.text_input("Въведи името си")

if name:

  st.write("Здравей,", name)
