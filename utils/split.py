import pandas as pd

def split_composant_version(df):
    """
    Scinde la colonne Composant_Version en deux colonnes : Composant et Version
    Règles :
    - ECHANGES_025.149.01:ECHANGES_025.149.01  -> Composant=ECHANGES, Version=025.149.01
    - ECHANGES_025.110:02                       -> Composant=ECHANGES, Version=025.110:02
    - Les autres : split sur ':' directement
    """

    def extract(val):
        val = str(val)

        # Cas ECHANGES spécial
        if val.startswith("ECHANGES_"):
            # si format ECHANGES_025.149.01:ECHANGES_025.149.01
            if ':' in val:
                parts = val.split(':')
                composant_part = parts[0]
                version_part = parts[1]

                # Composant = partie avant premier '_'
                composant = composant_part.split('_')[0]
                # Version = partie après premier '_' de la première partie
                version = composant_part[len(composant)+1:]
                
                # Mais si la partie après ':' est dupliquée comme ECHANGES_025.149.01, on prend juste la version
                # pour qu'on ait 025.149.01
                if version.startswith(composant + "_"):
                    version = version[len(composant)+1:]
                
                # Si format comme ECHANGES_025.110:02, version = 025.110:02
                if version_part != composant_part:
                    version = version_part
            else:
                # Pas de ':', split sur '_' pour composant et version
                composant = val.split('_')[0]
                version = val[len(composant)+1:]
        else:
            # Autres composants : split sur ':'
            if ':' in val:
                composant, version = val.split(':', 1)
            else:
                composant = val
                version = ''

        return pd.Series([composant.upper(), version])

    df[['Composant', 'Version']] = df['Composant_Version'].apply(extract)
    return df
