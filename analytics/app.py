import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import pandas as pd 
import requests

#endpoints 
api_url= 'http://127.0.0.1:8000/api/customer/'
swapi_endpoint = 'https://swapi.dev/api/people/1/'

#functions to fetch data 
def fetch_data(endpoint):
    response= requests.get(endpoint)
    data = response.json()
    return data 

def send_data(name, gender, age, favorite_number):
    gender_value = "0" if gender == "Female" else "1"
    data = {
        "name":name,
        "gender": gender_value,
        "age" : age,
        "favorite_number": favorite_number
    }

    response = requests.post(api_url, json=data)

    return response 


st.title("Analytics Dashboard")
st.write("v.0.0.1")

#layouts
col1, col2 = st.columns(2)

with col1:
    st.header('Column 1')
    st.write('some content')

    with st.expander("Click to choose something"):
        st.write('option to choose')
        st.write('another option to choose')
with col2:
    #Test Chart
    categories = ['A', 'B', 'C', 'D']
    values = np.random.randint(10,100, size=(4,))

    fig, ax = plt.subplots()
    ax.bar(categories, values, color='blue')
    ax.set_xlabel('categories')
    ax.set_ylabel('values')
    ax.set_title('First bar Chart')
    st.pyplot(fig)

#session state 
if 'counter' not in st.session_state:
    st.session_state.counter = 0

#increment button 
if st.button('increment'):
    st.session_state.counter +=1

st.write(f"Counter value : {st.session_state.counter}")

#data from SWAPIAPI 

swapi_data = fetch_data(swapi_endpoint)

st.write('Data from SWAPI API')
st.json(swapi_data)

#fetch data from our API

data = fetch_data(api_url)

if data:
    df = pd.DataFrame(data)

    st.dataframe(df)

    scatter_chart = alt.Chart(df).mark_circle().encode(
        x = 'age',
        y = 'favorite_number'
    )

    st.altair_chart(scatter_chart, use_container_width=True)


#form to collect customer data 
name = st.text_input("Your name")
gender = st.radio("Select your gender", ["Male", "Female"])
age = st.slider("Select your age")
favorite_number= st.number_input("Enter your fav number", step=1)


if st.button("Submit"):
    response = send_data(name,gender, age, favorite_number)

    if response.status_code ==201:
        st.success("New customer data created!")
        st.rerun()
    else:
        st.error("Something went wrong !!!")