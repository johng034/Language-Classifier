import pickle
import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
import pyautogui
import re
# import numpy as np

# DOCUMENTATION
# Streamlit
# https://docs.streamlit.io/en/stable/getting_started.html


# save the model to disk
model_file = './saved-items/naive_bayes.sav'
language_file = './saved-items/languages.sav'
# naive = 'naive.sav'
 
# load the model from disk
model = pickle.load(open(model_file, 'rb'))
languages = pickle.load(open(language_file, 'rb'))
# naive = pickle.load(open(n, 'rb'))

# Preprocess function
def preprocess(text):
    text = re.sub("[\[\[\]\]?—\"\"«»]", "", text)  # Remove special characters
    text = text.replace('\u200b', '')
    text = re.sub("-", " ", text)  # Replace '-' with a space
    text = " ".join(text.split())  # Remove any extra spaces
    text = text.lower()
    
    return text

# Streamlit app
st.title("Language Classifier")

# Summary
st.markdown("Hello and welcome! For this project, I trained a Naive Bayes Classifier to \
            predict which language the user types in. so yeah")

# def run_algo():
text = st.text_input("Please type a sentence: ")
text = preprocess(text)

if bool(text) or st.button("Classify"):
    if not bool(text):
        st.subheader("Please type a sentence.")
        if st.button('Reset'):
            pyautogui.hotkey('command','r')
        else:
            time.sleep(5)
            pyautogui.hotkey('command','r')

    else:
        st.header("Prediction")
        prediction = str(model.predict([text])[0])
        st.subheader("The classifier predicts this language is: ")
        time.sleep(0.2)
        probabilities = model.predict_proba([text])
        probs = probabilities[0]

        if all([x == probs[0] for x in probs]):
            st.subheader('Unsure')
            st.markdown("The model is not sure which language this is. Any prediction would be a random guess. \
            Please try again with more text.")
            if st.button('Reset'):
                pyautogui.hotkey('command','r')
        else:
            st.subheader(prediction)


            # Bar graph
            # probabilities = model.predict_proba([text])
            # st.text(probabilities)
            # st.text(languages)

            df = pd.DataFrame(probabilities, columns=languages)
            # st.dataframe(df)

            fig, ax = plt.subplots()
            ax.bar(x=languages, height=probabilities.reshape(10,), width=0.8)
            ax.tick_params(labelrotation=45)
            st.pyplot(fig)

            # st.markdown((naive.coef_.size))

            # plt.figure(figsize=(12, 8))
            # plt.bar(x=langs, height=pred_probs.reshape(10,), width=0.8)
            # plt.show()

            # st.bar_chart(df)
            if st.button('Reset'):
                pyautogui.hotkey('command','r')
