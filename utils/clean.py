import pandas as pd

def filter_columns(df):
    """Ne garde que les colonnes essentielles pour l'application"""
    cols = ["Composant_Version", "RFC", "UMEP", "Semaine cible", "Label Livraison affecté"]
    # garder seulement les colonnes existantes
    return df[[c for c in cols if c in df.columns]]
