import streamlit as st
import pandas as pd
from utils.clean import filter_split_and_reorder

def show():
    st.title("Chargement des données")

    uploaded_file = st.file_uploader("Charger un fichier CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = filter_split_and_reorder(df)
        st.success("Données chargées avec succès !")
        st.dataframe(df, use_container_width=True)
        return df
    return None
