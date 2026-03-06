import streamlit as st
import pandas as pd

def filter_by_week(df):
    df = df.copy()

    # Semaine cible déjà convertie en int dans clean.py
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
