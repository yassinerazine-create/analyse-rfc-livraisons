import streamlit as st

# imports des modules
import views.chargement as chargement
import views.incoherences as incoherences
import views.vue_ensemble as vue_ensemble
import views.livraisons as livraisons
import views.rfc as rfc
import views.composants as composants
import views.umep as umep

from utils.auth import login


# configuration de la page
st.set_page_config(
    page_title="Analyse RFC / Livraisons",
    layout="wide"
)


# initialisation session
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


# ==========================
# AUTHENTIFICATION
# ==========================

if not st.session_state.authenticated:
    login()
    st.stop()


# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Choisir une vue",
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


# bouton logout
if st.sidebar.button("Déconnexion"):
    st.session_state.authenticated = False
    st.rerun()


st.sidebar.success(f"Connecté : {st.session_state.user}")


# ==========================
# ROUTER DES PAGES
# ==========================

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
