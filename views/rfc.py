import streamlit as st
from utils.filters import filter_by_week, keep_highest_version_per_rfc_composant

def show(df):
    st.title("Vue par RFC")

    df = filter_by_week(df)

    # garder seulement la version max pour chaque RFC+Composant
    df = keep_highest_version_per_rfc_composant(df)

    rfcs = st.multiselect(
    "Choisir RFC(s)",
    sorted(df["RFC"].dropna().unique()),
    default=sorted(df["RFC"].dropna().unique()),
    placeholder="Sélectionner une ou plusieurs RFC"
)


    df_filtered = df[df["RFC"].isin(rfcs)]

    st.write("Nombre de lignes :", len(df_filtered))
    st.dataframe(df_filtered, use_container_width=True)
