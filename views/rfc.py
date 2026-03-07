import streamlit as st
from utils.filters import filter_by_week

def show(df):

    st.title("RFC")

    df = filter_by_week(df)

    r = st.multiselect(
        "RFC",
        sorted(df["RFC"].unique())
    )

    if r:

        df = df[df["RFC"].isin(r)]

    st.dataframe(df,use_container_width=True)
