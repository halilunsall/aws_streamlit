
# IMPORT AND USER-DEFINE FUNCTIONS

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle


def text(text, align="left", size=12, weight="normal", style="normal", color="#F4A460", on='main'):
    if on == 'side':
        st.sidebar.write(
            f"<div style='text-align: {align}; font-size: {size}px; font-weight: {weight}; font-style: {style}; color: {color};'>{text}</div>",
        unsafe_allow_html=True)
    elif on == 'main':
        st.write(
        f"<div style='text-align: {align}; font-size: {size}px; font-weight: {weight}; font-style: {style}; color: {color};'>{text}</div>",
        unsafe_allow_html=True)


# HEAD TO PICTURE
text(text='Car Price Prediction App', align='center', size=50, weight='bold', color='#9ACD32')

st.write('')
st.info('This app predicts **car prices** for you!')
st.write('')
st.write('')
st.image("image.jpg", use_column_width=True)
st.write('')
st.write('')


# ABOUT DATA
df = pd.read_csv('last_data.csv')
text(text='About Data', size=40, weight='bold')
st.write('')
st.bar_chart(data=df, x='make_model', y='price')
st.write('')
st.bar_chart(data=df, x='Gearing_Type', y='price')
st.write('')
st.area_chart(data=df, x='hp_kW', y='price')


# SIDEBAR 
text(text='Configurate your car', align='center', size='30', weight='bold', color='#87CEEB', on='side')
st.sidebar.write('')
make_model = st.sidebar.selectbox('Make and Model', ['Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia','Renault Clio', 'Renault Espace', "Other"])
st.sidebar.write('')
age = st.sidebar.slider('Car Age', 0, 20, 1)
st.sidebar.write('')
Gearing_Type = st.sidebar.radio('Gearing Type', ('Automatic', 'Manual', 'Semi-automatic'))
st.sidebar.write('')
Gears = st.sidebar.radio('Gears', [5,6,7,8])
st.sidebar.write('')
hp_kW=st.sidebar.slider("Engine Size", min_value=40, max_value=200, value=75, step=5)

# Create a dataframe using feature inputs
data = {'make_model': make_model,
            'age': age,
            'Gearing_Type': Gearing_Type,
            'Gears': Gears,
           'hp_kW': hp_kW}


filename = "final_model"
model=pickle.load(open(filename, "rb"))

# CAR TABLE
text(text='Car Features', size=40, weight='bold')
st.write('')
df = pd.DataFrame.from_dict([data])
st.table(df.rename(columns={'make_model':'Make Model', 'age':'Age', 'Gearing_Type':'Gearing Type', 'hp_kW':'Engine Size'}))



