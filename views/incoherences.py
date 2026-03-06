import streamlit as st
from utils.clean import filter_split_and_reorder


def show():
    st.title("Détection d'incohérences")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    #df = st.session_state.data
    df = st.session_state.data.copy()
    df = filter_split_and_reorder(df)
    result = df.groupby("Composant_Version")["RFC"].nunique().reset_index()
    result = result[result["RFC"] > 1]
    st.dataframe(result)
