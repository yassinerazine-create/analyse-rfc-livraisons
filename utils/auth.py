import streamlit as st

# utilisateurs
users = {
    "admin": {"password": "admin123"},
    "user": {"password": "user123"}
}

def login():
    st.title("Connexion")

    # widgets login
    username = st.text_input("Utilisateur")
    password = st.text_input("Mot de passe", type="password")
    login_button = st.button("Se connecter")

    # action du bouton
    if login_button:
        if username in users and users[username]["password"] == password:
            st.session_state.authenticated = True
            st.session_state.user = username
            st.success("Connexion réussie")
            st.experimental_rerun()  # relance le script pour afficher l'app
        else:
            st.error("Identifiants incorrects")
