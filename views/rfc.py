import streamlit as st
from utils.filters import filter_by_week


def show(df):

    st.title("Vue par RFC")

    df = filter_by_week(df)

    rfcs = st.multiselect(
        "Choisir RFC(s)",
        sorted(df["RFC"].dropna().unique()),
        default=sorted(df["RFC"].dropna().unique())
    )

    df_filtered = df[df["RFC"].isin(rfcs)]

    st.write("Nombre de lignes :", len(df_filtered))

    st.dataframe(df_filtered, use_container_width=True)
