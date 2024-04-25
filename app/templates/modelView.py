import streamlit as st

def render_pretrainedModel():
    
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