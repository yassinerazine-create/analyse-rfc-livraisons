import streamlit as st

# dictionnaire simple d'utilisateurs
USERS = {
    "admin": "admin",
    "user": "user"
}

def login():
    st.title("Connexion")
    
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    
    if st.button("Se connecter"):
        if username in USERS and password == USERS[username]:
            st.session_state.authenticated = True
            st.session_state.user = username
            st.success(f"Bienvenue {username} !")
            st.experimental_rerun()
        else:
            st.error("Identifiants incorrects")
