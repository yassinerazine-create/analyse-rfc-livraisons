import streamlit as st
from utils.filters import filter_by_week


def show(df):

    st.title("Vue d'ensemble")

    df = filter_by_week(df)

    st.write("Nombre de lignes :", len(df))

    st.dataframe(df, use_container_width=True)
