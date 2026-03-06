import streamlit as st

# imports des pages
import views.chargement as chargement
import views.vue_ensemble as vue_ensemble
import views.livraisons as livraisons
import views.rfc as rfc
import views.composants as composants
import views.incoherences as incoherences
import views.umep as umep

# -------------------------
# CONFIG PAGE
# -------------------------
st.set_page_config(page_title="Analyse RFC / Livraisons", layout="wide")

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choisir une vue",
    [
        "Chargement des données",
        "Vue d'ensemble",
        "Livraisons",
        "RFC",
        "Composants",
        "Incohérences",
        "UMEP"
    ]
)

# Vérifier si les données sont chargées
if page != "Chargement des données":
    if "df" not in st.session_state:
        st.warning("Veuillez charger les données dans l'onglet 'Chargement des données'")
        st.stop()



# -------------------------
# ROUTER DES PAGES
# -------------------------
if page == "Chargement des données":
    chargement.show()

elif page == "Vue d'ensemble":
    vue_ensemble.show(st.session_state.df)

elif page == "Livraisons":
    livraisons.show(st.session_state.df)

elif page == "RFC":
    rfc.show(st.session_state.df)

elif page == "Composants":
    composants.show(st.session_state.df)

elif page == "Incohérences":
    incoherences.show(st.session_state.df)

elif page == "UMEP":
    umep.show(st.session_state.df)

