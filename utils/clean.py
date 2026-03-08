import pandas as pd
import re

def split_composant_version(value: str):
    value = str(value).strip()

    # ":" prioritaire
    if ":" in value:
        composant, version = value.split(":", 1)
        return composant, version

    # "_" -> dernière partie = version
    if "_" in value:
        parts = value.split("_")
        composant = "_".join(parts[:-1])
        version = parts[-1]
        return composant, version

    return value, ""

def filter_split_and_reorder(df):
    df = df.copy()

    # rename colonne si besoin
    rename_map = {"Label Livraison affecté": "Label"}
    df = df.rename(columns=rename_map)

    # semaine cible
    if "Semaine cible" in df.columns:
        df["Semaine cible"] = df["Semaine cible"].astype(str).str.replace("S","", regex=False)
        df["Semaine cible"] = pd.to_numeric(df["Semaine cible"], errors="coerce")

    # split composant/version
    if "Composant_Version" in df.columns:
        split = df["Composant_Version"].apply(split_composant_version)
        df["Composant"] = split.apply(lambda x:x[0])
        df["Version"] = split.apply(lambda x:x[1])

    # colonnes finales
    desired_cols = [
        "Année Mois cible (LAAMM)",
        "Semaine cible",
        "Composant",
        "Version",
        "UMEP",
        "RFC",
        "Label"
    ]
    cols = [c for c in desired_cols if c in df.columns]
    df = df[cols]

    return df