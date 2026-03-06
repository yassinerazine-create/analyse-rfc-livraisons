import streamlit as st
import plotly.express as px

def show():
    st.title("Vue d'ensemble")
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    df = st.session_state.data
    fig = px.histogram(df, x="Label Livraison affecté", title="Composants par livraison")
    st.plotly_chart(fig, use_container_width=True)
