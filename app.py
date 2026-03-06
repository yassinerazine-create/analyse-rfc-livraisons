import streamlit as st

# Import des views
from views import chargement, vue_ensemble, livraisons, rfc, composants, incoherences, umep


# ==========================
# INITIALISATION SESSION
# ==========================

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user" not in st.session_state:
    st.session_state.user = None


# ==========================
# PAGE LOGIN
# ==========================

def login():

    st.title("Connexion")

    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):

        if username == "admin" and password == "admin":
            st.session_state.authenticated = True
            st.session_state.user = username
            st.success("Connexion réussie")
            st.rerun()

        else:
            st.error("Identifiants incorrects")


# ==========================
# SI PAS CONNECTÉ
# ==========================

if not st.session_state.authenticated:
    login()
    st.stop()


# ==========================
# SIDEBAR
# ==========================

st.sidebar.success(f"Connecté : {st.session_state.user}")

# bouton déconnexion
if st.sidebar.button("Déconnexion"):
    st.session_state.authenticated = False
    st.session_state.user = None
    st.rerun()


# ==========================
# MENU
# ==========================

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


# ==========================
# ROUTER DES PAGES
# ==========================

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
