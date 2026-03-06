import streamlit as st
from utils.auth import login

st.set_page_config(
    page_title="Analyse RFC / Livraisons",
    layout="wide"
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


if st.sidebar.button("Déconnexion"):
    st.session_state.authenticated = False
    st.rerun()

# Page login
if not st.session_state.authenticated:
    login()
    st.stop()

# Application principale
st.sidebar.success("Utilisateur connecté")

st.title("Analyse des adhérences RFC / Livraisons")

st.write("Utilisez le menu à gauche pour naviguer dans l'application.")
