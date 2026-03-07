import streamlit as st
from utils.incoherence_detection import detect_version_incoherence

def show(df):

    st.title("Incohérences")

    inco = detect_version_incoherence(df)

    if inco.empty:

        st.success("Aucune incohérence")

    else:

        st.dataframe(inco,use_container_width=True)
