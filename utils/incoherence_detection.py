import pandas as pd
from utils.versioning import version_to_tuple

def detect_version_incoherence(df: pd.DataFrame) -> pd.DataFrame:
    """
    Détecte les incohérences de versions d'un composant selon les semaines.
    
    Règle :
    - Pour un composant X, si la version max installée en semaine N
      est inférieure à une version installée dans une semaine précédente,
      alors incohérence.
    """
    inco = []

    # parcours par composant
    for comp, g in df.groupby("Composant"):
        # trier par semaine croissante
        g = g.sort_values("Semaine cible")
        
        # on conserve le max version vue jusqu'à la semaine précédente
        max_version_seen = None
        
        for week in sorted(g["Semaine cible"].unique()):
            # dataframe de la semaine
            week_df = g[g["Semaine cible"] == week].copy()
            
            # trouver la version max de la semaine
            week_df["v_tuple"] = week_df["Version"].apply(version_to_tuple)
            max_week_idx = week_df["v_tuple"].idxmax()
            max_week_version = week_df.loc[max_week_idx, "Version"]
            
            if max_version_seen is not None:
                # comparer la version max de cette semaine avec la max précédente
                if version_to_tuple(max_week_version) < version_to_tuple(max_version_seen):
                    # incohérence détectée
                    inco.append({
                        "Composant": comp,
                        "Semaine concernée": week,
                        "Version max semaine": max_week_version,
                        "Version max précédente": max_version_seen,
                        "RFC": week_df.loc[max_week_idx, "RFC"] if "RFC" in week_df.columns else "",
                        "Label": week_df.loc[max_week_idx, "Label"] if "Label" in week_df.columns else ""
                    })
            
            # mettre à jour max_version_seen
            max_version_seen = max(max_version_seen or "0.0.0", max_week_version, key=version_to_tuple)

    return pd.DataFrame(inco)
