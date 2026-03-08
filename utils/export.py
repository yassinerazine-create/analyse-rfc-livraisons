import streamlit as st
import pandas as pd

def export_excel(df,name="export.xlsx"):
    return st.download_button(
        "Télécharger Excel",
        df.to_csv(index=False),
        file_name=name
    )
