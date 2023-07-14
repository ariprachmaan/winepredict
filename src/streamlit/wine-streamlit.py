import streamlit as st
from PIL import Image
import requests

header_image = Image.open('assets/wine.jpg')
st.image(header_image)
st.title("Wine Quality Prediction")
st.subheader("Let's Predict Quality of Wine")

#create form
with st.form(key="wine_predict_form"):
    fixed_acidity = st.number_input(
        label="1. Input your Fixed Acidity Value:",
        help="Example value: 7.5"
    )

    volatile_acidity = st.number_input(
        label="2. Input your Volatile Acidity Value:",
        help="Example value: 0.5"
    )

    sulphates = st.number_input(
        label="3. Input your Sulphates Value:",
        help="Example value: 0.6"
    )

    alcohol = st.number_input(
        label="4. Input your Alcohol Value:",
        help="Example value: 12.3"
    )

    density = st.number_input(
        label="5. Input your Density Value:",
        help="Example value: 0.99"
    )
    
    #button submit
    submitted = st.form_submit_button('Predict')

    if submitted:
        # collect data from form
        form_data = {
            "fixed_acidity": fixed_acidity,
            "volatile_acidity": volatile_acidity,
            "sulphates": sulphates,
            "alcohol": alcohol,
            "density": density
        }

        # sending the data to api service
        with st.spinner("Sending data to prediction server... please wait..."):
            res = requests.post("http://api:8000/predict", json=form_data).json()

        # parse the prediction result
        if res['status'] == 200:
            st.success(f"WINE Quality Prediction: {res['prediction']}")
        else:
            st.error(f"ERROR predicting the data. Please check your code: {res}")
