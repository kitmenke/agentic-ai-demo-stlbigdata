from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from chromadb.utils.batch_utils import create_batches
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="demo3_duckdb_docs",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
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

from langchain.agents import create_agent


tools = [search_duckdb_documentation]
# If desired, specify custom instructions
prompt = (
    "You have access to a tool that searches the DuckDB documentation. "
    "Use the tool to help answer user queries."
)
agent = create_agent(model, tools, system_prompt=prompt)

query = (
    "How to read 'example.csv' file into DuckDB?\n\n"
    "Once you get the answer, what are some common parameters used in the function?"
)

for event in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    event["messages"][-1].pretty_print()