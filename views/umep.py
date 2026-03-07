import streamlit as st
from utils.filters import filter_by_week

def show(df):

    st.title("UMEP")

    df = filter_by_week(df)

    u = st.multiselect(
        "UMEP",
        sorted(df["UMEP"].unique())
    )

    if u:

        df = df[df["UMEP"].isin(u)]

    st.dataframe(df,use_container_width=True)
