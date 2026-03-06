import streamlit as st
import plotly.express as px


if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("Veuillez vous connecter.")
    st.stop()

    
st.title("Vue d'ensemble")

df = st.session_state.data

fig = px.histogram(
    df,
    x="Label Livraison affecté",
    title="Composants par livraison"
)

st.plotly_chart(fig, use_container_width=True)
