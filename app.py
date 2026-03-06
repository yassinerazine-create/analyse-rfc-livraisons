import streamlit as st
from views import chargement, incoherences, vue_ensemble, livraisons, rfc, composants, umep

st.set_page_config(page_title="Analyse RFC Livraisons", layout="wide")

# ==========================
# SESSION
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
        username = st.text_input("Utilisateur")
        password = st.text_input("Mot de passe", type="password")

        submit = st.form_submit_button("Se connecter")

        if submit:
            if username == "admin" and password == "admin":
                st.session_state.authenticated = True
                st.session_state.user = username
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

# bouton logout
if st.sidebar.button("Déconnexion"):
    st.session_state.authenticated = False
    st.session_state.user = None
    st.rerun()


# ==========================
# MENU
# ==========================

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Chargement des données",
        "Détection incohérences",
        "Vue d'ensemble",
        "Vue livraisons",
        "Vue RFC",
        "Vue composants",
        "Vue UMEP",
    ],
)


# ==========================
# ROUTER DES PAGES
# ==========================

if menu == "Chargement des données":
    chargement.show()

elif menu == "Détection incohérences":
    incoherences.show()

elif menu == "Vue d'ensemble":
    vue_ensemble.show()

elif menu == "Vue livraisons":
    livraisons.show()

elif menu == "Vue RFC":
    rfc.show()

elif menu == "Vue composants":
    composants.show()

elif menu == "Vue UMEP":
    umep.show()
