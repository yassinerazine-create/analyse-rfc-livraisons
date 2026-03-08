import streamlit as st
import matplotlib.pyplot as plt

def show(df):
    st.title("Dashboard")
    col1,col2,col3 = st.columns(3)
    col1.metric("RFC", df["RFC"].nunique())
    col2.metric("Composants", df["Composant"].nunique())
    col3.metric("UMEP", df["UMEP"].nunique())

    st.subheader("Livraisons par semaine")
    counts = df.groupby("Semaine cible").size()
    fig,ax = plt.subplots()
    ax.bar(counts.index,counts.values,color="#2563eb")
    ax.set_xlabel("Semaine")
    ax.set_ylabel("Nombre de livraisons")
    st.pyplot(fig)
