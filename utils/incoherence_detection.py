import pandas as pd
from utils.split import split_composant_version
from utils.versioning import version_to_tuple

def detect_version_incoherence(df: pd.DataFrame) -> pd.DataFrame:
    inco = []
    if "Composant" not in df.columns:
        df[["Composant", "Version"]] = df["Composant_Version"].apply(split_composant_version)

    for comp, g in df.groupby("Composant"):
        g = g.sort_values("Semaine cible")
        max_version_seen = None
        max_rfc_seen = None
        max_label_seen = None
        max_week_seen = None

        for week in sorted(g["Semaine cible"].dropna().unique()):
            week_df = g[g["Semaine cible"] == week].copy()
            if week_df["Version"].dropna().empty:
                continue
            week_df["v_tuple"] = week_df["Version"].apply(version_to_tuple)
            try:
                max_week_idx = week_df["v_tuple"].idxmax()
            except ValueError:
                continue
            max_week_version = week_df.loc[max_week_idx, "Version"]
            max_week_rfc = week_df.loc[max_week_idx, "RFC"] if "RFC" in week_df.columns else ""
            max_week_label = week_df.loc[max_week_idx, "Label"] if "Label" in week_df.columns else ""

            if max_version_seen is not None and version_to_tuple(max_week_version) < version_to_tuple(max_version_seen):
                inco.append({
                    "Composant": comp,
                    "Semaine concernée": week,
                    "RFC": max_week_rfc,
                    "Version max semaine": max_week_version,
                    "Version max précédente": max_version_seen,
                    "RFC précédente": max_rfc_seen,
                    "Label précédente": max_label_seen,
                    "Semaine précédente": max_week_seen
                })

            if max_version_seen is None or version_to_tuple(max_week_version) > version_to_tuple(max_version_seen):
                max_version_seen = max_week_version
                max_rfc_seen = max_week_rfc
                max_label_seen = max_week_label
                max_week_seen = week

    return pd.DataFrame(inco)
