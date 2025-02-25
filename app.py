import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image


pickle_in = open("model_1.pkl","rb")
classifier=pickle.load(pickle_in)
def welcome():
    return "Welcome All"

def predict_note_authentication(Property_Type,Property_Area,Number_of_Windows,Number_of_Doors,Furnishing,Frequency_of_Powercuts,Power_Backup,Water_Supply,Traffic_Density_Score,Crime_Rate,Dust_and_Noise,Air_Quality_Index,Neighborhood_Review):
    

   
    prediction=classifier.predict([[Property_Type,Property_Area,Number_of_Windows,Number_of_Doors,Furnishing,Frequency_of_Powercuts,Power_Backup,Water_Supply,Traffic_Density_Score,Crime_Rate,Dust_and_Noise,Air_Quality_Index,Neighborhood_Review]])
    print(prediction)
    return prediction



def main():
    st.title("Liveability Score")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">ML Model to predict the livebality score based on 13 parameters given below </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Property_Type = st.text_input("Property_Type\n\r 1-Apartment\n\r2-Bunglaow\n\r3-Container Home\n\r4-Duplex\n\r5-Single Family Home ")
    Property_Area = st.text_input("Property_Area")
    Number_of_Windows = st.text_input("Number_of_Windows")
    Number_of_Doors = st.text_input("Number_of_Doors")
    Furnishing = st.text_input("Furnishing \n\r1-Furnished\n\r2-Unfurnished")
    Frequency_of_Powercuts = st.text_input("Frequency_of_Powercuts")
    Power_Backup = st.text_input("Power_Backup\n\r1-No\n\r2-Yes")
    Water_Supply = st.text_input("Water_Supply\n\r0-All Time\n\r1-Not Mentioned\n\r2-Once in the day-Evening\n\r3-Once in the dat-Morning\n\r4-Once in two days")
    Traffic_Density_Score = st.text_input("Traffic_Density_Score")
    Crime_Rate = st.text_input("Crime_Rate\n\r1-Slightly Below Average\n\r2-Well Above Average\n\r3-Well Below Average")
    Dust_and_Noise = st.text_input("Dust_and_Noise\n\r0-High\n\r1-Medium\n\r2-Low")
    Air_Quality_Index = st.text_input("Air_Quality_Index")
    Neighborhood_Review = st.text_input("Neighborhood_Review")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Property_Type,Property_Area,Number_of_Windows,Number_of_Doors,Furnishing,Frequency_of_Powercuts,Power_Backup,Water_Supply,Traffic_Density_Score,Crime_Rate,Dust_and_Noise,Air_Quality_Index,Neighborhood_Review)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()