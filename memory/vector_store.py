import os
from langchain.vectorstores import FAISS  # type: ignore
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

vector_db = FAISS(embeddings_function=embeddings, index=None)

def add_documents(docs):
    vector_db.add_documents(docs)

def search(query, k=5):
    return vector_db.similarity_search(query, k=k)
