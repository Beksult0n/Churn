import pickle
import streamlit as st
st.title("Mijozlarni Qarori")

cityTier=st.number_input("Shahar darajasi",min_value=1, max_value=3,step=1)
gender = st.selectbox("Jinsini tanlang erkak bo'lsa: ", ["Erkak","Ayol"])
marry = st.selectbox("Turmush qurganmi yoki yolg'iz?", ["Xa","Yo'q"] )
number_add=st.number_input("Manzil raqami",min_value=1, max_value=10,step=1)
oxirgi = st.number_input("Oxirgi yildan buyurtma miqdori:", min_value=0, max_value=50, step=1)
buyurtma_miqdori = st.number_input("Oxirgi kundagi buyurtmalari:", min_value=0, max_value=10, step=1)
cash_hisobi = st.number_input("Keshbek miqdori:", min_value=0, max_value=200, step=1)

if gender =="Erkak":
    gender=1
elif gender=="Ayol":
    gender=0

if marry =="Xa":
    marry=1
elif marry=="Yo'q":
    gender=0

with open('Churn.pkl', 'rb') as file:
    churn = pickle.load(file)
if st.button("Natijani ko'rish uchun bosing!"):
    churn_result=churn.predict([[cityTier  , gender  ,marry ,number_add, oxirgi, buyurtma_miqdori,  cash_hisobi]])
    if(churn_result==0):
        st.write("Sizning mijozingiz qoladi")
    else:
        st.write("Sizning mijozingiz ketadi")
