import streamlit as st
from bot_ask import ask  

# Configuration de la page
st.set_page_config(
    page_title="VoixLibre - Assistance",
    page_icon="💬",
    layout="centered"
)

# Appliquer un style personnalisé
st.markdown(""" 
    <style>
        body {
            background-color: #f2e8d3; /* Fond beige clair */
        }
        .stTextArea textarea {
            border: 2px solid #f2c277; /* Bordure assortie aux bulles */
            border-radius: 10px;
            font-size: 16px;
            padding: 10px;
        }
        .stButton button {
            background-color: #f2c277; /* Bouton assorti */
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            right: 10px;
        }
        .stButton button:hover {
            background-color: #e5a960; /* Couleur plus foncée au survol */
        }
        .response-box {
            background-color: #e5a960; /* Couleur de la bulle Baké */
            padding: 15px;
            border-radius: 10px;
            color: black;
            font-size: 16px;
            margin: 10px 0;
        }
        .user-box {
            background-color: #fffff; /* Couleur de la bulle utilisateur */
            padding: 15px;
            border-radius: 10px;
            color: black;
            font-size: 16px;
            margin: 10px 0;
        }
        
        /* Style pour le bouton "Dénoncer" en bas à droite */
        .denoncer-button {
            position: fixed ;
            bottom: 45px;
            right: 10%;
            background-color: #f2c277; /* Couleur du bouton */
            color: white;
            padding: 10px 25px;
            font-size: 16px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        
        }
        .denoncer-button:hover {
            background-color: #e5a960; /* Couleur au survol */
        }
    </style>
""", unsafe_allow_html=True)

# Titre de l'application
st.title("VoixLibre 💬")

# Message d'accueil
st.subheader("👋 Bienvenue, je suis Baké !")
st.markdown("""
    Je suis là pour t'écouter, te guider, et te fournir des réponses claires à tes questions sur tes droits 
    et les options disponibles face aux violences basées sur le genre.  
    Si tu cherches des conseils, n'hésite pas à me le faire savoir. Ensemble, nous trouverons des solutions. 🤝
""")

# Entrée utilisateur
user_input = st.text_area(
    "Posez votre question ici 👇",
    placeholder="Exemple : Quels sont mes droits en cas de harcèlement ?"
)

# Bouton pour envoyer la question
if st.button("Envoyer"):
    if user_input.strip():
        with st.spinner("Baké est en train d'écrire..."):
            response = ask(user_input)
        st.markdown('<div class="user-box">' + user_input + '</div>', unsafe_allow_html=True)
        st.markdown('<div class="response-box">' + response + '</div>', unsafe_allow_html=True)
    else:
        st.warning("Veuillez entrer une question avant d'envoyer.")

# Ajout d'une note de confidentialité
st.markdown("""
    ---
    🔒 **Confidentialité garantie :** Toutes vos interactions avec moi, Baké, restent strictement confidentielles.
""")

# Bouton "Dénoncer" en bas à droite
st.markdown("""
    <a href="https://voixlibre.netlify.app/denoncement" target="_blank">
        <button class="denoncer-button">Dénoncer</button>
    </a>
""", unsafe_allow_html=True)
