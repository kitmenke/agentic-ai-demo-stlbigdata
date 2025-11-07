"""Demo 3: Query for RAG."""
import logging
import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

logging.basicConfig(level=logging.INFO)

DATA_DIR = os.getenv("DATA_DIR")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="demo3_duckdb_docs",
    embedding_function=embeddings,
    persist_directory=f"{DATA_DIR}/chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

query = "read_csv parameters"
retrieved_docs = vector_store.similarity_search(query, k=3)
for doc in retrieved_docs:
    logging.info("\n\n-------------------------------------------------------")
    logging.info(f"Source: {doc.metadata}\nContent: {doc.page_content}\n")