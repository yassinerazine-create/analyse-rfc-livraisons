import streamlit as st
from utils.auth import login

st.set_page_config(
    page_title="Analyse RFC / Livraisons",
    layout="wide"
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login()
    st.stop()

st.sidebar.success("Utilisateur connecté")

st.title("Analyse des adhérences RFC / Livraisons")

st.markdown("""
Application permettant d'analyser les dépendances entre :

- RFC
- Composants
- Livraisons
- UMEP
""")
