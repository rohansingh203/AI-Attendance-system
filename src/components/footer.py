import streamlit as st


def footer_home():

    logo_url = ""

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
                <p style="font-wight:bold; color:white;"> Created with ❤️ </p>
                <img src='{logo_url}' style='mas-height:25px' />
        </div>

                """, unsafe_allow_html=True)