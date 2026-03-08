import streamlit as st
import pandas as pd
from utils.clean import filter_split_and_reorder

def show():
    st.title("Chargement des données")
    uploaded_file = st.file_uploader("Choisir un fichier CSV ou Excel", type=["csv","xlsx"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        df = filter_split_and_reorder(df)
        st.session_state.df = df
        st.success("Fichier chargé avec succès")
        st.dataframe(df,use_container_width=True)
