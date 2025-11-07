import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_chroma import Chroma
from chromadb.utils.batch_utils import create_batches
from dotenv import load_dotenv
load_dotenv()

DATA_DIR = os.getenv("DATA_DIR")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="demo3_duckdb_docs",
    embedding_function=embeddings,
    persist_directory=f"{DATA_DIR}/chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

# Documentation: https://docs.langchain.com/oss/python/langchain/retrieval#document_loaders

filename = f"{DATA_DIR}/duckdb-docs.md"
with open(filename, 'r') as f:
    content = f.read()

document = Document(
    page_content=content, metadata={"source": filename}
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=200,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)
all_splits = text_splitter.split_documents([document])
print(f"Split documentation into {len(all_splits)} sub-documents.")


# Split the documents into smaller batches
batch_size = 5461  # Set to the maximum allowed batch size
for i in range(0, len(all_splits), batch_size):
    batch = all_splits[i:i + batch_size]
    document_ids = vector_store.add_documents(documents=batch)

print(document_ids[:3])  # Print the first 3 document IDs