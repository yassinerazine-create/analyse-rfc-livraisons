import streamlit as st
from views import chargement, vue_ensemble, livraisons, rfc, composants, incoherences, umep

# Initialisation de la session
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


# Fonction de connexion
def login():
    st.title("Connexion")

    with st.form("login_form"):
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")

        submit = st.form_submit_button("Se connecter")

        if submit:
            if username == "admin" and password == "admin":
                st.session_state.authenticated = True
                st.success("Connexion réussie")
                st.rerun()
            else:
                st.error("Identifiants incorrects")


# Si NON connecté
if not st.session_state.authenticated:
    login()

# Si connecté
else:
    st.sidebar.success("Connecté")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Vue d'ensemble",
            "Chargement",
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

    if page == "Chargement":
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


# LOGOUT
if st.sidebar.button("Déconnexion"):
    st.session_state.authenticated = False
    st.rerun()


    st.title(page)

