import streamlit as st

users = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "viewer"
    }
}


def login():

    st.title("Connexion")

    username = st.text_input("Utilisateur")
    password = st.text_input("Mot de passe", type="password")

    if st.button("Connexion"):

        if username in users and users[username]["password"] == password:

            st.session_state.authenticated = True
            st.session_state.user = username
            st.session_state.role = users[username]["role"]

            st.success("Connexion réussie")
            st.rerun()

        else:
            st.error("Identifiants incorrects")
