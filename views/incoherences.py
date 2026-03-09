import streamlit as st
import pandas as pd
from utils.incoherence_detection import detect_version_incoherence
from utils.split import split_composant_version

def show(df):

    st.title("Incohérences - Versions / Semaines")

    # -------------------------
    # Split composant/version
    # -------------------------
    if "Composant_Version" in df.columns:
        df[["Composant", "Version"]] = df["Composant_Version"].apply(split_composant_version)

    # sécuriser colonnes
    for col in ["RFC", "Label", "Semaine cible"]:
        if col not in df.columns:
            df[col] = None

    # -------------------------
    # Détection incohérences
    # -------------------------
    inco = detect_version_incoherence(df)

    if inco.empty:
        st.success("Aucune incohérence détectée")
        return

    # -------------------------
    # Conversion robuste semaine
    # -------------------------
    if "Semaine concernée" in inco.columns:

        inco["Semaine concernée"] = (
            pd.to_numeric(inco["Semaine concernée"], errors="coerce")
            .fillna(0)
            .astype(int)
        )

    # -------------------------
    # Colonnes précédentes sécurisées
    # -------------------------
    for col in ["RFC précédente", "Label précédente", "Semaine précédente"]:
        if col not in inco.columns:
            inco[col] = ""

    # -------------------------
    # Formatage versions
    # -------------------------
    def format_max(row):
        return f"⬆ {row['Version max semaine']}"

    def format_prev(row):

        week = row["Semaine précédente"]
        if pd.notna(week):
            week = f"S{int(week)}"
        else:
            week = ""

        return (
            f"⬇ {row['Version max précédente']} "
            f"(RFC:{row['RFC précédente']}, {row['Label précédente']}, {week})"
        )

    inco["Version max semaine"] = inco.apply(format_max, axis=1)
    inco["Version max précédente"] = inco.apply(format_prev, axis=1)

    # -------------------------
    # Colonnes affichées
    # -------------------------
    display_cols = [
        "Composant",
        "Semaine concernée",
        "RFC",
        "Version max semaine",
        "Version max précédente",
    ]

    display_cols = [c for c in display_cols if c in inco.columns]

    styled = inco[display_cols]

    # -------------------------
    # Couleurs
    # -------------------------
    def color_versions(val):

        if isinstance(val, str):

            if val.startswith("⬆"):
                return "color: green; font-weight:bold"

            if val.startswith("⬇"):
                return "color: red; font-weight:bold"

        return ""

    st.dataframe(
        styled.style.applymap(
            color_versions,
            subset=["Version max semaine", "Version max précédente"],
        ),
        use_container_width=True,
    )
