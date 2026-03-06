import streamlit as st
from utils.filters import filter_by_week


def show(df):

    st.title("Vue par UMEP")

    df = filter_by_week(df)

    umeps = st.multiselect(
        "Choisir UMEP(s)",
        sorted(df["UMEP"].dropna().unique()),
        default=sorted(df["UMEP"].dropna().unique())
    )

    df_filtered = df[df["UMEP"].isin(umeps)]

    st.write("Nombre de lignes :", len(df_filtered))

    st.dataframe(df_filtered, use_container_width=True)
