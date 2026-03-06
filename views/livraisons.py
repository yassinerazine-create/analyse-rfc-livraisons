import streamlit as st
from utils.clean import filter_split_and_reorder


def show():
    st.title("Vue par livraison")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    #df = st.session_state.data
    df = st.session_state.data.copy()
    df = filter_split_and_reorder(df)
    livraison = st.selectbox("Choisir livraison", df["Label Livraison affecté"].unique())
    st.dataframe(df[df["Label Livraison affecté"] == livraison])
