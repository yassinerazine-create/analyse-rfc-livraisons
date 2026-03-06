import streamlit as st


if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Veuillez vous connecter.")
    st.stop()

    
st.title("Vue par RFC")

df = st.session_state.data

rfc = st.selectbox("Choisir RFC", df["RFC"].unique())

filtered = df[df["RFC"] == rfc]

st.dataframe(filtered)
