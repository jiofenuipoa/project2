import streamlit as st

st.write("Формуляр")

name = st.text_input("Как се казваш?")

if name:
  st.write("Здравей,", name)

st.number_input("На колко години си?", age)

if age < 18:
  st.write(f"Ти си на {age} години и НЕ си пълнолетен!")

else:
  st.write(f"Ти си на {age} години и си пълнолетен!")
