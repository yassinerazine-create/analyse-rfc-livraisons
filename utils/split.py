import pandas as pd

def split_composant_version(cv: str):
    if pd.isna(cv):
        return pd.Series([None, None])

    if ':' in cv and cv.count(':') == 1:
        parts = cv.split(':')
        prefix = parts[0]
        suffix = parts[1]
        if '_' in prefix:
            idx = prefix.rfind('_')
            composant = prefix[:idx]
            version = prefix[idx+1:] + ':' + suffix
        else:
            composant = prefix
            version = suffix
        return pd.Series([composant, version])

    if '_' in cv:
        idx = cv.rfind('_')
        composant = cv[:idx]
        version = cv[idx+1:]
        return pd.Series([composant, version])

    return pd.Series([cv, None])
