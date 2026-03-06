import streamlit as st

st.title("Vue par RFC")

df = st.session_state.data

rfc = st.selectbox("Choisir RFC", df["RFC"].unique())

filtered = df[df["RFC"] == rfc]

st.dataframe(filtered)
