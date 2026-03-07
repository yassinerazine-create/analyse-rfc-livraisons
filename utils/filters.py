import streamlit as st
import pandas as pd
from utils.versioning import version_to_tuple

def filter_by_week(df):
    df = df.copy()

    # Semaine cible déjà convertie en int dans clean.py
    weeks = sorted(df["Semaine cible"].dropna().astype(int).unique())

    if not weeks:
        st.warning("⚠️ Aucune semaine valide dans les données")
        return df


    selected_weeks = st.multiselect(
    "Choisir semaine(s)",
    sorted(df["Semaine cible"].dropna().unique()),
    default=sorted(df["Semaine cible"].dropna().unique()),
    placeholder="Sélectionner une ou plusieurs semaine"
)


    return df[df["Semaine cible"].isin(selected_weeks)]


def keep_highest_version_per_rfc_composant(df):
    """
    Pour chaque RFC + Composant, garder seulement la ligne avec la version la plus haute
    """
    df = df.copy()
    df["v_tuple"] = df["Version"].apply(version_to_tuple)

    # garder la ligne avec la version max pour chaque RFC+Composant
    df_max = df.loc[df.groupby(["RFC", "Composant"])["v_tuple"].idxmax()]

    # supprimer colonne temporaire
    df_max = df_max.drop(columns=["v_tuple"])

    return df_max
