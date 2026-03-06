import pandas as pd

def split_composant_version(df):
    """
    Crée deux colonnes : Composant et Version à partir de Composant_Version
    """
    def extract(val):
        val = str(val)

        # Séparer la partie version si ':' présent
        if ':' in val:
            composant_part, version_part = val.split(':', 1)
        else:
            composant_part = val
            version_part = ''

        # Si composant_part contient '_', séparer au premier '_'
        if '_' in composant_part:
            first_underscore = composant_part.find('_')
            composant = composant_part[:first_underscore]
            version = composant_part[first_underscore+1:]
        else:
            composant = composant_part
            version = version_part

        # Si version_part existe, on le remplace par la version après ':'
        if version_part:
            version = version_part

        return pd.Series([composant, version])

    df[['Composant', 'Version']] = df['Composant_Version'].apply(extract)
    return df