# PREDICTION
predict = st.button("Predict")
result = str(model.predict(df)[0])+' $'
if predict :
    st.balloons()
    st.success(result)
    # MORE INFORMATION
    text(text='Informatin About Car',align='center', size=40, weight='bold')
    if make_model == 'Audi A1':
        st.write()
        st.image("audia1.jpeg")
        st.write()
        text(align='center',size=25,text='The Audi A1 (internally designated Typ 8X) is a supermini car launched by Audi at the 2010 Geneva Motor Show. Sales of the initial three-door A1 model started in Germany in August 2010, with the United Kingdom following in November 2010. A five-door version, called Sportback, was launched in November 2011, with sales starting in export markets during spring 2012.', color='#FFF5EE')
        st.info('Please Click for More Information')
        st.write("[:car:](https://en.wikipedia.org/wiki/Audi_A1)")
    elif make_model == 'Audi A3':
        st.write()
        st.image("audia3.jpg")
        st.write()
        text(align='center',size=25,text='The Audi A3 is a subcompact executive/small family car (C-segment) manufactured and marketed by the German automaker Audi AG since September 1996, currently in its fourth generation.The first two generations of the Audi A3 were based on the Volkswagen Group A platform, while the third and fourth generations use the Volkswagen Group MQB platform.', color='#FFF5EE')
        st.info('Please Click for More Information')
        st.write("[:car:](https://en.wikipedia.org/wiki/Audi_A3)")
    elif make_model == 'Opel Corsa':
        st.write()
        st.image("opelcorsa.jpg")
        st.write()
        text(align='center',size=25,text='The Opel Corsa is a supermini car engineered and produced by the German automobile manufacturer Opel since 1982. Throughout its existence, it has been sold under a variety of other brands owned by General Motors (most notably Vauxhall, Chevrolet, and Holden) and also spawned various other derivatives.At its height of popularity, the Corsa became the best-selling car in the world in 1998, recording 910,839 sales with assembly operations in four continents and was sold under five marques with five different body styles. By 2007, over 18 million Corsas had been sold globally', color='#FFF5EE')
        st.info('Please Click for More Information')
        st.write("[:car:](https://en.wikipedia.org/wiki/Opel_Corsa)")
    elif make_model == 'Opel Astra':
        st.write()
        st.image("opelastra.jpg")
        st.write()
        text(align='center',size=25,text='The Opel Astra is a compact car/small family car (C-segment) developed and produced by the German automaker Opel since 1991, currently at its sixth generation. It was first launched in September 1991 as a direct replacement to the Opel Kadett. As of 2022, the car slots between the smaller Corsa supermini and the larger Insignia large family car.', color='#FFF5EE')
        st.info('Please Click for More Information')
        st.write("[:car:](https://en.wikipedia.org/wiki/Opel_Astra)")
    elif make_model == 'Opel Insignia':
        st.write()
        st.image("opelinsignia.jpg")
        st.write()
        text(align='center',size=25,text='The Opel Insignia is a large family car (D-segment in Europe) developed and produced by the German car manufacturer Opel since 2008. Taking its name from a 2003 concept car, the model line serves as the flagship Opel car line, slotted above the Astra and Corsa in size. The Insignia serves as the successor to both the Signum and Vectra model lines, replacing both vehicles under a single nameplate. Currently in its second generation, the model line is offered in four-door sedan/saloon body styles, five-door liftback, and as a five-door station wagon/estate.', color='#FFF5EE')
        st.info('Please Click for More Information')
        st.write("[:car:](https://en.wikipedia.org/wiki/Opel_Insignia)")
    elif make_model == 'Renault Clio':
        st.write()
        st.image("renaultclio.jpg")
        st.write()
        text(align='center',size=25,text="The Renault Clio is a supermini car (B-segment), produced by French automobile manufacturer Renault. It was launched in 1990, and entered its fifth generation in 2019. The Clio has had substantial critical and commercial success, being consistently one of Europe's top-selling cars since its launch, and it is largely credited with restoring Renault's reputation and stature after a difficult second half of the 1980s. The Clio is one of only two cars, the other being the Volkswagen Golf, to have been voted European Car of the Year twice, in 1991 and 2006.", color='#FFF5EE')
        st.info('Please Click for More Information')
        st.write("[:car:](https://en.wikipedia.org/wiki/Renault_Clio)")
    elif make_model == 'Renault Espace':
        st.write()
        st.image("renaultespace.jpg")
        st.write()
        text(align='center',size=25,text="The Renault Espace is a large five-door multi-purpose vehicle/MPV (M-segment) manufactured by Renault since 1984 for five generations. The first three generations of the Espace were amongst the first contemporary minivans or MPVs, and were manufactured by Matra for Renault. The fourth generation, also an MPV, was manufactured by Renault. The Renault Grand Espace is a long wheelbase (LWB) version with increased rear leg room and boot size. The fifth generation is introduced with a crossover SUV-inspired styling while keeping the space-oriented MPV body style. Renault described the fifth generation Espace as a 'crossover-style MPV' which combines elements of saloon, SUV and MPV, while retaining interior space and practicality of the latter. The sixth generation Espace will return as an SUV.", color='#FFF5EE')
        st.info('Please Click for More Information')
        st.write("[:car:](https://en.wikipedia.org/wiki/Renault_Espace)")