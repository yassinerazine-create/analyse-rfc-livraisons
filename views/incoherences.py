import streamlit as st
import pandas as pd
from utils.incoherence_detection import detect_version_incoherence

def show(df):
    st.title("Incohérences - Versions / Semaines")

    # ajouter RFC et Label si manquants
    for col in ["RFC", "Label"]:
        if col not in df.columns:
            df[col] = ""

    # détecte incohérences avec version max précédente
    inco = detect_version_incoherence(df)

    if inco.empty:
        st.success("Aucune incohérence détectée")
        return

    # transformer semaine pour afficher juste le nombre entier
    if "Semaine concernée" in inco.columns:
        inco["Semaine concernée"] = inco["Semaine concernée"].apply(lambda x: int(float(x)))

    # flèches et couleurs pour versions
    def style_versions(row):
        max_week = f"⬆ {row['Version max semaine']}"
        max_prev = f"⬇ {row['Version max précédente']} (RFC: {row['RFC précédente']}, Label: {row['Label précédente']}, Semaine: {row['Semaine précédente']})"
        return pd.Series([max_week, max_prev])

    # ajouter info RFC/Label/Semaine de version max précédente
    for col in ["RFC précédente", "Label précédente", "Semaine précédente"]:
        if col not in inco.columns:
            inco[col] = ""

    styled = inco.copy()
    styled[["Version max semaine", "Version max précédente"]] = styled.apply(style_versions, axis=1)

    # colonnes finales
    desired_cols = [
        "Composant", "Semaine concernée",
        "Version max semaine", "Version max précédente"
    ]
    cols = [c for c in desired_cols if c in styled.columns]
    styled = styled[cols]

    # couleurs conditionnelles
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
