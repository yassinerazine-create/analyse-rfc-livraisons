import pandas as pd
import re

def split_composant_version(value):

    value = str(value)

    if value.startswith("ECHANGES"):

        match = re.search(r"(\d+\.\d+(\.\d+)*)", value)

        if match:
            return "ECHANGES", match.group(0)

    if ":" in value:

        comp, ver = value.split(":",1)

        return comp, ver

    return value,""


def filter_split_and_reorder(df):

    df = df.copy()

    df["Semaine cible"] = (
        df["Semaine cible"]
        .astype(str)
        .str.replace("S","")
    )

    df["Semaine cible"] = pd.to_numeric(
        df["Semaine cible"],
        errors="coerce"
    )

    split = df["Composant_Version"].apply(split_composant_version)

    df["Composant"] = split.apply(lambda x:x[0])
    df["Version"] = split.apply(lambda x:x[1])

    cols = [
        "Année Mois cible (LAAMM)",
        "Semaine cible",
        "Composant",
        "Version",
        "UMEP",
        "RFC",
        "Label"
    ]

    df = df[cols]

    return df
