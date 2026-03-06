import streamlit as st

def show():
    st.title("Vue par composant")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    df = st.session_state.data
    comp = st.selectbox("Choisir composant", df["Composant"].unique())
    st.dataframe(df[df["Composant_Version"] == comp])
