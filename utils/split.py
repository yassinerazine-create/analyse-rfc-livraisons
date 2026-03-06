import pandas as pd
import re


def split_component_version(value):

    value = str(value)

    if value.startswith("ECHANGES"):

        match = re.search(r"(\d+\.\d+(\.\d+)?(:\d+)?)", value)

        if match:
            return "ECHANGES", match.group(0)

    if ":" in value:
        parts = value.split(":")
        return parts[0], parts[1]

    if "_" in value:
        parts = value.split("_", 1)
        return parts[0], parts[1]

    return value, ""


def filter_split_and_reorder(df):

    df = df.copy()

    df = df.rename(columns={
        "Label Livraison affecté": "Label"
    })

    comp = df["Composant_Version"].apply(split_component_version)

    df["Composant"] = comp.apply(lambda x: x[0])
    df["Version"] = comp.apply(lambda x: x[1])

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
