import streamlit as st

st.title("Vue par livraison")

df = st.session_state.data

livraison = st.selectbox(
    "Choisir livraison",
    df["Label Livraison affecté"].unique()
)

filtered = df[df["Label Livraison affecté"] == livraison]

st.dataframe(filtered)
