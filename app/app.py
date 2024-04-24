import streamlit as st



st.info("🎈 **NEW:** Add your own code template to this site! [Guide](https://github.com/jrieke/traingenerator#adding-new-templates)")


st.markdown("<br>", unsafe_allow_html=True)
"""Jumpstart your machine learning code:

1. Specify model in the sidebar *(click on **>** if closed)*
2. Training code will be generated below
3. Download and do magic! :sparkles:

---
"""

st.write("")  # add vertical space
col1, col2, col3 = st.columns(3)
open_colab = col1.button("🚀 Open in Colab")  # logic handled further down
open_colab2 = col2.button("🚀 Open in Cola")  # logic handled further down
open_colab3 = col3.button("🚀 Open in Col")  # logic handled further down
