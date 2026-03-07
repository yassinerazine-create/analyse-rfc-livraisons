import streamlit as st
from utils.filters import filter_by_week

def show(df):

    st.title("Composants")

    df = filter_by_week(df)

    c = st.multiselect(
        "Composant",
        sorted(df["Composant"].unique())
    )

    if c:

        df = df[df["Composant"].isin(c)]

    st.dataframe(df,use_container_width=True)
