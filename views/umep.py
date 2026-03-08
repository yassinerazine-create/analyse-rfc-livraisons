import streamlit as st

def show(df):
    st.title("UMEP")
    
    # vérifie si colonne UMEP existe
    if "UMEP" not in df.columns:
        st.warning("Colonne UMEP absente dans le fichier")
        return

    # filtre semaine si présent
    if "Semaine cible" in df.columns:
        weeks = sorted(df["Semaine cible"].dropna().unique())
        selected_weeks = st.multiselect("Filtrer par semaine", weeks, default=weeks)
        df = df[df["Semaine cible"].isin(selected_weeks)]

    # multiselect UMEP
    umep_values = sorted(df["UMEP"].dropna().unique())
    selected_umep = st.multiselect("Sélectionner UMEP", umep_values, default=umep_values)
    if selected_umep:
        df = df[df["UMEP"].isin(selected_umep)]

    st.dataframe(df,use_container_width=True)
