import streamlit as st
import views
import style

st.set_page_config(
    page_title="Analyse RFC Livraisons",
    page_icon="📦",
    layout="wide"
)

style.apply_style()

st.sidebar.title("📦 Analyse RFC")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Chargement",
        "Vue d'ensemble",
        "Livraisons",
        "RFC",
        "Composants",
        "UMEP",
        "Incohérences"
    ]
)

if menu == "Chargement":
    views.chargement.show()

else:

    if "df" not in st.session_state:
        st.warning("Veuillez charger un fichier")
        st.stop()

    df = st.session_state.df

    if menu == "Vue d'ensemble":
        views.vue_ensemble.show(df)

    if menu == "Livraisons":
        views.livraisons.show(df)

    if menu == "RFC":
        views.rfc.show(df)

    if menu == "Composants":
        views.composants.show(df)

    if menu == "UMEP":
        views.umep.show(df)

    if menu == "Incohérences":
        views.incoherences.show(df)
