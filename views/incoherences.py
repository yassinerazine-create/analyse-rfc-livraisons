import streamlit as st
import pandas as pd
from utils.incoherence_detection import detect_version_incoherence

def show(df):
    st.title("Incohérences - Versions / Semaines")

    # Split composant/version si besoin
    if "Composant_Version" in df.columns:
        from utils.split import split_composant_version
        df[["Composant", "Version"]] = df["Composant_Version"].apply(split_composant_version)

    # Ajouter RFC et Label si manquants
    for col in ["RFC", "Label"]:
        if col not in df.columns:
            df[col] = ""

    # Détecte incohérences
    inco = detect_version_incoherence(df)

    if inco.empty:
        st.success("Aucune incohérence détectée")
        return

    # transformer semaine pour afficher entier
    if "Semaine concernée" in inco.columns:
        inco["Semaine concernée"] = inco["Semaine concernée"].apply(lambda x: int(float(x)))

    # Ajouter info RFC/Label/Semaine précédente si manquante
    for col in ["RFC précédente", "Label précédente", "Semaine précédente"]:
        if col not in inco.columns:
            inco[col] = ""

    # Créer Version max précédente formatée
    def style_versions(row):
        max_week = f"⬆ {row['Version max semaine']}"
        max_prev = f"⬇ {row['Version max précédente']} (RFC:{row['RFC précédente']}, {row['Label précédente']}, S{row['Semaine précédente']})"
        return pd.Series([max_week, max_prev])

    styled = inco.copy()
    styled[["Version max semaine", "Version max précédente"]] = styled.apply(style_versions, axis=1)

    # Colonnes finales
    desired_cols = [
        "Composant", "Semaine concernée", "RFC",
        "Version max semaine", "Version max précédente"
    ]
    cols = [c for c in desired_cols if c in styled.columns]
    styled = styled[cols]

    # Couleurs conditionnelles
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
