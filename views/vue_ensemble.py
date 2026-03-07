import streamlit as st
from utils.filters import filter_by_week,keep_highest_version_per_rfc_composant

def show(df):

    st.title("Vue d'ensemble")

    df = filter_by_week(df)

    df = keep_highest_version_per_rfc_composant(df)

    st.dataframe(df,use_container_width=True)
