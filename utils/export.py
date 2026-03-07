import pandas as pd
import streamlit as st

def export_excel(df,name="export.xlsx"):

    return st.download_button(
        "Télécharger Excel",
        df.to_csv(index=False),
        file_name=name
    )
