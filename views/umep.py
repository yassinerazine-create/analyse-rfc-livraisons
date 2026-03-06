import streamlit as st
from utils.clean import filter_split_and_reorder


def show():
    st.title("Vue par UMEP")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    #df = st.session_state.data
    df = st.session_state.data.copy()
    df = filter_split_and_reorder(df)
    #umep = st.selectbox("Choisir UMEP", df["UMEP"].unique())
    #st.dataframe(df[df["UMEP"] == umep])
    umeps = st.multiselect("Choisir UMEP(s)", df["UMEP"].unique(), default=df["UMEP"].unique())
    st.dataframe(df[df["UMEP"].isin(umeps)])

