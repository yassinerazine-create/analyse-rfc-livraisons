import streamlit as st
from utils.clean import filter_split_and_reorder


def show():
    st.title("Vue par RFC")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    #df = st.session_state.data
    df = st.session_state.data.copy()
    df = filter_split_and_reorder(df)
    rfc = st.selectbox("Choisir RFC", df["RFC"].unique())
    st.dataframe(df[df["RFC"] == rfc])
