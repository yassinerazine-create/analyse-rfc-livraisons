import streamlit as st

st.title("Vue par composant")

df = st.session_state.data

comp = st.selectbox(
    "Choisir composant",
    df["Composant_Version"].unique()
)

filtered = df[df["Composant_Version"] == comp]

st.dataframe(filtered)
