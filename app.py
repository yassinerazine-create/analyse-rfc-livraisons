import streamlit as st
from utils.auth import login
from views import 1_chargement_donnees, 2_detection_incoherences, 3_vue_ensemble, 4_vue_livraisons, 5_vue_rfc, 6_vue_composants, 7_vue_umep

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
    1_chargement_donnees.show()

elif menu == "Détection incohérences":
    2_detection_incoherences.show()

elif menu == "Vue d'ensemble":
    3_vue_ensemble.show()

elif menu == "Vue livraisons":
    4_vue_livraisons.show()

elif menu == "Vue RFC":
    5_vue_rfc.show()

elif menu == "Vue composants":
    6_vue_composants.show()

elif menu == "Vue UMEP":
    7_vue_umep.show()
