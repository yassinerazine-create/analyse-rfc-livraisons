import streamlit as st


if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Veuillez vous connecter.")
    st.stop()

    
st.title("Vue par UMEP")

df = st.session_state.data

umep = st.selectbox("Choisir UMEP", df["UMEP"].unique())

filtered = df[df["UMEP"] == umep]

st.dataframe(filtered)
