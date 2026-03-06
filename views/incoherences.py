import streamlit as st
import pandas as pd

def show():
    st.title("Détection des incohérences")

    if "data" not in st.session_state:
        st.warning("Veuillez d'abord charger les données")
        return

    df = st.session_state["data"]

    # exemple de détection : Composant_Version avec plusieurs RFC
    result = df.groupby("Composant_Version")["RFC"].nunique().reset_index()
    result = result[result["RFC"] > 1]

    st.write("Composants présents dans plusieurs RFC :")
    st.dataframe(result)
