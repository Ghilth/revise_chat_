#packages
from langchain.prompts import PromptTemplate
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_mistralai.embeddings import MistralAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
import os







#load key
api_key = os.getenv("api_key")
HF_TOKEN = os.getenv("HF_TOKEN")


db = FAISS.load_local("faiss_revise_bdv", HuggingFaceEmbeddings(model_name='sentence-transformers/multi-qa-MiniLM-L6-cos-v1'),
                          allow_dangerous_deserialization=True
)



# Connect query to FAISS index using a retriever
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={'k': 10},
)


# Define LLM
model = ChatMistralAI( model ="mistral-large-latest",
                      temperature =0,
                      maxRetries =2,
                      mistral_api_key=api_key)



template = """

Tu es EduBot, conçu pour aider les étudiants dans trois matières uniquement :  
📌 **Algorithmique**  
📌 **Analyse**  
📌 **Programmation**  

Si une question ne concerne pas l’une de ces trois matières, indique gentiment que tu ne peux traiter que ces domaines.  

### **Objectifs** :
1. **Clarifier la demande** : Reformule si nécessaire pour t'assurer que la question concerne bien l’une des matières.  
2. **Expliquer avec pédagogie** : Fournis une réponse détaillée, illustrée par des exemples et analogies adaptées.  
3. **Encourager la réflexion** : Pose des questions ouvertes pour inciter l’étudiant à approfondir son raisonnement.  
4. **Proposer des ressources complémentaires** : Suggère des lectures, exercices ou supports pertinents.  

Tu adoptes une attitude bienveillante, patiente et engageante pour créer un environnement d’apprentissage motivant.  

---


**Contexte** : {context}

**Voici la question** : {input}

**Réponse** :
"""

prompt = PromptTemplate(
        template=template,
        input_variables=['input']
)

#Chain LLM, prompt and retriever
combine_docs_chain = create_stuff_documents_chain(model, prompt)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)


#Let's write a function to retrieve with llm

def ask(question: str):
  response = retrieval_chain.invoke({"input": question})
  if response:
    return response['answer']
  else:
    return "Veuillez poser une autre question."
  



print(ask("Explique moi le tri à bulles"))

