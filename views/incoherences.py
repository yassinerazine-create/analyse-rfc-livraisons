import streamlit as st
import pandas as pd


def show(df: pd.DataFrame):

    st.subheader("⚠️ Vue incohérences")

    if df is None or df.empty:
        st.warning("Aucune donnée disponible.")
        return

    data = df.copy()

    # sécurisation des colonnes nécessaires
    needed_cols = [
        "Application",
        "Version",
        "RFC",
        "Label",
        "Semaine",
        "Semaine cible",
        "Version max semaine",
    ]

    for col in needed_cols:
        if col not in data.columns:
            data[col] = ""

    # tri pour déterminer version précédente
    data = data.sort_values(["Application", "Version"])

    data["Prev Version"] = data.groupby("Application")["Version"].shift(1)
    data["Prev RFC"] = data.groupby("Application")["RFC"].shift(1)
    data["Prev Label"] = data.groupby("Application")["Label"].shift(1)
    data["Prev Semaine"] = data.groupby("Application")["Semaine"].shift(1)

    inco = data.copy()

    # format sécurisé
    def format_prev(row):

        v = row.get("Prev Version", "")
        rfc = row.get("Prev RFC", "")
        label = row.get("Prev Label", "")
        week = row.get("Prev Semaine", "")

        if pd.isna(v) or v == "":
            return ""

        rfc = "" if pd.isna(rfc) else str(rfc)
        label = "" if pd.isna(label) else str(label)

        if pd.isna(week) or week == "":
            week_str = ""
        else:
            try:
                week_str = f"S{int(float(week))}"
            except:
                week_str = str(week)

        return f"{v} ({rfc}, {label}, {week_str})"

    inco["Version max précédente"] = inco.apply(format_prev, axis=1)

    # colonnes finales affichées
    display_cols = [
        "Application",
        "Version",
        "RFC",
        "Label",
        "Semaine cible",
        "Semaine",
        "Version max semaine",
        "Version max précédente",
    ]

    result = inco[display_cols]

    st.dataframe(result, use_container_width=True)

    # export
    csv = result.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Télécharger les incohérences",
        csv,
        "incoherences.csv",
        "text/csv"
    )
