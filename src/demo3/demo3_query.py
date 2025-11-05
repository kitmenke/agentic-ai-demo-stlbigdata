from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from chromadb.utils.batch_utils import create_batches
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="demo3_duckdb_docs",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

query = "read_csv parameters"
retrieved_docs = vector_store.similarity_search(query, k=3)
for doc in retrieved_docs:
    print("\n\n-------------------------------------------------------")
    print(f"Source: {doc.metadata}\nContent: {doc.page_content}\n")
  