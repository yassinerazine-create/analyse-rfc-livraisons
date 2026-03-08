import streamlit as st
import pandas as pd
from utils.incoherence_detection import detect_version_incoherence
from utils.split import split_composant_version

def show(df):
    st.title("Incohérences - Versions / Semaines")

    # -------------------------
    # Split Composant / Version
    # -------------------------
    if "Composant_Version" in df.columns:
        df[["Composant", "Version"]] = df["Composant_Version"].apply(split_composant_version)

    # Ajouter RFC et Label si manquants
    for col in ["RFC", "Label"]:
        if col not in df.columns:
            df[col] = ""

    # -------------------------
    # Détecter incohérences
    # -------------------------
    inco = detect_version_incoherence(df)

    if inco.empty:
        st.success("Aucune incohérence détectée")
        return

    # -------------------------
    # Conversion sécurisée semaine
    # -------------------------
    if "Semaine concernée" in inco.columns:
        def safe_int(x):
            try:
                return int(float(x))
            except (ValueError, TypeError):
                return pd.NA
        inco["Semaine concernée"] = inco["Semaine concernée"].apply(safe_int)

    # Assurer colonnes précédentes
    for col in ["RFC précédente", "Label précédente", "Semaine précédente"]:
        if col not in inco.columns:
            inco[col] = ""

    # -------------------------
    # Créer Version max précédente formatée
    # -------------------------
    def format_prev_version(row):
        return f"⬇ {row['Version max précédente']} (RFC:{row['RFC précédente']}, {row['Label précédente']}, S{row['Semaine précédente']})"

    def format_max_version(row):
        return f"⬆ {row['Version max semaine']}"

    inco["Version max semaine"] = inco.apply(format_max_version, axis=1)
    inco["Version max précédente"] = inco.apply(format_prev_version, axis=1)

    # -------------------------
    # Colonnes finales à afficher
    # -------------------------
    display_cols = [
        "Composant",
        "Semaine concernée",
        "RFC",
        "Version max semaine",
        "Version max précédente"
    ]
    cols = [c for c in display_cols if c in inco.columns]
    styled = inco[cols]

    # -------------------------
    # Style conditionnel
    # -------------------------
    def color_versions(val):
        if isinstance(val, str):
            if val.startswith("⬆"):
                return 'color: green; font-weight:bold'
            elif val.startswith("⬇"):
                return 'color: red; font-weight:bold'
        return ''

    st.dataframe(
        styled.style.applymap(color_versions, subset=["Version max semaine", "Version max précédente"]),
        use_container_width=True
    )
