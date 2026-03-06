import streamlit as st
import pandas as pd

st.title("Chargement des données")

file = st.file_uploader("Importer fichier", type=["xlsx","csv"])

if file:

    if file.name.endswith("csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.session_state["data"] = df

    st.success("Données chargées")

    st.dataframe(df.head())
