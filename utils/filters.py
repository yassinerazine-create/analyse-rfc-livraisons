import streamlit as st
from utils.versioning import version_to_tuple

def filter_by_week(df):
    weeks = sorted(df["Semaine cible"].dropna().unique())
    selected = st.multiselect("Filtrer semaines", weeks, default=weeks)
    return df[df["Semaine cible"].isin(selected)]

def keep_highest_version_per_rfc_composant(df):
    df = df.copy()
    df["v_tuple"] = df["Version"].apply(version_to_tuple)
    df = df.loc[df.groupby(["RFC","Composant"])["v_tuple"].idxmax()]
    df = df.drop(columns="v_tuple")
    return df
