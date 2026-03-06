import streamlit as st

st.title("Vue par UMEP")

df = st.session_state.data

umep = st.selectbox("Choisir UMEP", df["UMEP"].unique())

filtered = df[df["UMEP"] == umep]

st.dataframe(filtered)
