import streamlit as st
from utils.incoherence_detection import detect_version_incoherence, detect_same_version_multi_week
from utils.filters import filter_by_week, keep_highest_version_per_rfc_composant

def style_version(row):
    styles = []
    for col in row.index:
        if col == "Version A":
            styles.append("color:red; font-weight:bold")
        elif col == "Version B":
            styles.append("color:green; font-weight:bold")
        else:
            styles.append("")
    return styles

def format_versions_and_weeks(df):
    df = df.copy()
    # convertir semaines en entier
    for col in ["Semaine A", "Semaine B"]:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: int(x) if pd.notna(x) else x)
    # ajouter flèches aux versions
    df["Version A"] = df["Version A"].apply(lambda v: f"⬇ {v}")
    df["Version B"] = df["Version B"].apply(lambda v: f"⬆ {v}")
    return df

def show(df):
    st.title("Détection des incohérences")

    df = filter_by_week(df)
    df = keep_highest_version_per_rfc_composant(df)

    # Tableau 1 : Version / Semaine
    st.subheader("Incohérences Version / Semaine")
    inco = detect_version_incoherence(df)

    if inco.empty:
        st.success("Aucune incohérence détectée")
    else:
        inco = format_versions_and_weeks(inco)
        st.warning(f"{len(inco)} incohérence(s) détectée(s)")
        st.dataframe(inco.style.apply(style_version, axis=1), use_container_width=True)

    # Tableau 2 : Même version sur plusieurs semaines
    st.subheader("Même version planifiée plusieurs semaines")
    dup = detect_same_version_multi_week(df)

    if dup.empty:
        st.success("Aucune duplication")
    else:
        st.warning(f"{len(dup)} ligne(s) concernée(s)")
        st.dataframe(dup, use_container_width=True)
