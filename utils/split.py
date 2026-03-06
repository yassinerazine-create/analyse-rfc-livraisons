# utils/split.py
import pandas as pd

def split_composant_version(df):
    """
    Scinde Composant_Version en Composant et Version
    """
    def extract(val):
        val = str(val)
        if ':' in val:
            composant_part, version_part = val.split(':', 1)
        else:
            composant_part = val
            version_part = ''

        if '_' in composant_part:
            first_underscore = composant_part.find('_')
            composant = composant_part[:first_underscore]
            version = composant_part[first_underscore+1:]
        else:
            composant = composant_part
            version = version_part

        if version_part:
            version = version_part

        return pd.Series([composant, version])

    df[['Composant', 'Version']] = df['Composant_Version'].apply(extract)
    return df
