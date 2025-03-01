import streamlit as st
import pandas
import numpy

#https://docs.streamlit.io/get-started/fundamentals/main-concepts

#to give title to website
st.title("My first website")

st.header('My data in a table')
#table with two columns
data = pandas.DataFrame(
    {
        'roll_no': [1,2,3],
        'name': ['raju', 'ravi', 'shyam']
    }
)
st.write(data)

st.header('My line chart')
chart_data = pandas.DataFrame({
    'a': [1,2,3,4,5],
    'b': [6,7,8,9,10],
    'c': [10,20,30,40,50]
})

st.line_chart(chart_data)

st.subheader('Bar chart')
st.bar_chart(chart_data)

st.subheader('Scatter chart')
st.scatter_chart(chart_data)

#map
st.subheader('Map')
map_data = pandas.DataFrame({
    'lat': [37],
    'lon': [122]
    })

st.map(map_data)

st.subheader('User input and square it')
x = st.slider('select the number', key='square')  
st.write('The number squared is', x * x)

st.subheader('User input and half it')
x = st.slider('select the number', key='half')  
st.write('The number divided by 2 is', x/2)

st.subheader('User input and find even or odd')
x = st.slider('select the number', key='odd_even')  
if x % 2 == 0:
    st.write('The number is even')
else:
    st.write('The number is odd')

#Home work - Person can vote or not
#Take input from slider of age
#with if else give the decision >18 (vote) / <18 (cant vote)


#True or false
st.subheader('Checkbox - Do you accept terms and condition')
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)


#true or false
click = st.button("Click me")

if click:
    st.write('clicked')
else:
    st.write('not clicked')
 
st.page_link("app.py", label="Home")
 
st.image("sample.png")

a = st.sidebar.radio("Select one:", [1, 2])
st.sidebar.write(a)

selected = st.feedback("thumbs")
st.write(selected)

selected = st.feedback("faces")
st.write(selected)

selected = st.feedback("stars")
st.write(selected)

selected = st.pills("Tags", ["Sports", "Politics"])
st.write(selected)

selected = st.radio("Pick one", ["cats", "dogs"])
st.write(selected)

st.segmented_control("Filter", ["Open", "Closed"])

st.toggle("Enable")

st.selectbox("Pick one", ["cats", "dogs"])

st.multiselect("Buy", ["milk", "apples", "potatoes"])

text_data = st.text_input("First name")

st.write(text_data.upper())



number = st.number_input("Pick a number", 0, 10)
st.write('square = ', number * number)

st.text_area("Text to translate")


st.date_input("Your birthday")

st.time_input("Meeting time")

st.file_uploader("Upload a CSV")

st.audio_input("Record a voice message")

st.camera_input("Take a picture")

st.color_picker("Pick a color")


#message types
st.balloons()
st.snow()
st.toast("Warming up...")
st.error("Error message")
st.warning("Warning message")
st.info("Info message")
st.success("Success message")
st.exception('error')

