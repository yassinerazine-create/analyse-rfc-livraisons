import streamlit as st

# import des pages
from views import (
    chargement,
    vue_ensemble,
    livraisons,
    rfc,
    composants,
    incoherences,
    umep
)

st.set_page_config(page_title="Analyse RFC / Livraisons", layout="wide")

# -------------------------
# SESSION
# -------------------------
if "df" not in st.session_state:
    st.session_state.df = None

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Aller à :",
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

# -------------------------
# ROUTER
# -------------------------
df = st.session_state.df

if page == "Chargement des données":
    df = chargement.show()
    st.session_state.df = df
elif page == "Vue d'ensemble":
    if df is not None:
        vue_ensemble.show(df)
elif page == "Livraisons":
    if df is not None:
        livraisons.show(df)
elif page == "RFC":
    if df is not None:
        rfc.show(df)
elif page == "Composants":
    if df is not None:
        composants.show(df)
elif page == "Incohérences":
    if df is not None:
        incoherences.show(df)
elif page == "UMEP":
    if df is not None:
        umep.show(df)
