import streamlit as st
import pandas as pd


def version_to_tuple(version):
    """
    Convertit une version '025.149.01' ou '025.110:02'
    en tuple comparable.
    """
    version = str(version)

    version = version.replace(":", ".")
    parts = version.split(".")

    try:
        return tuple(int(p) for p in parts)
    except:
        return (0,)


def detect_incoherences(df):

    incoherences = []

    # convertir versions pour comparaison
    df["version_tuple"] = df["Version"].apply(version_to_tuple)

    # grouper par composant
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


def show(df):

    st.title("Détection des incohérences")

    inco = detect_incoherences(df)

    if inco.empty:
        st.success("✅ Aucune incohérence détectée")
        return

    st.warning(f"⚠️ {len(inco)} incohérence(s) détectée(s)")

    st.dataframe(
        inco,
        use_container_width=True
    )
