import streamlit as st

def render_steps():
    
    multi = '''
    ### Tips for using the model:
    - Try different sentences related to various topics such as education, health, hobbies, etc.
    - The model achieves its highest accuracy when the sentiment of each sentence is clearly indicated as positive or negative.
    - The model accepts emojis during training. The pretrained model uses the emoji [MASK]. For a different approach, set up the model yourself in the "Train Model" section.
    - The model was trained over small length sentences, so you will have more accuracy. So use around 110 to 160 characters by sentence.
    '''
    st.markdown(multi)

    
    
