import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import requests
import joblib

st.markdown(
    f"""
       <style>
       .stApp {{
           background-image: url("https://gsnfx.co.uk/wp-content/uploads/2022/06/contact-background-scaled-1400x500-c-default.jpg");
           background-attachment: fixed;
           background-size: cover;
           /* opacity: 0.3; */
       }}
       </style>
       """,
    unsafe_allow_html=True
)
col1, col2 = st.columns(2)

base_url = 'https://api.exchangerate-api.com/v4/latest/'
with col1:
    st.markdown("<h3 style='text-align: center; color: black;'>เว็บไซต์แปลงสกุลเงิน </h3>", unsafe_allow_html=True)
    amount = st.number_input("กรุณาระบุจำนวนเงิน")
    currency_from = st.selectbox("กรุณาเลือกสกุลเงิน", ["USD", "GBP", "EUR", "JPY", "HKD", "SGD",])
    currency_to = st.selectbox("กรุณาเลือกสกุลเงินที่ต้องการแปลง", ["USD", "GBP", "EUR", "JPY", "HKD", "SGD"])
    if st.button("แปลง"):
        response = requests.get(base_url + currency_from)
        data = response.json()
        rate = data["rates"][currency_to]
        result = round(amount * rate, 2)
        st.write(f"{amount} {currency_from} ได้ {result} {currency_to}")


with col2:
    def load_exchange1_data():
        return pd.read_excel('exchange1.xlsx')


    def save_model(model):
        joblib.dump(model, 'model.joblib')

    def load_model():
        return joblib.load('model.joblib')


    def generate_exchange1_data():
        pass

    generateb = st.button('generate exchange1.xlsx')
    if generateb:
        st.write('generating "exchange1.xlsx" ...')
        generate_exchange1_data()
        st.write(' ... done')




    loadb = st.button('load exchange1.xlsx')
    if loadb:
        st.write('loading "exchange1.xlsx ..."')
        df = pd.read_excel('exchange1.xlsx', index_col=0)
        st.write('... done')
        st.dataframe(df)
        fig, ax = plt.subplots()

    trainb = st.button('อัตราแลกเปลี่ยน')
    if trainb:
        st.write('training model ...')
        df = pd.read_excel('exchange1.xlsx', index_col=0)
        model = LinearRegression()
        st.write('... done')
        st.dataframe(df)
        save_model(model)



