# utils/clean.py
from .split import split_composant_version

def filter_columns(df):
    """
    Garde uniquement les colonnes essentielles
    """
    cols = ["RFC", "UMEP", "Semaine cible", "Label Livraison affecté"]
    df = df[[c for c in cols if c in df.columns]]
    df = split_composant_version(df)
    return df
