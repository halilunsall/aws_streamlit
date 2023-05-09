
# IMPORT AND USER-DEFINE FUNCTIONS

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle
from bs4 import BeautifulSoup
import requests


def html_options(text=None, align="left", size=12, weight="normal", style="normal", color="#F4A460", bg_color=None, bg_size=16, on='main', to_link=None, image_width=None, image_height=None, image_source=None, image_bg_color=None):
    if on == 'main':
        st.markdown(f"""<div style="background-color:{bg_color};padding:{bg_size}px">
        <h2 style='text-align: {align}; font-size: {size}px; font-weight: {weight}; font-style: {style}; color: {color};'>{text} </h2>
        </div>""", unsafe_allow_html=True)
    elif on == 'side':
        st.sidebar.markdown(f"""<div style="background-color:{bg_color};padding:{bg_size}px">
        <h2 style='text-align: {align}; font-size: {size}px; font-weight: {weight}; font-style: {style}; color: {color};'>{text} </h2>
        </div>""", unsafe_allow_html=True)
    elif on == 'link':
        image_style = f"background-color:{image_bg_color};" if image_bg_color else ""
        st.markdown(f"""<div style="text-align: {align};"> <a href="{to_link}"><img width="{image_width}" height="{image_height}" src="{image_source}" style="{image_style}" /></a></div>""", unsafe_allow_html=True)



# HEAD TO PICTURE
html_options(text='Car Price Prediction App', align='center', size=50, weight='bold', color='#FFA500', bg_color='#000000')


st.write('')
st.info('This app predicts **car prices** for you!')
st.write('')
st.write('')
st.image("https://www.motortrend.com/uploads/2022/03/2022-Honda-Civic-Touring-vs-2022-Hyundai-Elantra-Limited-vs-2022-Kia-Forte-GT-vs-2022-Mazda-Mazda3-Sedan-AWD-Turbo-vs-2022-Nissan-Sentra-SR-vs-2022-Volkswagen-Jetta-SEL-19.jpg?fit=around%7C875:492", use_column_width=True)
st.write('')
st.write('')



# SIDEBAR 
html_options(text='Configurate your car', align='center', size='30', weight='bold', color='#32C823', on='side', bg_color='#000000')
st.sidebar.write('')
model = st.sidebar.selectbox('Scikit-Learn Model', ['Select', 'Lasso', 'Random Forest', 'XGBoost'])
if model == 'Lasso':
    st.sidebar.warning('This model has a high error rate.')
elif model == 'XGBoost':
    st.sidebar.warning('This model is out of use as it is under development.')
st.sidebar.write('')
make_model = st.sidebar.selectbox('Make and Model', ['Select','Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia','Renault Clio', 'Renault Espace', "Other"])
st.sidebar.write('')
Type = st.sidebar.selectbox('Type Status', ['Select',"Used", "Employee's car", "Demonstration", "Pre-registered", "New", "Other"])
st.sidebar.write('')
age = st.sidebar.slider('Car Age', 0, 20, 10, 1)
st.sidebar.write('')
km = st.sidebar.slider('Km', min_value=0, max_value=320000, value=160000, step=1000)
st.sidebar.write('')
hp_kW=st.sidebar.slider("Engine Size", min_value=40, max_value=200, value=100, step=5)
Gearing_Type = st.sidebar.radio('Gearing Type', ('Automatic', 'Manual', 'Semi-automatic'))
st.sidebar.write('')
st.sidebar.write('')
Gears = st.sidebar.radio('Gears', [5,6,7,8])


# Create a dataframe using feature inputs
if model == 'Lasso':
    data = {'make_model': make_model,
                'age': age,
                'hp_kW': hp_kW,
                'km': km,
            'Type': Type,
            'Gearing_Type': Gearing_Type}
elif model == 'Random Forest':
    data = {'make_model': make_model,
                'age': age,
                'Gearing_Type': Gearing_Type,
                'Gears': Gears,
            'hp_kW': hp_kW}



model_rf=pickle.load(open('rf_model', "rb"))
model_lasso=pickle.load(open('lasso_model', "rb"))

# CAR TABLE
html_options(text='Car Features', size=40, weight='bold', color='#FFA500', align='center')
st.write('')
try:
    df = pd.DataFrame.from_dict([data])
    st.table(df.rename(columns={'make_model':'Make Model', 'age':'Age', 'Gearing_Type':'Gearing Type', 'hp_kW':'Engine Size', 'km':'Km'}))
