import streamlit as st
import joblib 
model=joblib.load('sentiment_analyzer')
st.title('Amazon Review Prediction')
ip = st.text_input("Enter the Review")
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])  
   
