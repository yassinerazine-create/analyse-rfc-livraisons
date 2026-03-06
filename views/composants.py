import streamlit as st
from utils.filters import filter_by_week


def show(df):

    st.title("Vue par composant")

    df = filter_by_week(df)

    composants = st.multiselect(
        "Choisir composant(s)",
        sorted(df["Composant"].dropna().unique()),
        default=sorted(df["Composant"].dropna().unique())
    )

    df_filtered = df[df["Composant"].isin(composants)]

    st.write("Nombre de lignes :", len(df_filtered))

    st.dataframe(df_filtered, use_container_width=True)
