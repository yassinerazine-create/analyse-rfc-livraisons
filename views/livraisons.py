import streamlit as st

def show():
    st.title("Vue par livraison")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    df = st.session_state.data
    livraison = st.selectbox("Choisir livraison", df["Label Livraison affecté"].unique())
    st.dataframe(df[df["Label Livraison affecté"] == livraison])
