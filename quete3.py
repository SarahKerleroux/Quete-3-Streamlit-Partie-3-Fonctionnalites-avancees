import pandas as pd
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    100, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
      st.title("Bienvenue sur ma page")
      st.markdown("![Alt Text](http://www.animaniacs.fr/wp-content/uploads/2013/08/catgriffe.gif)")
 
def album():
    st.title("La fashion week des chats")
    st.write("Collection automne-hiver 2024")
    image1 = "https://img.freepik.com/photos-gratuite/portrait-chats-anthropomorphes-vetus-vetements-humains_23-2151107479.jpg"
    image2 = "https://img.freepik.com/photos-premium/chat-porte-lunettes-soleil-costume-fond-rose_974206-4829.jpg"
    image3 = "https://img.freepik.com/photos-gratuite/portrait-chats-anthropomorphes-vetus-vetements-humains_23-2151107481.jpg"
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(image1, caption="Image 1", use_container_width=True)
    with col2:
        st.image(image2, caption="Image 2", use_container_width=True)
    with col3:
        st.image(image3, caption="Image 3", use_container_width=True)
    with col2:
        st.markdown(
    """
    <style>
    video {
        width: 200px !important;
        height: auto !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
    st.video("video_defile.mp4")

if st.session_state["authentication_status"]:
    # Création du menu qui va afficher les choix qui se trouvent dans la variable options
    with st.sidebar:
        selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Album"]
        )
    print(selection)
    if selection == "Accueil":
        accueil()
    elif selection == "Album":
        album()
  # Le bouton de déconnexion
    authenticator.logout("Déconnexion")
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')
