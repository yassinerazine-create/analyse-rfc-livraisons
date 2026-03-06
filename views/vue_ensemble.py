import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.title("Vue d'ensemble")

    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    df = st.session_state["data"]

    col1, col2, col3 = st.columns(3)
    col1.metric("Nombre RFC", df["RFC"].nunique())
    col2.metric("Nombre Composants", df["Composant_Version"].nunique())
    col3.metric("Nombre Livraisons", df["Label Livraison affecté"].nunique())

    # exemple graphique : RFC par mois
    if "Année Mois cible (LAAMM)" in df.columns:
        fig = px.histogram(df, x="Année Mois cible (LAAMM)", color="RFC", title="RFC par mois")
        st.plotly_chart(fig)
