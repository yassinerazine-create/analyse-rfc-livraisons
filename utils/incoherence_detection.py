import pandas as pd
from utils.versioning import version_to_tuple

def detect_version_incoherence(df: pd.DataFrame):
    inco = []
    for comp, g in df.groupby("Composant"):
        g = g.sort_values("Semaine cible")
        for i in range(len(g)-1):
            v1, v2 = g.iloc[i]["Version"], g.iloc[i+1]["Version"]
            s1, s2 = g.iloc[i]["Semaine cible"], g.iloc[i+1]["Semaine cible"]
            if version_to_tuple(v2) < version_to_tuple(v1):
                inco.append({
                    "Composant": comp,
                    "Version supérieure": v1,
                    "Semaine supérieure": s1,
                    "Version inférieure": v2,
                    "Semaine inférieure": s2
                })
    return pd.DataFrame(inco)
