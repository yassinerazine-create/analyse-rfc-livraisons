import pandas as pd
from utils.versioning import version_to_tuple

def detect_version_incoherence(df):

    inco = []

    for comp, g in df.groupby("Composant"):

        g = g.sort_values("Semaine cible")

        for i in range(len(g)-1):

            v1 = g.iloc[i]["Version"]
            v2 = g.iloc[i+1]["Version"]

            if version_to_tuple(v2) < version_to_tuple(v1):

                inco.append({

                    "Composant":comp,
                    "Version A":v1,
                    "Semaine A":g.iloc[i]["Semaine cible"],
                    "Version B":v2,
                    "Semaine B":g.iloc[i+1]["Semaine cible"]
                })

    return pd.DataFrame(inco)
