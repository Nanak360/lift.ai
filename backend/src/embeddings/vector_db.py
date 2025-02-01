import time
from uuid import uuid4
from langchain_ollama import OllamaEmbeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from constants import PINECONE_VECTOR_DB_INDEX_NAME
import os
import json
from dotenv import load_dotenv

load_dotenv(verbose=True)

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
INDEX_NAME = PINECONE_VECTOR_DB_INDEX_NAME

pc = Pinecone(api_key=PINECONE_API_KEY)

def get_vector_store():
    try:
        embeddings = OllamaEmbeddings(
            model="llama3.2",
        )
        existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

        if INDEX_NAME not in existing_indexes:
            pc.create_index(
                name=INDEX_NAME,
                dimension=3072,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
            while not pc.describe_index(INDEX_NAME).status["ready"]:
                time.sleep(1)

        index = pc.Index(INDEX_NAME)
        vector_store = PineconeVectorStore(
            embedding=embeddings,
            index=index
        )
        print("Vector store created successfully")
    except Exception as e:
        raise Exception(f"Error: {str(e)}")
    return vector_store

def store_vectors(documents):
    print("Storing embeddings in vector database")
    try:
        vector_store = get_vector_store()
        vector_store.add_documents(documents, ids=[str(uuid4()) for _ in range(len(documents))])
        print("Storing embeddings in vector database")
        return "Embeddings stored successfully"
    except Exception as e:
        raise Exception(f"Error: {str(e)}")

def retrieve_embedding(query):
    try:
        vector_store = get_vector_store()
        results = vector_store.similarity_search(query, k=1)
        print(f"Results: {results}")
        if results:
            return results[0].page_content
        else:
            return None
    except Exception as e:
        raise Exception(f"Error: {str(e)}")
