import streamlit as st
import pandas as pd


def filter_by_week(df):

    df = df.copy()

    # conversion sécurisée
    df["Semaine cible"] = pd.to_numeric(
        df["Semaine cible"],
        errors="coerce"
    )

    weeks = sorted(df["Semaine cible"].dropna().unique())

    selected_weeks = st.multiselect(
        "Filtrer par semaine cible",
        weeks,
        default=weeks
    )

    return df[df["Semaine cible"].isin(selected_weeks)]
