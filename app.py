import pickle
import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt


# DOCUMENTATION
# Streamlit
# https://docs.streamlit.io/en/stable/getting_started.html


# save the model to disk
filename = 'finalized_model.sav'
file = 'language.sav'
 
# load the model from disk
model = pickle.load(open(filename, 'rb'))
languages = pickle.load(open(file, 'rb'))

# symbols = set(punctuation)
# text = input('Please type a phrase: ').lower()

# print(text)
# print(model.predict([text]))


# Streamlit app
st.title("Language Classifier")

# Summary
st.text("Hello and welcome! For this project, I trained a Naive Bayes Classifier to predict which language the user types in.")

# text = st.text_input("Please type a sentence: ")

# if bool(text) or st.button("Classify"):
#     # st.button("New sentence")
#     # print('')
#     st.header("Prediction")
#     prediction = str(model.predict([text])[0])
#     # time.sleep(1)
#     st.subheader("The classifier predicts this language is: ")
#     time.sleep(0.2)
#     st.subheader(prediction)
#     # if st.button("New sentence"):
#     #     pass

# def run_algo():
text = st.text_input("Please type a sentence: ")

if bool(text) or st.button("Classify"):
    # st.button("New sentence")
    # print('')
    st.header("Prediction")
    prediction = str(model.predict([text])[0])
    # time.sleep(1)
    st.subheader("The classifier predicts this language is: ")
    time.sleep(0.2)
    st.subheader(prediction)


    # Bar graph
    probabilities = model.predict_proba([text])
    # st.text(probabilities)
    # st.text(languages)

    df = pd.DataFrame(probabilities, columns=languages)
    # st.dataframe(df)

    fig, ax = plt.subplots()
    ax.bar(x=languages, height=probabilities.reshape(10,), width=0.8)
    st.pyplot(fig)

    # plt.figure(figsize=(12, 8))
    # plt.bar(x=langs, height=pred_probs.reshape(10,), width=0.8)
    # plt.show()

    # st.bar_chart(df)



    # if st.button("New sentence"):
    #     run_algo()


# run_algo()
# if st.button("New sentence"):
#     run_algo()


# time.sleep(8)

# if st.button('Hit me'):
#     print('button press')

# st.text(text)
# # Input
# # text = st.text_input("Please type a sentence: ")

# # while text != "":        # Loop until it is a blank line
# #     text = st.text_input("Please type a sentence: ")

# st.header("Prediction")

# prediction = str(model.predict([text])[0])
# st.subheader("The classifier predicts this language is: " + prediction)

# # print(st.__file__)