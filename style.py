import streamlit as st

def apply_style():
    st.markdown("""
    <style>
    .stApp { background-color: #f5f7fb; }
    section[data-testid="stSidebar"] { background-color: #111827; color: white; }
    h1, h2, h3 { color: #1f2937; }
    div[data-baseweb="select"] { border-radius: 8px; }
    .stDataFrame { border-radius: 10px; border: 1px solid #e5e7eb; }
    </style>
    """, unsafe_allow_html=True)
