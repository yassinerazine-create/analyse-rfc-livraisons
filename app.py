import streamlit as st
from utils.auth import login
from views import chargement, incoherences, vue_ensemble, livraisons, rfc, composants, umep

st.set_page_config(
    page_title="Analyse RFC / Livraisons",
    layout="wide"
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


# LOGIN
if not st.session_state.authenticated:
    login()
    st.stop()


# MENU
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Choisir une page",
    [
        "Chargement des données",
        "Détection incohérences",
        "Vue d'ensemble",
        "Vue livraisons",
        "Vue RFC",
        "Vue composants",
        "Vue UMEP"
    ]
)


# LOGOUT
if st.sidebar.button("Déconnexion"):
    st.session_state.authenticated = False
    st.rerun()


# ROUTER
if menu == "Chargement des données":
    chargement.show()

elif menu == "Détection incohérences":
    incoherences.show()

elif menu == "Vue d'ensemble":
    vue_ensemble.show()

elif menu == "Vue livraisons":
    livraisons.show()

elif menu == "Vue RFC":
    rfc.show()

elif menu == "Vue composants":
    composants.show()

elif menu == "Vue UMEP":
    umep.show()
