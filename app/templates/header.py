import streamlit as st

def render_header():
    
    
    st.markdown("""
    <header style="text-align: center;">
        <h1>Comment Analyzer</h1>
    </header>
    """, unsafe_allow_html=True)

    st.write("")  # add vertical space
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.link_button("Open in github", "https://github.com/haarrublar/XAnalizer")

    with col2:
        st.link_button("Visit my website", "https://haarrublar.com")

    with col3:
        st.link_button("email me", "mailto:harrubla.96@gmail.com")

    
    st.markdown("""
    <hr/>
    """, unsafe_allow_html=True)
    
    
