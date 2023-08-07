import streamlit as st

def create_responsive_layout():
    st.set_page_config(layout="wide")

def create_responsive_sidebar():
    st.sidebar.markdown("""
    <style>
    .reportview-container .main .block-container {
        max-width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

def create_responsive_table():
    st.markdown("""
    <style>
    table {
        width:100%;
    }
    </style>
    """, unsafe_allow_html=True)

def apply_responsive_design():
    create_responsive_layout()
    create_responsive_sidebar()
    create_responsive_table()

apply_responsive_design()