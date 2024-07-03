import streamlit as st
import requests
import os

token = os.getenv('token')
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

st.header("Ovqat nomini yozing va tezda tayyorlang", )
matn = st.chat_input('Ovqat nomini kiriting..')
try:
    if matn != None:
        querystring = {"tags":matn,"number":"1"}

        headers = {
            "x-rapidapi-key": token,
            "x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        heads = response.json()['recipes'][0]
        st.image(heads['image'], caption=heads['title'])
        st.markdown(heads['summary'], unsafe_allow_html=True)
        st.subheader('Tayyorlash ketma-ketligi')
        st.markdown(heads['instructions'],unsafe_allow_html=True)

        bases = heads['analyzedInstructions'][0]['steps']
        for i in range(0,len(bases)-1):
            tr = bases[i]['number']
            qadam_nomi = bases[0]['step']
            ingridient_nomi = bases[0]['step']['ingredients'][0]['name']
            # ingridient_rasmi = bases[0]['step']['ingredients'][0]['image']
            # equipment_nomi = bases[0]['step']['equipment'][0]['name']
            # equipment_rasmi = bases[0]['step']['equipment'][0]['image']
            
            st.markdown(f"""
                        {tr}. {qadam_nomi}
            """,unsafe_allow_html=True)
except Exception as e:
    st.error(f'Xatolik {str(e)}')
    