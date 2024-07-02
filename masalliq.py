import streamlit as st
import requests
import json
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

st.header("Ovqat nomini yozing va tezda tayyorlang", )
matn = st.chat_input('Ovqat nomini kiriting..')
if matn != None:
    querystring = {"tags":matn,"number":"1"}

    headers = {
        "x-rapidapi-key": "dc521e16e1msh8a91d612c2d7f38p1e17cajsnd665a5824996",
        "x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(type(response.json()['recipes'][0]))
    st.json(response.json()['recipes'])

    