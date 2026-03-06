import streamlit as st
import pandas as pd

def show():
    st.title("Chargement des données")

    file = st.file_uploader("Importer fichier", type=["csv","xlsx"])
    if file:

        #lecture du fichier
        if file.name.endswith("csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)


        #Nettoyage du fichier
        if "RFC" in df.columns:
            #garder uniquement les lignes avec donnée RFC commenant par 'RFC'
            df=df[df["RFC"].astype(str).str.upper().str.startswith("RFC")]

            st.success ("donnée nettoyées : lignes sans RFC ou RFC incorrectes supprimées")

        else:
            st.warning("Colonne 'RFC' non trouvée dans le fichier")

        # garder uniquement les colonnes essentielles
        df = filter_columns(df)

        
        st.session_state["data"] = df
        st.success("Données chargées")
        st.dataframe(df)
