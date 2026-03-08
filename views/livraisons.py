import streamlit as st
from utils.filters import filter_by_week, keep_highest_version_per_rfc_composant

def show(df):
    st.title("Livraisons")
    df = filter_by_week(df)
    df = keep_highest_version_per_rfc_composant(df)
    choix = st.multiselect("Choisir livraison", sorted(df["Label"].unique()))
    if choix:
        df = df[df["Label"].isin(choix)]
    st.dataframe(df,use_container_width=True)

