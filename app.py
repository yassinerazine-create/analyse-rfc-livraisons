import streamlit as st

# import des pages
import views.chargement as chargement
import views.vue_ensemble as vue_ensemble
import views.livraisons as livraisons
import views.rfc as rfc
import views.composants as composants
import views.incoherences as incoherences
import views.umep as umep

from utils.auth import login

st.set_page_config(page_title="Analyse RFC / Livraisons", layout="wide")

# -------------------------
# SESSION
# -------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user" not in st.session_state:
    st.session_state.user = None

# -------------------------
# LOGIN
# -------------------------
if not st.session_state.authenticated:
    login()
    st.stop()

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.success(f"Connecté : {st.session_state.user}")

# bouton déconnexion
if st.sidebar.button("Déconnexion"):
    st.session_state.authenticated = False
    st.session_state.user = None
    st.experimental_rerun()

# menu navigation
page = st.sidebar.radio(
    "Navigation",
    [
        "Chargement des données",
        "Vue d'ensemble",
        "Livraisons",
        "RFC",
        "Composants",
        "Incohérences",
        "UMEP"
    ]
)

# -------------------------
# ROUTER
# -------------------------
if page == "Chargement des données":
    chargement.show()
elif page == "Vue d'ensemble":
    vue_ensemble.show()
elif page == "Livraisons":
    livraisons.show()
elif page == "RFC":
    rfc.show()
elif page == "Composants":
    composants.show()
elif page == "Incohérences":
    incoherences.show()
elif page == "UMEP":
    umep.show()
