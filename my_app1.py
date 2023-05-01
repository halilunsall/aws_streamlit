import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#Title
st.title("This is a title")
st.text("This is some text")

#Markdown
st.markdown('Streamlit is **_really_ cool** :+1:')
st.markdown("# This is a markdown")

# Header/Subheader
st.header('This is a header')
st.subheader('This is a subheader')

#Video Açma
#my_video = open("ml.mov",'rb')
#st.video(my_video)


st.success('Successfully')
st.info('Info Message')
st.error('This is an error!')
st.write('wassup')
st.image(Image.open('images.jpeg'))

df = pd.read_csv('Advertising.csv')
st.dataframe(df.describe())

st.video("https://www.youtube.com/watch?v=_c1w056MItU&list=RD_c1w056MItU&start_radio=1")

st.bar_chart(df)

# Add checkbox
st.checkbox("Up and Down")
cbox= st.checkbox("Hide and Seek")
if cbox:
    st.write('Clicked')
else:
    st.write('Not Clicked')

# Add radio button
status = st.radio("Select a color",("blue","orange","yellow"))
st.write("My favorite color is ", status)

# Add button
clicked = st.button("Merry Christmas")
if clicked:
    st.snow()

# Add select box
occupation=st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor"])
st.write("Your Occupation is ", occupation)
xd= "SCIENCE BITCHH!"
if occupation == 'DataScientist':
   st.code(xd) 

# Multi_select
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])

st.write(f"You selected {len(multi_select)} number(s)")
st.write(f"Sum Numbers:{sum(multi_select)}")

# Slider
option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=3)
option2 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=5.2, step=0.2)

st.write(f"Your result is: {option1+option2}")

result=option1*option2
st.write("multiplication of two options is:",result)

# Text_input
name = st.text_input("Enter your name", placeholder="Your name here")

if name == 'xd':
    st.write('31')
else:
    st.write('Hello ',name)

# Code  # to show as if code
st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np")

# Echo  # it is used "with block" to draw some code on the app, then execute it
with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df

# Date input
import datetime
today=st.date_input("Today is", datetime.datetime.now())
date=st.date_input("Enter the date")

# Time input
the_time=st.time_input("The time is", datetime.time(8, 45))
hour=st.time_input(str(pd.Timestamp.now()))
st.write("Hour is", hour)

# Sidebar
st.sidebar.title("Menu")
st.sidebar.header("Pages")

# Sidebar with slider
a=st.sidebar.slider( "input1",0,5,2,1)
x=st.sidebar.slider( "input2" )
st.write("slidebar input result")
st.success(a*x)

# Dataframe
df=pd.read_csv("Advertising.csv")

# To display dataframe there are 3 methods

# Method 1
st.table(df.head())
# Method 2
st.write(df.head())  # dynamic, you can sort
st.write(df.isnull().sum())
# Method 3
st.dataframe(df.describe().T)  # dynamic, you can sort

import pickle
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))

# To take feature inputs
TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)

# Create a dataframe using feature inputs
my_dict = {"TV":TV,
           "radio":radio,
           "newspaper":newspaper}

df = pd.DataFrame.from_dict([my_dict])
st.table(df)


# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])

