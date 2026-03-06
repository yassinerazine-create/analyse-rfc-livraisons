import pandas as pd
from .split import split_composant_version

def filter_and_split(df):
    """Garde les colonnes essentielles et scinde Composant_Version"""
    cols = ["Composant_Version", "RFC", "UMEP", "Semaine cible", "Label Livraison affecté"]
    df = df[[c for c in cols if c in df.columns]]
    df = split_composant_version(df)
    return df
