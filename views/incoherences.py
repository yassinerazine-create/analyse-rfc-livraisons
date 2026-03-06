import streamlit as st
import pandas as pd


def version_to_tuple(version):
    """Convertit une version en tuple comparable"""
    version = str(version).replace(":", ".")
    parts = version.split(".")

    try:
        return tuple(int(p) for p in parts)
    except:
        return (0,)


# --------------------------------------------------
# INCOHERENCE VERSION / SEMAINE
# --------------------------------------------------
def detect_version_incoherences(df):

    incoherences = []

    df["version_tuple"] = df["Version"].apply(version_to_tuple)

    for composant, group in df.groupby("Composant"):

        group = group.sort_values("version_tuple")

        for i in range(len(group)):
            for j in range(i + 1, len(group)):

                row_a = group.iloc[i]
                row_b = group.iloc[j]

                version_a = row_a["version_tuple"]
                version_b = row_b["version_tuple"]

                semaine_a = row_a["Semaine cible"]
                semaine_b = row_b["Semaine cible"]

                if version_a < version_b and semaine_a > semaine_b:

                    incoherences.append({
                        "Composant": composant,

                        "RFC A": row_a["RFC"],
                        "Version A": row_a["Version"],
                        "Semaine cible A": semaine_a,

                        "RFC B": row_b["RFC"],
                        "Version B": row_b["Version"],
                        "Semaine cible B": semaine_b,

                        "UMEP A": row_a["UMEP"],
                        "UMEP B": row_b["UMEP"],

                        "Label A": row_a["Label"],
                        "Label B": row_b["Label"]
                    })

    return pd.DataFrame(incoherences)


# --------------------------------------------------
# MEME VERSION / SEMAINES DIFFERENTES
# --------------------------------------------------
def detect_same_version_multiple_weeks(df):

    duplicates = df.groupby(["Composant", "Version"]).filter(
        lambda x: x["Semaine cible"].nunique() > 1
    )

    return duplicates.sort_values(["Composant", "Version", "Semaine cible"])


# --------------------------------------------------
# PAGE STREAMLIT
# --------------------------------------------------
def show(df):

    st.title("Détection des incohérences")

    # ----------------------------------
    # tableau 1
    # ----------------------------------
    st.subheader("Incohérences Version / Semaine")

    inco = detect_version_incoherences(df)

    if inco.empty:
        st.success("Aucune incohérence détectée")
    else:
        st.warning(f"{len(inco)} incohérence(s) détectée(s)")
        st.dataframe(inco, use_container_width=True)

    # ----------------------------------
    # tableau 2
    # ----------------------------------
    st.subheader("Même composant et version sur plusieurs semaines")

    dup = detect_same_version_multiple_weeks(df)

    if dup.empty:
        st.success("Aucune version planifiée sur plusieurs semaines")
    else:
        st.warning(f"{len(dup)} ligne(s) concernée(s)")
        st.dataframe(dup, use_container_width=True)
