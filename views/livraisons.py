import streamlit as st
from utils.filters import filter_by_week


def show(df):

    st.title("Vue par livraison")

    df = filter_by_week(df)

    livraisons = st.multiselect(
        "Choisir livraison(s)",
        sorted(df["Label"].dropna().unique()),
        default=sorted(df["Label"].dropna().unique())
    )

    df_filtered = df[df["Label"].isin(livraisons)]

    st.write("Nombre de lignes :", len(df_filtered))

    st.dataframe(df_filtered, use_container_width=True)
