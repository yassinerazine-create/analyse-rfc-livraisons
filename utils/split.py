import pandas as pd
import re

def split_composant_version(cv: str):
    """
    Split un champ Composant_Version en composant et version, supporte tous les formats listés.
    """
    if pd.isna(cv):
        return pd.Series([None, None])

    # Gérer le cas avec '_Echanges...' répété ou ':' répété
    # On garde toujours la première occurrence du composant avant le dernier '_'
    # et on prend la version correcte après le dernier '_'
    
    # Remplacer les doublons ECHANGES_025.110.12:ECHANGES_025.110.12 => ECHANGES_025.110.12
    if '_' in cv:
        # Séparer par '_' puis prendre la partie composant
        # Rechercher le motif composant_XX.YY.ZZ(:YY)
        # Si ':' présent, prendre juste avant ':'
        # Utilisation regex pour capturer composant et version
        match = re.search(r'^([A-Z]+(?:_[A-Z0-9]+)*)_(\d[\d.:]*)', cv)
        if match:
            composant = match.group(1)
            version = match.group(2)
            return pd.Series([composant, version])

    # fallback
    return pd.Series([cv, None])
