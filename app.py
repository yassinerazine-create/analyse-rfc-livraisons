import streamlit as st
from views import (
    chargement,
    dashboard,
    vue_ensemble,
    livraisons,
    rfc,
    composants,
    umep,
    incoherences
)
from style import apply_style

st.set_page_config(
    page_title="Analyse RFC Livraisons",
    page_icon="📦",
    layout="wide"
)

apply_style()

st.sidebar.title("📦 Analyse RFC")
menu = st.sidebar.radio(
    "Navigation",
    ["Chargement", "Dashboard", "Vue d'ensemble", "Livraisons", "RFC", "Composants", "UMEP", "Incohérences"]
)

if menu == "Chargement":
    chargement.show()
else:
    if "df" not in st.session_state:
        st.warning("Veuillez charger un fichier")
        st.stop()

    df = st.session_state.df

    if menu == "Dashboard":
        dashboard.show(df)
    if menu == "Vue d'ensemble":
        vue_ensemble.show(df)
    if menu == "Livraisons":
        livraisons.show(df)
    if menu == "RFC":
        rfc.show(df)
    if menu == "Composants":
        composants.show(df)
    if menu == "UMEP":
        umep.show(df)
    if menu == "Incohérences":
        incoherences.show(df)
