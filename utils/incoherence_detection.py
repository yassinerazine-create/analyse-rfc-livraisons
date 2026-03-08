import pandas as pd
from utils.versioning import version_to_tuple

def detect_version_incoherence(df: pd.DataFrame) -> pd.DataFrame:
    """
    Détecte les incohérences de versions par semaine pour chaque composant.
    
    Règle :
    - Pour un composant X, si la version max installée en semaine N
      est inférieure à une version max installée dans une semaine précédente,
      alors incohérence.
    """
    inco = []

    for comp, g in df.groupby("Composant"):
        g = g.sort_values("Semaine cible")
        max_version_seen = None

        for week in sorted(g["Semaine cible"].dropna().unique()):
            week_df = g[g["Semaine cible"] == week].copy()

            # ignorer si aucune version
            if week_df["Version"].dropna().empty:
                continue

            # convertir en tuple pour comparaison
            week_df["v_tuple"] = week_df["Version"].apply(version_to_tuple)

            # sécurité : idxmax peut échouer si tout NaN
            try:
                max_week_idx = week_df["v_tuple"].idxmax()
            except ValueError:
                continue

            max_week_version = week_df.loc[max_week_idx, "Version"]

            # comparer avec la version max vue précédemment
            if max_version_seen is not None:
                if version_to_tuple(max_week_version) < version_to_tuple(max_version_seen):
                    inco.append({
                        "Composant": comp,
                        "Semaine concernée": week,
                        "Version max semaine": max_week_version,
                        "Version max précédente": max_version_seen,
                        "RFC": week_df.loc[max_week_idx, "RFC"] if "RFC" in week_df.columns else "",
                        "Label": week_df.loc[max_week_idx, "Label"] if "Label" in week_df.columns else ""
                    })

            # mettre à jour la version max vue
            if max_version_seen is None:
                max_version_seen = max_week_version
            else:
                # choisir la plus grande entre max_version_seen et max_week_version
                max_version_seen = max(
                    max_version_seen,
                    max_week_version,
                    key=version_to_tuple
                )

    return pd.DataFrame(inco)
