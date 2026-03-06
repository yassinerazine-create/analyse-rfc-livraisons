import pandas as pd

def split_composant_version(df):
    """
    Scinde la colonne Composant_Version en Composant et Version
    Cas traités :
    - abcf_sla_101_interface_fournisseurs:2.00.27 -> Composant = abcf_sla_101_interface_fournisseurs, Version = 2.00.27
    - ECHANGES_025.110:02 -> Composant = ECHANGES, Version = 025.110:02
    - ECHANGES_025.149.01:ECHANGES_025.149.01 -> Composant = ECHANGES, Version = 025.149.01
    """

    def extract(val):
        val = str(val)

        if val.startswith("ECHANGES_"):
            # Composant = ECHANGES
            composant = "ECHANGES"

            # Vérifier s'il y a ':'
            if ':' in val:
                parts = val.split(':', 1)
                left = parts[0]   # ECHANGES_025.110 ou ECHANGES_025.149.01
                right = parts[1]  # peut être "02" ou "ECHANGES_025.149.01"

                # Pour ECHANGES_025.149.01:ECHANGES_025.149.01
                if right.startswith("ECHANGES_"):
                    version = left.split('_',1)[1]  # tout après le premier '_'
                else:
                    # Pour ECHANGES_025.110:02
                    version = left.split('_',1)[1] + ":" + right  # 025.110:02
            else:
                # Pas de ':', juste prendre après premier '_'
                version = val.split('_',1)[1]

        else:
            # Autres composants : split normal sur ':'
            if ':' in val:
                composant, version = val.split(':',1)
            else:
                composant = val
                version = ''

        return pd.Series([composant.upper(), version])

    df[['Composant', 'Version']] = df['Composant_Version'].apply(extract)
    return df
