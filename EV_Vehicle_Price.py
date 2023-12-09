import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import pickle
from PIL import Image

#load trained model
model = joblib.load("best_model1.pkl")

# Define the app title and layout
st.title("Electric Vehicle Price Prediction")
st.text('How Much Does an Electric Car Cost?')

image = Image.open('dataset2-cover.jpg')
st.sidebar.image(image, caption='Electric Vehicles')
#Vehicle_make = st.sidebar.selectbox ('Make',('Ford','Ram','Land Rover' ,'Nissan','Chevrolet','BMW','Aston Martin','Infiniti','Bentley','Dodge','Maserati','Bugatti','Mercedes-Benz','Cadillac','GMC','Audi','Rolls-Royce','Lamborghini','Jeep'))
st.sidebar.markdown("Thinking it's time to ditch gas and go electric? It's a good idea, but it's important to have a budget in mind because depending on the model you choose, you'll see massive differences in price. Though most electric vehicles (EVs) are still more expensive than comparable gasoline-powered models, the difference is getting smaller, year by year. When you consider the cost of fuel, maintenance and purchase incentives, the price differences are reduced or eliminated. With increasing ranges and lower relative costs, today's EVs are no longer just niche vehicles. There are now models in nearly every vehicle class from compact hatchbacks to sports cars to full-size pickup trucks.", help=None)

# Define input fields for features

Battery = st.number_input("Battery Size", min_value=50, max_value=500, value=50, step=1)
Efficiency = st.number_input("Energy efficiency rating of the vehicle", min_value=100.0, max_value=500.0, value=100.0, step=20.0)
Range = st.slider("Range of veicle on a single charge", 150, 1000)
Fast_Charge = st.number_input("Fast Charge ",min_value =100, max_value=1000, step=20)
Top_Speed = st.number_input("Top Speed ",min_value =100, max_value=500, step=30)
Accelaration_Time = st.number_input("Accelaration Time ",min_value =1, max_value=20, step=2)


#prediction
if st.button('predict'):
    Make_Prediction = model.predict([[Fast_Charge,Battery,Efficiency,Range,Top_Speed,]])
    output = round(Make_Prediction[0],3)
    st.success('Electric Vehicle Price {}'.format(output))