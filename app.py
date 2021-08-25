from pycaret.classification import load_model, predict_model
import streamlit as st
import numpy as np
import pandas as pd


def predict_quality(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    return predictions_data['Label'][0]
    

model = load_model('diamond-pipeline')


st.title('Diamond Price Prediction')
st.write('This is a web app to classify the quality of your wine based on\
         several features that you can see in the sidebar. Please adjust the\
         value of each feature. After that, click on the Predict button at the bottom to\
         see the prediction of the classifier.')
         
         
        
carat = st.number_input(label = 'Carat Value', min_value = 0.0,max_value = 5.0 ,value = 0.7,step = 0.1)

color = st.number_input(label = 'Color Value from Worst to Best', min_value = 0,max_value = 6 ,value =3 ,step = 1)

clarity = st.number_input(label = 'Clarity Value from Worst to Best', min_value = 1,max_value = 8 ,value = 3,step = 1)


x = st.number_input(label = 'Length(mm)', min_value = 0.0,max_value = 10.80 ,value = 5.71,step = 0.1)
                          
y = st.number_input(label = 'Width(mm)', min_value = 0.0,max_value = 58.50 ,value = 5.71,step = 0.1)                          

z = st.number_input(label = 'Depth(mm)', min_value = 0.0,max_value = 31.50 ,value = 3.5,step = 0.1)

depth = st.number_input(label = 'Total Depth percentage', min_value = 43.000, max_value = 79.0  ,value = 61.0,step = 1.0)

table = st.number_input(label = 'Table( width of top of diamond)', min_value = 43.0 ,max_value = 95.0 ,value = 57.0,step = 1.0)

cut = st.radio(
     "What type of Cut do you want?",
    ('Ideal', 'Premium', 'Very Good','Good','Fair'))
                       
                          
features = {'carat':carat, 'x':x, 'y':y, 'z':z,'clarity':clarity,
            'depth':depth,'table':table, 'cut':cut,'color':color
           }
 

features_df  = pd.DataFrame([features])

print(features_df)

#st.table(features_df)  

if st.button('Predict'):
    
    prediction = predict_quality(model, features_df)
    
    st.write(' Based on feature values, Price of Diamond $'+ str(prediction)+" US dollars")