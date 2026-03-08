import streamlit as st
import pandas as pd
from utils.incoherence_detection import detect_version_incoherence

def show(df):
    st.title("Incohérences")

    # assure que RFC et Label existent dans le DataFrame
    for col in ["RFC", "Label"]:
        if col not in df.columns:
            df[col] = ""

    inco = detect_version_incoherence(df)

    if inco.empty:
        st.success("Aucune incohérence détectée")
        return

    # Ajouter flèches ↑↓ et couleur
    def style_versions(row):
        sup = f"⬆ {row['Version supérieure']}"
        inf = f"⬇ {row['Version inférieure']}"
        return pd.Series([sup, inf])

    styled = inco.copy()
    styled[["Version supérieure", "Version inférieure"]] = styled.apply(style_versions, axis=1)

    # colonnes finales (ne garder que celles existantes)
    desired_cols = [
        "Composant", "RFC", "Label",
        "Version supérieure", "Semaine supérieure",
        "Version inférieure", "Semaine inférieure"
    ]
    cols = [c for c in desired_cols if c in styled.columns]  # <- seulement celles présentes
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
        styled.style.applymap(color_cells, subset=["Version supérieure", "Version inférieure"]),
        use_container_width=True
    )
