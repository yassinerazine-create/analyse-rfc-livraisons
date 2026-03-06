import streamlit as st


if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Veuillez vous connecter.")
    st.stop()

    
st.title("Vue par livraison")

df = st.session_state.data

livraison = st.selectbox(
    "Choisir livraison",
    df["Label Livraison affecté"].unique()
)

filtered = df[df["Label Livraison affecté"] == livraison]

st.dataframe(filtered)
