import streamlit as st
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pickle
from auxfn import emojiMask, cleanSentence



def render_trainModel():
    
    st.markdown("""
    <header>
        <h1>Select the Model attributes</h1>
    </header>
    """, unsafe_allow_html=True)


    add_selectbox = st.selectbox(
        "Emoji MASK?",
        ("Yes", "No")
    )

    add_radio = st.radio(
        "Vocabulary size",
        ("1000", 
        "3000",
        "5000",
        "10000")
    )


    color = st.slider(
        label='Vocabulary size',
        min_value=1000,
        max_value=10000,
        step=2000
        )
    
def render_pretrainedModel():

    user_input = st.text_input("", "I love this product!")

    loaded_model = tf.keras.models.load_model('models/2T/model2T_15e')
    with open('models/2T/model2T_15e/training_history.obj', 'rb') as f:
        loaded_history = pickle.load(f)

    if user_input:
        st.write("**Input Text:** "+user_input)

        if st.checkbox("Show Plot"):
            pass

    if st.button("Analyze Sentiment"):

        threshold = 0.5
        sentence_emojiMask = emojiMask(user_input)
        clean_sentence = str(cleanSentence(sentence_emojiMask))
        tf_clean_sentence = tf.constant([clean_sentence])
        prediction = loaded_model(tf_clean_sentence)
        binary_prediction = 1 if prediction.numpy()[0][0] > threshold else 0
        st.write(f'{binary_prediction}')

        # prediction = model.predict([user_input])[0][0]
        # sentiment = "Positive" if prediction > 0.5 else "Negative"
        # st.write(f"Prediction: {sentiment} ({prediction:.2f})")