import streamlit as st


def filter_by_week(df):

    weeks = sorted(df["Semaine cible"].unique())

    selected = st.multiselect(
        "Filtrer semaine cible",
        weeks,
        default=weeks
    )

    return df[df["Semaine cible"].isin(selected)]
