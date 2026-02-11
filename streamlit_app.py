import streamlit as st

st.write("Формуляр")

name = st.text_input("Как се казваш?")

if name:
  st.write("Здравей,", name)

age = st.number_input("На колко години си?", step=1, min_value=1, max_value=100)

if age < 18:
  st.write(f"Ти си на {age} години и НЕ си пълнолетен!")

else:
  st.write(f"Ти си на {age} години и си пълнолетен!")

answer = st.radio(

  "Обичаш ли програмирането?",

  ("да", "не")

)

if answer == "да":

  st.write("Страхотно, продължавай!")

else:

  st.write("Няма проблем, ще го харесаш ")

if st.button("Кликни ме!"):

  st.write("Благодаря!")

num = st.number_input("Колко е 5х5?")
if num == 25:
  st.write("Правилно!")
else:
  st.write("Грешно!")
