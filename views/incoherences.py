import streamlit as st

def show():
    st.title("Détection d'incohérences")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    df = st.session_state.data
    result = df.groupby("Composant_Version")["RFC"].nunique().reset_index()
    result = result[result["RFC"] > 1]
    st.dataframe(result)
