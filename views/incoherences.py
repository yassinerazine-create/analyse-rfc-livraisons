import streamlit as st
import pandas as pd
from utils.incoherence_detection import detect_version_incoherence

def show(df):
    st.title("Incohérences - Versions / Semaines")

    # ajouter RFC et Label si manquants
    for col in ["RFC", "Label"]:
        if col not in df.columns:
            df[col] = ""

    # détecte incohérences avec la nouvelle logique
    inco = detect_version_incoherence(df)

    if inco.empty:
        st.success("Aucune incohérence détectée")
        return

    # ajouter flèches pour version max semaine vs max précédente
    def style_versions(row):
        max_week = f"⬆ {row['Version max semaine']}"  # version max semaine
        max_prev = f"⬇ {row['Version max précédente']}"  # version max précédente
        return pd.Series([max_week, max_prev])

    styled = inco.copy()
    styled[["Version max semaine", "Version max précédente"]] = styled.apply(style_versions, axis=1)

    # colonnes finales existantes
    desired_cols = [
        "Composant", "Semaine concernée", "RFC", "Label",
        "Version max semaine", "Version max précédente"
    ]
    cols = [c for c in desired_cols if c in styled.columns]
    styled = styled[cols]

    # appliquer couleurs conditionnelles
    def color_cells(val):
        if isinstance(val, str):
            if val.startswith("⬆"):
                return 'color: green; font-weight:bold'
            elif val.startswith("⬇"):
                return 'color: red; font-weight:bold'
        return ''

    st.dataframe(
        styled.style.applymap(color_cells, subset=["Version max semaine", "Version max précédente"]),
        use_container_width=True
    )
