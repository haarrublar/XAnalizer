import streamlit as st
import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
template_directory = os.path.join(current_directory, 'templates')
sys.path.append(template_directory)


from header import render_header
from howto import render_steps
from modelView import render_pretrainedModel



# Render the header
render_header()
render_steps()



tab1, tab2= st.tabs(["Pretrained Model", "Train Model"])

with tab1:
    render_pretrainedModel()

    col1, col2 = st.columns(2)
    with col1:
        st.text_input(label='', value='')
    with col2:    
        st.text_input(label='Epoch', value='10')

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)




# st.info("🎈 **NEW:** Add your own code template to this site! [Guide](https://github.com/jrieke/traingenerator#adding-new-templates)")

# Centered text using Markdown and HTML
st.markdown("<div style='text-align: center;'>This text is centered</div>", unsafe_allow_html=True)

# Input field for the user to enter text
user_input = st.text_input(label='', value='')

# Button to submit the input
st.button("Submit")

