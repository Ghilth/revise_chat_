import streamlit as st
from bot_ask import ask  # Fonction qui interroge le modèle RAG

# Configuration de la page
st.set_page_config(
    page_title="Révise tes cours",
    page_icon="📚",
    layout="centered"
)

# Styles personnalisés
st.markdown("""
    <style>
        body {
            background-color: #eef2f3;
        }
        .stTextArea textarea {
            border: 2px solid #4a90e2;
            border-radius: 10px;
            font-size: 16px;
            padding: 10px;
        }
        .stButton button {
            background-color: #4a90e2;
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #357abd;
        }
        .response-box {
            background-color: #d0e7ff;
            padding: 15px;
            border-radius: 10px;
            font-size: 16px;
            margin: 10px 0;
        }
        .user-box {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            font-size: 16px;
            margin: 10px 0;
            border: 1px solid #4a90e2;
        }
    </style>
""", unsafe_allow_html=True)

# Titre et introduction
st.title("📚 EduBot")
st.subheader("💡 Pose-moi tes questions et je t'aiderai à comprendre tes cours !")

# Entrée utilisateur
user_input = st.text_area(
    "Pose ta question ici 👇",
    placeholder="Exemple : Peux-tu expliquer c'est quoi un algorithme ?"
)

# Interaction avec l'assistant
if st.button("Envoyer"):
    if user_input.strip():
        with st.spinner("EduBot réfléchit..."):
            response = ask(user_input)
        st.markdown(f'<div class="user-box">👨‍🎓 {user_input}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="response-box">🤖 {response}</div>', unsafe_allow_html=True)
    else:
        st.warning("Veuillez entrer une question avant d'envoyer.")



# Note pédagogique
st.markdown("""
    ---
    🎯 **Conseil** : Pose des questions précises pour des réponses plus détaillées.
""")
