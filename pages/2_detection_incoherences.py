import streamlit as st
from utils.analytics import composants_multi_rfc

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Veuillez vous connecter.")
    st.stop()

st.title("Détection d'incohérences")

if "data" not in st.session_state:
    st.warning("Veuillez charger les données")
    st.stop()

df = st.session_state.data

st.subheader("Composants présents dans plusieurs RFC")

result = composants_multi_rfc(df)

st.dataframe(result)
