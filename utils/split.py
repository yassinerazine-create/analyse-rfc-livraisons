import re

def split_composant_version(cv: str):
    """
    Split un champ Composant_Version en composant et version.
    
    Gère les formats :
    - XXXX_02.12.52 -> XXXX / 02.12.52
    - XXXX_02.12:01 -> XXXX / 02.12:01
    - XX_YY_01.10.00 -> XX_YY / 01.10.00
    - XX_YY_01.10:02 -> XX_YY / 01.10:02
    - AAA_BBB_CCC_03.04.05 -> AAA_BBB_CCC / 03.04.05
    - ECHANGES_025.110.12:01 -> ECHANGES / 025.110.12:01
    - XXXXX_101_YYYYY:12.025.01 -> XXXXX_101_YYYYY / 12.025.01
    """
    if pd.isna(cv):
        return pd.Series([None, None])

    # cas avec ':' séparateur principal
    if ':' in cv and cv.count(':') == 1:
        parts = cv.split(':')
        prefix = parts[0]
        suffix = parts[1]
        # vérifier si prefix contient '_', prendre tout avant dernier '_'
        if '_' in prefix:
            idx = prefix.rfind('_')
            composant = prefix[:idx]
            version = prefix[idx+1:] + ':' + suffix
        else:
            composant = prefix
            version = suffix
        return pd.Series([composant, version])

    # sinon on split sur dernier '_' pour les autres formats
    if '_' in cv:
        idx = cv.rfind('_')
        composant = cv[:idx]
        version = cv[idx+1:]
        return pd.Series([composant, version])

    # fallback
    return pd.Series([cv, None])
