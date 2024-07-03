import streamlit as st
import requests
import os

token = os.getenv('token')
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

st.header("Ovqat nomini yozing va tezda tayyorlang", )
matn = st.chat_input('Ovqat nomini kiriting..')
if matn != None:
    querystring = {"tags":matn,"number":"1"}

    headers = {
        "x-rapidapi-key": token,
        "x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(type(response.json()['recipes'][0]))
    st.json(response.json()['recipes'])

    