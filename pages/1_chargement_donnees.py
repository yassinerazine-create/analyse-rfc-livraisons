import streamlit as st
from utils.loader import load_file

st.title("Chargement de données")

file = st.file_uploader("Importer fichier", type=["xlsx","csv"])

if file:

    df = load_file(file)

    st.session_state["data"] = df

    st.success("Données chargées")

    st.dataframe(df)

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Changements", df["RFC"].nunique())
    col2.metric("Composants", df["Composant_Version"].nunique())
    col3.metric("Livraisons", df["Label Livraison affecté"].nunique())
    col4.metric("UMEP", df["UMEP"].nunique())
