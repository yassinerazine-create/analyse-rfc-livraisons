import streamlit as st
import pandas as pd


def filter_by_week(df):

    df = df.copy()

    # conversion en numérique, ignorer les valeurs non convertibles
    df["Semaine cible"] = pd.to_numeric(df["Semaine cible"], errors="coerce")

    # garder uniquement les semaines valides
    weeks = sorted(df["Semaine cible"].dropna().astype(int).unique())

    if not weeks:
        st.warning("⚠️ Aucune semaine valide dans les données")
        return df

    selected_weeks = st.multiselect(
        "Filtrer par semaine cible",
        weeks,
        default=weeks
    )

    return df[df["Semaine cible"].isin(selected_weeks)]
