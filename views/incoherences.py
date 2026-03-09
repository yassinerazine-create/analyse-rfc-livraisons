import streamlit as st
import pandas as pd


def show(df: pd.DataFrame):

    st.subheader("⚠️ Vue Incohérences")

    if df.empty:
        st.warning("Aucune donnée chargée.")
        return

    data = df.copy()

    # normalisation colonnes
    cols = {
        "Application": "Application",
        "Version": "Version",
        "RFC": "RFC",
        "Label": "Label",
        "Semaine": "Semaine",
        "Semaine cible": "Semaine cible",
        "Version max semaine": "Version max semaine"
    }

    for c in cols:
        if c not in data.columns:
            data[c] = None

    data = data.rename(columns=cols)

    # tri pour trouver version précédente
    data = data.sort_values(["Application", "Version"])

    data["Prev Version"] = data.groupby("Application")["Version"].shift(1)
    data["Prev RFC"] = data.groupby("Application")["RFC"].shift(1)
    data["Prev Label"] = data.groupby("Application")["Label"].shift(1)
    data["Prev Semaine"] = data.groupby("Application")["Semaine"].shift(1)

    inco = data.copy()

    def format_prev(row):
        v = row.get("Prev Version")
        rfc = row.get("Prev RFC")
        label = row.get("Prev Label")
        week = row.get("Prev Semaine")

        if pd.isna(v):
            return ""

        # sécurisation semaine
        if pd.notna(week):
            try:
                week = f"S{int(float(week))}"
            except:
                week = str(week)
        else:
            week = ""

        rfc = "" if pd.isna(rfc) else str(rfc)
        label = "" if pd.isna(label) else str(label)

        return f"{v} ({rfc}, {label}, {week})"

    inco["Version max précédente"] = inco.apply(format_prev, axis=1)

    # colonnes affichées
    result = inco[
        [
            "Application",
            "Version",
            "RFC",
            "Label",
            "Semaine cible",
            "Semaine",
            "Version max semaine",
            "Version max précédente",
        ]
    ]

    st.dataframe(result, use_container_width=True)

    st.download_button(
        "📥 Télécharger les incohérences",
        result.to_csv(index=False).encode("utf-8"),
        "incoherences.csv",
        "text/csv"
    )
