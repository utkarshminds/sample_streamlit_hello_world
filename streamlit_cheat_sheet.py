import streamlit as st
import pandas
import numpy

#https://docs.streamlit.io/get-started/fundamentals/main-concepts

#to give title to website
st.title("My first website")

st.header('Editable excel')
df = pandas.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

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
else:
    st.write('Sorry you cant continue')

#Homework-Allow user to perform add, subtract, divide,
#multiply operation 
#select from checkbox 
#perform

st.subheader('Dropdown or select')
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)

#Currency converter
#take from user in rupees and ask 
#to convert in euro, dollar, yen (dropdown)



#true or false
st.subheader('Button click')
click = st.button("Click me")

if click:
    st.write('clicked')
else:
    st.write('not clicked')

st.subheader('Hyperlink')
st.page_link("app.py", label="App.py")

st.subheader('Display') 
st.image("poster.jpeg")

st.sidebar.header('Radio buttons')
a = st.sidebar.radio("Select one:", [1, 2], key='main2')
st.sidebar.write(a)

st.header('Radio buttons')
a = st.radio("Select one:", [1, 2], key='main')
st.write(a)

st.subheader('Feeback using thumbs')
selected = st.feedback("thumbs")
st.write(selected)

if selected:
    st.write('Feeback is good')
else:
    st.write('Feedback is poor')


st.header('Feedback in faces')
selected = st.feedback("faces")
st.write(selected)

if selected > 3:
    st.write('good job')
    st.balloons()
else:
    st.write('improve')
    st.snow()

st.header('Feedback in stars')
selected = st.feedback("stars")
st.write(selected)

st.subheader('Select your pills choice')
selected = st.pills("Tags", ["Sports", "Politics"])
st.write(selected)

st.header('Radio buttons')
selected = st.radio("Pick one", ["cats", "dogs"])
st.write(selected)

st.header('Segmented control')
st.segmented_control("Filter", ["Open", "Closed"])

st.header('Toggle')
st.toggle("Enable")

st.header('Multiselect dropdown')
st.multiselect("Buy", ["milk", "apples", "potatoes"])

st.header('Take input from user using text box')
text_data = st.text_input("First name")

st.write(text_data.upper())


st.header('Take input from user')
number = st.number_input("Pick a number", 0, 10)
st.write('square = ', number * number)

st.header('Take input using text area')
st.text_area("Text to translate")

st.header('Take input using date area')
st.date_input("Your birthday")

st.header('Time input')
st.time_input("Meeting time")

st.header('Upload files')
st.file_uploader("Upload a CSV")

st.header('Recorder of audio')
st.audio_input("Record a voice message")

st.header('Camera input')
st.camera_input("Take a picture")

st.header('Color input')
st.color_picker("Pick a color")


#message types
if st.button('Click me for ballons and snow:'):
    st.balloons()
    st.snow()

st.header('Messages list')
st.toast("Warming up...")
st.error("Error message")
st.warning("Warning message")
st.info("Info message")
st.success("Success message")
st.exception('error')

'''
Homework
========

1. Calculator
2. Rock paper scissor game
3. Currency converter
4. Feedback of image
5. Feedback or registration form
6. Upload a dataset and get data viz
7. Portfolio website
8. dashboard  
'''