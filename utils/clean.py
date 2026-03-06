import pandas as pd
from .split import split_composant_version

def reorder_columns(df):
    """
    Réorganise les colonnes dans l'ordre désiré
    """
    desired_order = [
        "Semaine cible",
        "Composant",
        "Version",
        "UMEP",
        "RFC",
        "Label Livraison affecté",
        "Composant_Version"
    ]
    # garder uniquement les colonnes existantes
    cols = [c for c in desired_order if c in df.columns]
    return df[cols]

def filter_split_and_reorder(df):
    """
    1️⃣ garde les colonnes essentielles
    2️⃣ scinde Composant_Version en Composant / Version
    3️⃣ réorganise les colonnes
    """
    # Colonnes à garder
    essential_cols = ["Composant_Version", "RFC", "UMEP", "Semaine cible", "Label Livraison affecté"]
    df = df[[c for c in essential_cols if c in df.columns]]

    # Split composant/version
    df = split_composant_version(df)

    # Réordonner les colonnes
    df = reorder_columns(df)

    return df

def filter_columns(df):
    """
    Filtrage simple pour compatibilité ancienne version
    """
    return filter_split_and_reorder(df)
