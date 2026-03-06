import streamlit as st


if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Veuillez vous connecter.")
    st.stop()

    
st.title("Vue par composant")

df = st.session_state.data

comp = st.selectbox(
    "Choisir composant",
    df["Composant_Version"].unique()
)

filtered = df[df["Composant_Version"] == comp]

st.dataframe(filtered)
