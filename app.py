import numpy as np
import pickle
import streamlit as st

st.markdown("<h2 style='text-align: center; color: green;'>Agricultural land Web app</h2>", unsafe_allow_html=True)

# loading the saved model
model = pickle.load(open('model.sav', 'rb'))

# function to convert input data to numeric values
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return np.nan

# getting the input data from the user and converting to numeric values
N = convert_to_float(st.text_input('Nitrogen content in soil'))
P = convert_to_float(st.text_input('Phosphorous content in soil'))
K = convert_to_float(st.text_input('Potassium content in soil'))
temperature = convert_to_float(st.text_input('Temperature in celsius'))
humidity = convert_to_float(st.text_input('Humidity in %'))
ph = convert_to_float(st.text_input('Ph value of the soil'))
rainfall = convert_to_float(st.text_input('Rainfall in mm'))

# code for Prediction
diagnosis = ''

# creating a button for Prediction
if st.button('Result'):
    # Check if any of the input values are NaN (non-numeric)
    if np.isnan([N, P, K, temperature, humidity, ph, rainfall]).any():
        st.error("Please provide numeric values for all input fields.")
    else:
        # Convert input values to array and reshape for prediction
        input_data = np.array([N, P, K, temperature, humidity, ph, rainfall]).reshape(1, -1)
        prediction = model.predict(input_data)

        # Mapping the prediction to the crop names
        crop_names = [
            "Rice", "Maize", "Jute", "Cotton", "Coconut", "Papaya", "Orange", "Apple",
            "Muskmelon", "Watermelon", "Grapes", "Mango", "Banana", "Pomegranate", 
            "Lentil", "Blackgram", "Mungbean", "Mothbeans", "Pigeonpeas", "Kidneybeans", 
            "Chickpea", "Coffee"
        ]
        diagnosis = crop_names[prediction[0]]
        
        st.success(f"It is {diagnosis}")

st.markdown("<h4 style='text-align: center; color: red;'> Founded by Rim Abria </h4>", unsafe_allow_html=True)
