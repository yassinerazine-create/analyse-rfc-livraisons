import pandas as pd
import re

def split_composant_version(value):

    value = str(value)

    # Cas ECHANGES
    if value.startswith("ECHANGES"):
        match = re.search(r"(\d+\.\d+(\.\d+)?(:\d+)?)", value)
        if match:
            return "ECHANGES", match.group(0)

    # Cas standard composant:version
    if ":" in value:
        comp, ver = value.split(":", 1)
        return comp, ver

    # Cas composant_version
    if "_" in value:
        comp, ver = value.split("_", 1)
        return comp, ver

    return value, ""


def filter_split_and_reorder(df):

    df = df.copy()

    # renommer colonne label si nécessaire
    df = df.rename(columns={
        "Label Livraison affecté": "Label"
    })

    # convertir semaine Sxx en nombre
    df["Semaine cible"] = df["Semaine cible"].astype(str).str.upper().str.replace("S", "", regex=False)
    df["Semaine cible"] = pd.to_numeric(df["Semaine cible"], errors="coerce")

    # split composant/version
    split = df["Composant_Version"].apply(split_composant_version)
    df["Composant"] = split.apply(lambda x: x[0])
    df["Version"] = split.apply(lambda x: x[1])

    # réorganisation des colonnes avec Année Mois cible (LAAMM) au début
    cols = ["Année Mois cible (LAAMM)", "Semaine cible", "Composant", "Version", "UMEP", "RFC", "Label", "Composant_Version"]
    df = df[cols]

    return df
