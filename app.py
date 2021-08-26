from pycaret.classification import load_model, predict_model
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import base64


def predict_quality(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    return predictions_data['Label'][0]
    

model = load_model('diamond-pipeline')
st.sidebar.title('Diamond Price Prediction')

#image = Image.open('diamond.gif')
#st.sidebar.image(image)

file_ = open("diamond.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.sidebar.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="diamond gif" style="width:100%;">',
    unsafe_allow_html=True,
)
st.sidebar.text("")
st.sidebar.text("")
# st.write('This is a web app to classify the quality of your wine based on\
#          several features that you can see in the sidebar. Please adjust the\
#          value of each feature. After that, click on the Predict button at the bottom to\
#          see the prediction of the classifier.')
         
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5,col6 = st.columns(2)
col7,col8 = st.columns(2)
#col1.header("")
carat = col8.number_input(label='Carat Value',min_value = 0.0,max_value = 5.0 ,value = 0.7,step = 0.1)
#col2.header("")
color = st.slider(label='Color Value from Worst to Best',min_value = 0,max_value = 6 ,value =3 ,step = 1)
clarity = st.slider(label = 'Clarity Value from Worst to Best', min_value = 1,max_value = 8 ,value = 3,step = 1)
x = col3.number_input(label = "Length(mm)", min_value = 0.0,max_value = 10.80 ,value = 5.71,step = 0.1)
#col4.header("")                          
y = col4.number_input(label = 'Width(mm)', min_value = 0.0,max_value = 58.50 ,value = 5.71,step = 0.1)                          
#col5.header("")
z = col5.number_input(label = 'Depth(mm)', min_value = 0.0,max_value = 31.50 ,value = 3.5,step = 0.1)
#col6.header("")
depth = col6.number_input(label = 'Total Depth percentage', min_value = 43.000, max_value = 79.0  ,value = 61.0,step = 1.0)
#col7.header("")
table = col7.number_input(label = 'Table(width of top of diamond)', min_value = 43.0 ,max_value = 95.0 ,value = 57.0,step = 1.0)
#col8.header("")
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
cut = st.radio(
     "What type of Cut do you want?",
    ('Ideal', 'Premium', 'Very Good','Good','Fair'))
                       
                          
features = {'carat':carat, 'x':x, 'y':y, 'z':z,'clarity':clarity,
            'depth':depth,'table':table, 'cut':cut,'color':color
           }
features_df  = pd.DataFrame([features])

print(features_df)

c1,c2,c3 = st.sidebar.columns(3)
if c2.button('Predict'):
    
    prediction = predict_quality(model, features_df)
    
    st.sidebar.success(' Based on feature values, Price of Diamond $'+ str(prediction)+" US dollars")
