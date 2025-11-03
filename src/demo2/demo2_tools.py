import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage, ToolCall
from typing import List

import duckdb

load_dotenv()

db = duckdb.connect("demo2.duckdb", read_only=True)

# class ListDuckDBTables(BaseModel):
#     """List all tables in the duckdb database."""
#     tables: List[str] = Field(..., description="List of table names in the database.")

#     def __call__(self) -> List[str]:
#         result = db.execute("show tables").fetchall()
#         return [row[0] for row in result]

@tool
def list_duckdb_tables() -> List[str]:
    """List all tables in the duckdb database."""
    result = db.execute("show tables").fetchall()
    return [row[0] for row in result]

@tool
def get_table_schema(table_name: str) -> str:
    """Get the schema of a table in the duckdb database."""
    result = db.execute(f"describe {table_name}").fetchall()
    schema = "\n".join([f"{row[0]} {row[1]}" for row in result])
    return schema

@tool
def query_duckdb(query: str) -> List[str]:
    """Query the duckdb database."""
    result = db.execute(query).fetchall()
    return str(result)

# Initialize the OpenAI model
# Ensure OPENAI_API_KEY is set in your .env file
# Documentation: https://reference.langchain.com/python/langchain/models/
model:ChatOpenAI = ChatOpenAI(model="gpt-5", temperature=0)
model.bind_tools(
    [list_duckdb_tables, get_table_schema, query_duckdb]
)

if __name__ == "__main__":
    print("--- Demo 2: Introduction to Tools (No Agent) ---")

    # Documentation for Messages: https://reference.langchain.com/python/langchain/messages/
    system = SystemMessage(f"""
You are a helpful assistant that interacts with a DuckDB SQL database.
Given an input question, create a syntactically correct DuckDB query to run,
then look at the results of the query and return the answer. Unless the user
specifies a specific number of examples they wish to obtain, always limit your
query to at most 5 results.

You can order the results by a relevant column to return the most interesting
examples in the database. Never query for all the columns from a specific table,
only ask for the relevant columns given the question.

You MUST double check your query before executing it. If you get an error while
executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the
database.

To start you should ALWAYS look at the tables in the database to see what you
can query. Do NOT skip this step.

Then you should query the schema of the most relevant tables.
            """)
    user = HumanMessage("Which customers have the most orders? Provide their names and the number of orders.")

    messages = [
        system,
        user
    ]
    print("System Message:")
    print(system.content)
    print("User Message:")
    print(user.content)

    available_tools = {
        "list_duckdb_tables": list_duckdb_tables,
        "get_table_schema": get_table_schema,
        "query_duckdb": query_duckdb,
    }

    # Start Tool Calling Loop
    while True:
        print("\nInvoking the model...\n")
        # Documentation: https://docs.langchain.com/oss/python/langchain/models#invoke
        ai_msg: AIMessage = model.invoke(messages)
        messages.append(ai_msg)
        ai_msg.pretty_print()
        print("\nTool Calls:")
        print(ai_msg.tool_calls)
        # Check if user wants to stop using the console
        human_check:str = input("Type 'exit' to stop, or press Enter to continue: ")
        if human_check.lower() == "exit":
            break

        if ai_msg.tool_calls:
            print(f"Tool Calls:")
            for tool_call in ai_msg.tool_calls:
                print(tool_call)
                tool = available_tools[tool_call["name"]]
                tool_output = tool.invoke(tool_call["args"])
                messages.append(ToolMessage(content=str(tool_output), tool_call_id=tool_call["id"]))
        else:
            print("No tool calls. Ending interaction.")
            break