except:
    pass


# PREDICTION

predict = st.button("Predict")
if model == 'Lasso':
    result = str(model_lasso.predict(df)[0])
elif model == 'Random Forest':
    result = str(model_rf.predict(df)[0])



def car_info(image_url, title_num=1):
    base_url = 'https://en.wikipedia.org/wiki/{}'
    st.write()
    st.image(image_url)
    st.write()
    r = requests.get(base_url.format(make_model))
    soup = BeautifulSoup(r.content, 'html')
    first = soup.find('div', {'class':'mw-parser-output'})
    titles = first.find_all('p')

    wiki_text = ''
    for num in range(1, title_num+1):
        wiki_text += titles[num].text.replace('[1]', '').replace('[2]', '').replace('[3]', '').replace('[4]', '').replace('[5]', '').strip()+' '
    html_options(align='center',size=25,text=wiki_text, color='#FFF5EE')
    html_options(on='link', align='center',to_link=base_url.format(make_model), image_height=150, image_width=300, image_source="https://media.istockphoto.com/id/1287057320/vector/more-info-button-rounded-sign-on-white-background.jpg?s=612x612&w=0&k=20&c=iS2ANd4VHjWopfcT1xgdDlpc7p1AHnnyDzVCu-Tm10w=", image_bg_color='#FFFFFF')


if predict:
    if make_model == 'Select' or model == 'Select' or Type=='Select':
        st.warning("Please make sure you choose 'Scikit-Learn Model', 'Make and Model' and 'Type Status'!")
    elif model == 'XGBoost':
        st.info('The model you selected is currently not available.')
    else:
        st.balloons()
        st.success(result[:8]+' $')
        # MORE INFORMATION
        html_options(text='Information About Car',align='center', size=40, weight='bold')
        
        if make_model == 'Audi A1':
            car_info('https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Audi_metroproject_quattro_concept.JPG/1024px-Audi_metroproject_quattro_concept.JPG')
        elif make_model == 'Audi A3':
            car_info('https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Audi_A3_8Y_Sedan_IMG_5936.jpg/1920px-Audi_A3_8Y_Sedan_IMG_5936.jpg', title_num=2)
        elif make_model == 'Opel Corsa':
            car_info('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Opel_Corsa-e_at_IAA_2019_IMG_0738.jpg/1280px-Opel_Corsa-e_at_IAA_2019_IMG_0738.jpg', title_num=2)
        elif make_model == 'Opel Astra':
            car_info('https://upload.wikimedia.org/wikipedia/commons/c/c0/Opel_Astra_L_1X7A6738.jpg')
        elif make_model == 'Opel Insignia':
            car_info('https://upload.wikimedia.org/wikipedia/commons/e/ed/Opel_Insignia_Sports_Tourer_1.5_DIT_Innovation_%28B%29_%E2%80%93_Frontansicht%2C_12._Mai_2017%2C_D%C3%BCsseldorf.jpg')
        elif make_model == 'Renault Clio':
            car_info('https://upload.wikimedia.org/wikipedia/commons/f/f0/2019_Renault_Clio_Iconic_TCE_1.0_Front.jpg')
        elif make_model == 'Renault Espace':
            car_info('https://upload.wikimedia.org/wikipedia/commons/2/2c/2015-present_Renault_Espace_Front.jpg')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
html_options(text='More information about me:', size=30, color='#E6FFFB', bg_color='#3ABCA7', weight='bold', style='italic')
st.write('')
st.write('')


col1, col2, col3 = st.columns(3)

with col1:
    html_options(on='link', to_link='https://www.linkedin.com/in/halilibrahimunsal/', image_height=60, image_width=60, image_source="https://unpkg.com/simple-icons@v8/icons/linkedin.svg", image_bg_color='#FFFFFF')
with col2:
    html_options(on='link', to_link='https://github.com/halilunsall', image_height=60, image_width=60, image_source="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg", image_bg_color='#FFFFFF')
with col3:
    html_options(on='link', to_link='https://public.tableau.com/app/profile/halilunsal', image_height=60, image_width=60, image_source="https://cdn.worldvectorlogo.com/logos/tableau-software.svg", image_bg_color='#FFFFFF')

