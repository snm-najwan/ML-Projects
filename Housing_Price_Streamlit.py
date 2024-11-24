import streamlit as st
import numpy as np
import joblib

st.title("House Price Prediction App")

# def load_model():
with open("mlr.pkl", "rb") as file:  
    model = joblib.load(file)
# return model
with open('scaler.pkl', 'rb') as f:
    scaler = joblib.load(f)

with open('pca.pkl', 'rb') as f:
    pca = joblib.load(f)


# ML = load_model()




num_rooms = st.number_input("Number of Bed Rooms", min_value=1, max_value=20, step=1)
area = st.number_input("Net Area (in sq. ft.)", min_value=50, max_value=750, step=50)
# area_per_bedroom = st.number_input("area_per_bedroom", min_value=5, max_value=120, step=1)
area_per_bedroom = area/num_rooms
centre_dist = st.number_input("Distance from the Nearest Center", min_value=10, max_value=2000, step=50)
floor = st.number_input("The Floor number", min_value=1, max_value=24, step=1)
metro_dist = st.number_input("Distance from the Nearest Metro", min_value=10, max_value=300, step=10)
age = st.number_input("Age", min_value=1, max_value=90, step=1)
# Map categorical input if needed


# Button to make predictions
if st.button("Predict"):
    
    user_input = np.array([[area, centre_dist, metro_dist, floor, age, area_per_bedroom]])
    # if prediction<0:
    #     tr = -prediction
    # else:
    #     tr = prediction
    user_input_scaled = scaler.transform(user_input)

    # Apply PCA to the scaled input
    user_input_pca = pca.transform(user_input_scaled)

    # Make prediction using the model
    prediction = model.predict(user_input_pca)[0]
    st.write(prediction)
