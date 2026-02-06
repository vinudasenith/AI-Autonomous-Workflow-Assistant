from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

def create_vector_store(texts):
    return FAISS.from_texts(texts, embeddings)