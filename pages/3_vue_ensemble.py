import streamlit as st
import plotly.express as px

st.title("Vue d'ensemble")

df = st.session_state.data

fig = px.histogram(
    df,
    x="Label Livraison affecté",
    title="Composants par livraison"
)

st.plotly_chart(fig, use_container_width=True)
