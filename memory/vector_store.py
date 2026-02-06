import os
import faiss
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

dim = len(embeddings.embed_query("test query"))

index = faiss.IndexFlatL2(dim)

vector_db = FAISS(embedding_function=embeddings, index=index, docstore=InMemoryDocstore({}), index_to_docstore_id={})

def add_documents(docs):
    vector_db.add_documents(docs)

def search(query, k=5):
    return vector_db.similarity_search(query, k=k)
