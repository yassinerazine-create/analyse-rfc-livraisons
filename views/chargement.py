import streamlit as st
import pandas as pd

def show():
    st.title("Chargement des données")

    uploaded_file = st.file_uploader("Importer Excel ou CSV", type=["xlsx", "csv"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.session_state["data"] = df
        st.success(f"Données chargées : {df.shape[0]} lignes, {df.shape[1]} colonnes")
        st.dataframe(df)
