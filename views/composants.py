import streamlit as st
from utils.filters import filter_by_week

def show(df):
    st.title("Composants")
    df = filter_by_week(df)
    choix = st.multiselect("Composant", sorted(df["Composant"].unique()))
    if choix:
        df = df[df["Composant"].isin(choix)]
    st.dataframe(df,use_container_width=True)
