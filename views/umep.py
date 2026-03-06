import streamlit as st

def show():
    st.title("Vue par UMEP")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    df = st.session_state.data
    umep = st.selectbox("Choisir UMEP", df["UMEP"].unique())
    st.dataframe(df[df["UMEP"] == umep])
