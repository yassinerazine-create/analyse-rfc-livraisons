import streamlit as st
import pandas as pd
from utils.clean import filter_split_and_reorder

def show():
    st.title("Chargement des données")

    uploaded_file = st.file_uploader("Charger un fichier CSV ou Excel", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            # détecter le type de fichier
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Format de fichier non supporté")
                return None

            # filtrer, splitter et réordonner
            df = filter_split_and_reorder(df)

            st.success(f"Données chargées avec succès : {df.shape[0]} lignes")
            st.dataframe(df, use_container_width=True)

            return df
        except Exception as e:
            st.error(f"Erreur lors du chargement du fichier : {e}")
            return None

    return None
