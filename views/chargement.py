import streamlit as st
import pandas as pd
from utils.clean import filter_split_and_reorder

def show():
    st.title("Chargement des données")

    file = st.file_uploader("Importer fichier CSV ou Excel", type=["csv","xlsx"])
    if file:

        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        df = filter_split_and_reorder(df)

        st.session_state.df = df

        st.success("Données chargées")

        st.dataframe(df)
