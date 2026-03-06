import streamlit as st
from utils.clean import filter_split_and_reorder


def show():
    st.title("Vue par composant")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    #df = st.session_state.data
    df = st.session_state.data.copy()
    df = filter_split_and_reorder(df)
    #comp = st.selectbox("Choisir composant", df["Composant"].unique())
    #st.dataframe(df[df["Composant"] == comp])
    composants = st.multiselect("Choisir Composants(s)", df["Composant"].unique(), default=df["Composant"].unique())
    st.dataframe(df[df["Composant"].isin(composants)])

