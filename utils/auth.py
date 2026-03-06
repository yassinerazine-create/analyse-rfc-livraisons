import streamlit as st

users = {
    "admin": "admin123"
}

def login():

    st.title("Connexion")

    user = st.text_input("Utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):

        if user in users and users[user] == password:
            st.session_state.authenticated = True
            st.rerun()

        else:
            st.error("Identifiants incorrects")
