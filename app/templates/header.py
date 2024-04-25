import streamlit as st

def render_header():
    
    
    st.markdown("""
    <header style="text-align: center;">
        <h1>Comment Analyzer</h1>
    </header>
    """, unsafe_allow_html=True)

    st.write("")  # add vertical space
    col1, col2, col3 = st.columns(3)
    col1.button("🚀 Open in Colab")
    col2.button("🚀 Open in Cola")
    col3.button("🚀 Open in Col")
    
    st.markdown("""
    <hr/>
    """, unsafe_allow_html=True)
    
    
