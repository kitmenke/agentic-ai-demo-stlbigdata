"""Demo 3: RAG Agent."""
import logging
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

logging.basicConfig(level=logging.INFO)

DATA_DIR = os.getenv("DATA_DIR")

# RAG demo
# https://docs.langchain.com/oss/python/langchain/rag
# Initialize the vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="demo3_duckdb_docs",
    embedding_function=embeddings,
    persist_directory=f"{DATA_DIR}/chroma_langchain_db",  # Where to save data locally, remove if not necessary
)
model = init_chat_model("gpt-5-mini", temperature=0)


@tool(response_format="content_and_artifact")
def search_duckdb_documentation(query: str):
    """Search the DuckDB documentation and guides."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


tools = [search_duckdb_documentation]
# If desired, specify custom instructions
prompt = (
    "You have access to a tool that searches the DuckDB documentation. "
    "Use the tool to help answer user queries."
)
# https://docs.langchain.com/oss/python/langchain/agents
agent = create_agent(model, tools, system_prompt=prompt)

query = "Explain how to read a CSV file into DuckDB and provide some examples."

for event in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    logging.info(event["messages"][-1])
