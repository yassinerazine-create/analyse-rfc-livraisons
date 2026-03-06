import pandas as pd
from utils.versioning import version_to_tuple


def detect_version_incoherence(df):

    rows = []

    df = df.copy()

    df["v"] = df["Version"].apply(version_to_tuple)

    for comp, g in df.groupby("Composant"):

        g = g.sort_values("v")

        for i in range(len(g)-1):

            a = g.iloc[i]

            for j in range(i+1, len(g)):

                b = g.iloc[j]

                if a["v"] < b["v"] and a["Semaine cible"] > b["Semaine cible"]:

                    rows.append({
                        "Composant": comp,

                        "RFC A": a["RFC"],
                        "Version A": a["Version"],
                        "Semaine A": a["Semaine cible"],

                        "RFC B": b["RFC"],
                        "Version B": b["Version"],
                        "Semaine B": b["Semaine cible"]
                    })

    return pd.DataFrame(rows)


def detect_same_version_multi_week(df):

    return df.groupby(
        ["Composant", "Version"]
    ).filter(lambda x: x["Semaine cible"].nunique() > 1)
