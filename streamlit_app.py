import streamlit as st

st.write("Формуляр")

name = st.text_input("Как се казваш?")

if name:
  st.write("Здравей,", name)

age = st.number_input("На колко години си?")

if age < 18:
  st.write(f"Ти си на {age} години и НЕ си пълнолетен!")

else:
  st.write(f"Ти си на {age} години и си пълнолетен!")

answer = st.radio(

  "Обичаш ли програмирането?",

  ("да", "не")

)

if answer. == "да":

  st.write("Страхотно, продължавай!")

else:

  st.write("Няма проблем, ще го харесаш ")
