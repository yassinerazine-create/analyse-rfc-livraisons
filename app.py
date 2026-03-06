import streamlit as st

# Import des pages
from views import chargement, vue_ensemble, livraisons, rfc, composants, incoherences, umep


# ==========================
# INITIALISATION SESSION
# ==========================

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "user" not in st.session_state:
    st.session_state.user = None


# ==========================
# LOGIN
# ==========================

def login():

    st.title("Connexion")

    with st.form("login_form"):
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")

        submit = st.form_submit_button("Se connecter")

        if submit:
            if username == "admin" and password == "admin":
                st.session_state.authenticated = True
                st.session_state.user = username
                st.success("Connexion réussie")
                st.rerun()
            else:
                st.error("Identifiants incorrects")


# ==========================
# SI NON CONNECTÉ
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
# ROUTER
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
