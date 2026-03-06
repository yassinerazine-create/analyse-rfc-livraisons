import pandas as pd
import re


def split_composant_version(value):

    value = str(value)

    # cas ECHANGES
    if value.startswith("ECHANGES"):

        match = re.search(r"(\d+\.\d+(\.\d+)?(:\d+)?)", value)

        if match:
            return "ECHANGES", match.group(0)

    # cas standard composant:version
    if ":" in value:

        comp, ver = value.split(":", 1)

        return comp, ver

    # cas composant_version
    if "_" in value:

        comp, ver = value.split("_", 1)

        return comp, ver

    return value, ""


def filter_split_and_reorder(df):

    df = df.copy()

    df = df.rename(columns={
        "Label Livraison affecté": "Label"
    })

    split = df["Composant_Version"].apply(split_composant_version)

    df["Composant"] = split.apply(lambda x: x[0])
    df["Version"] = split.apply(lambda x: x[1])

    df = df[[
        "Semaine cible",
        "Composant",
        "Version",
        "UMEP",
        "RFC",
        "Label",
        "Composant_Version"
    ]]

    return df
