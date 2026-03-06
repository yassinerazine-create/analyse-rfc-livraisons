import streamlit as st
import pandas as pd

def show():
    st.title("Chargement des données")

    file = st.file_uploader("Importer fichier", type=["csv","xlsx"])
    if file:
        if file.name.endswith("csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.session_state["data"] = df
        st.success("Données chargées")
        st.dataframe(df)
