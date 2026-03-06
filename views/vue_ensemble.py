import streamlit as st
import plotly.express as px
from utils.clean import filter_split_and_reorder

def show():
    st.title("Vue d'ensemble")
    st.dataframe(df)
    if "data" not in st.session_state:
        st.warning("Veuillez charger les données")
        return

    df = st.session_state.data.copy()
    df = filter_split_and_reorder(df)

    fig = px.histogram(df, x="Label Livraison affecté", title="Composants par livraison")
    st.plotly_chart(fig, use_container_width=True)
