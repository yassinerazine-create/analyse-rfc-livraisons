import streamlit as st

users = {
    "admin": "admin123",
    "user": "user123"
}

def login():

    st.title("Authentification")

    username = st.text_input("Utilisateur :")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Connexion"):

        if username in users and users[username] == password:
            st.session_state.authenticated = True
            st.success("Connexion réussie")
            st.rerun()

        else:
            st.error("Identifiants incorrects")
