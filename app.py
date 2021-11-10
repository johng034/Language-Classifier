import os
os.environ['DISPLAY'] = ':0.0'
# os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'

import re
import time
import pickle
import pyautogui
import pandas as pd
import streamlit as st
import plotly.express as px
from platform import system

# DOCUMENTATION
# Streamlit
# https://docs.streamlit.io/en/stable/getting_started.html

# Model path
model_file = './saved-items/naive_bayes.sav'
language_file = './saved-items/languages.sav'
 
# Load the model
model = pickle.load(open(model_file, 'rb'))
languages = pickle.load(open(language_file, 'rb'))

# Operating System (for pyautogui.hotkey on lines 57, 71, and 88
sys_name = system()
system_keys = {
    'Windows': 'ctrl',
    'Darwin': 'command',
    'Linux': 'ctrl'
}

# Preprocess function
def preprocess(text):
    text = re.sub("[\[\[\]\]?—\"\"«»]", "", text)  # Remove special characters
    text = text.replace('\u200b', '')
    text = re.sub("-", " ", text)  # Replace '-' with a space
    text = " ".join(text.split())  # Remove any extra spaces
    text = text.lower()
    
    return text

# Streamlit app
st.set_page_config(page_title='Language Classifier', page_icon='🗣')
st.title("Language Classifier")


# Welcome message
st.markdown("Hello and welcome! For this project, I trained a Naive Bayes classifier to \
            predict the language you type in. Please try it out and see how it performs!")

text = st.text_input("Please type a sentence: ")
text = preprocess(text)

if bool(text) or st.button("Classify"):
    if not bool(text):
        st.subheader("Please type a sentence.")
        if st.button('Reset'):
            pyautogui.hotkey(system_keys[sys_name],'r')

    else:
        prediction = str(model.predict([text])[0])
        st.subheader("The classifier predicts this language is: ")
        time.sleep(0.2)
        probabilities = model.predict_proba([text])
        probs = probabilities[0]

        if all([x == probs[0] for x in probs]):  # In case the model cannot predict the language
            st.subheader('Unsure')
            st.markdown("The model is not sure which language this is. Any prediction would be a random guess. \
            Please try again with more text.")
            if st.button('Reset'):
                pyautogui.hotkey(system_keys[sys_name],'r')

        else:
            st.subheader(prediction)

            # DataFrame with prediction probabilities
            results = {
                'Language': [languages[i] for i in range(len(languages))],
                'Probability': [probs[i] for i in range(len(probs))]
            }
            df = pd.DataFrame(results)

            # Plot a bar chart of predictions
            fig = px.bar(df, x=df.Language, y=df.Probability, title='Probability of Each Language')
            st.plotly_chart(fig)

            if st.button('Reset'):
                pyautogui.hotkey(system_keys[sys_name],'r')
