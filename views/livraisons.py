import streamlit as st
from utils.filters import filter_by_week, keep_highest_version_per_rfc_composant

def show(df):
    st.title("Vue par livraison")

    df = filter_by_week(df)
    df = keep_highest_version_per_rfc_composant(df)

    livraisons = st.multiselect(
        "Choisir Label(s)",
        sorted(df["Label"].dropna().unique()),
        default=sorted(df["Label"].dropna().unique()),
        placeholder="Sélectionner une ou plusieurs RFC"
    )


    df_filtered = df[df["Label"].isin(livraisons)]
    st.write("Nombre de lignes :", len(df_filtered))
    st.dataframe(df_filtered, use_container_width=True)
