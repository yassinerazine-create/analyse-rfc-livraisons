import streamlit as st
from utils.incoherence_detection import detect_version_incoherence
from utils.incoherence_detection import detect_same_version_multi_week
from utils.filters import filter_by_week


def highlight_rows(row):

    return ["background-color:#ffcccc"] * len(row)


def show(df):

    st.title("Détection des incohérences")

    df = filter_by_week(df)

    st.subheader("Incohérences Version / Semaine")

    inco = detect_version_incoherence(df)

    if len(inco) == 0:
        st.success("Aucune incohérence")
    else:
        st.dataframe(inco.style.apply(highlight_rows, axis=1))

    st.subheader("Même version planifiée plusieurs semaines")

    dup = detect_same_version_multi_week(df)

    if len(dup) == 0:
        st.success("Aucune duplication")
    else:
        st.dataframe(dup)
