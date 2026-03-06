import streamlit as st

from views import chargement
from views import vue_ensemble
from views import livraisons
from views import rfc
from views import composants
from views import umep
from views import incoherences

st.set_page_config(page_title="Analyse RFC / Livraisons", layout="wide")

st.title("Analyse RFC / Livraisons")

page = st.sidebar.radio(
    "Navigation",
    [
        "Chargement des données",
        "Vue d'ensemble",
        "Livraisons",
        "RFC",
        "Composants",
        "UMEP",
        "Incohérences"
    ]
)

if page == "Chargement des données":
    chargement.show()

if "df" not in st.session_state and page != "Chargement des données":
    st.warning("Veuillez charger les données")
    st.stop()

df = st.session_state.df

if page == "Vue d'ensemble":
    vue_ensemble.show(df)

elif page == "Livraisons":
    livraisons.show(df)

elif page == "RFC":
    rfc.show(df)

elif page == "Composants":
    composants.show(df)

elif page == "UMEP":
    umep.show(df)

elif page == "Incohérences":
    incoherences.show(df)
