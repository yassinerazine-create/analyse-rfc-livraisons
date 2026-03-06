import streamlit as st

def show():
    st.title("Vue par RFC")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    df = st.session_state.data
    rfc = st.selectbox("Choisir RFC", df["RFC"].unique())
    st.dataframe(df[df["RFC"] == rfc])
