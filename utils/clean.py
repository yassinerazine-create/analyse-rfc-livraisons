import pandas as pd
from .split import split_composant_version

def filter_split_and_reorder(df: pd.DataFrame) -> pd.DataFrame:
    # garde uniquement les colonnes importantes
    cols_to_keep = ["Composant_Version", "RFC", "UMEP", "Semaine cible", "Label Livraison affecté", "Année Mois cible (LAAMM)"]
    df = df[[c for c in cols_to_keep if c in df.columns]]

    # split composant_version
    df[["Composant", "Version"]] = df["Composant_Version"].apply(split_composant_version)

    # réorganiser colonnes
    columns_order = ["Année Mois cible (LAAMM)", "Semaine cible", "RFC", "Composant", "Version", "UMEP", "Label Livraison affecté", "Composant_Version"]
    df = df[[c for c in columns_order if c in df.columns]]

    return df
