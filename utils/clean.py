import pandas as pd
import re

def split_composant_version(value):

    value = str(value)

    if value.startswith("ECHANGES"):
        match = re.search(r"(\d+\.\d+(\.\d+)*)", value)
        if match:
            return "ECHANGES", match.group(0)

    if ":" in value:
        comp, ver = value.split(":", 1)
        return comp, ver

    return value, ""


def filter_split_and_reorder(df):

    df = df.copy()

    # renommer colonnes si nécessaire
    rename_map = {
        "Label Livraison affecté": "Label"
    }

    df = df.rename(columns=rename_map)

    # conversion semaine
    if "Semaine cible" in df.columns:

        df["Semaine cible"] = (
            df["Semaine cible"]
            .astype(str)
            .str.replace("S", "", regex=False)
        )

        df["Semaine cible"] = pd.to_numeric(
            df["Semaine cible"],
            errors="coerce"
        )

    # split composant/version
    if "Composant_Version" in df.columns:

        split = df["Composant_Version"].apply(split_composant_version)

        df["Composant"] = split.apply(lambda x: x[0])
        df["Version"] = split.apply(lambda x: x[1])

    # ordre colonnes souhaité
    desired_cols = [
        "Année Mois cible (LAAMM)",
        "Semaine cible",
        "Composant",
        "Version",
        "UMEP",
        "RFC",
        "Label"
    ]

    # garder uniquement les colonnes présentes
    cols = [c for c in desired_cols if c in df.columns]

    df = df[cols]

    return df
