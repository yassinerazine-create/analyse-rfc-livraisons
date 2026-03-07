import streamlit as st

def apply_style():

    st.markdown("""
    <style>

    /* Fond principal */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1f2937;
        color: white;
    }

    section[data-testid="stSidebar"] h1 {
        color: white;
    }

    /* Boutons radio navigation */
    .stRadio label {
        font-weight: 600;
    }

    /* Multiselect */
    div[data-baseweb="select"] {
        background-color: white;
        border-radius: 8px;
    }

    /* Tables */
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
        border: 1px solid #e5e7eb;
    }

    /* Titres */
    h1, h2, h3 {
        color: #1f2937;
    }

    /* Alertes */
    .stAlert {
        border-radius: 8px;
    }

    </style>
    """, unsafe_allow_html=True)
