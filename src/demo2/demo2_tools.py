"""Demo 2: Introduction to Tools."""
import logging
from typing import List

import duckdb
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import BaseTool, tool
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ToolCall,
    ToolMessage,
)

load_dotenv()

logging.basicConfig(level=logging.INFO)

# Define some tools to use
db = duckdb.connect("demo2.duckdb", read_only=True)


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

model = init_chat_model("gpt-5-mini", temperature=0)
tools: List[BaseTool] = [list_duckdb_tables, get_table_schema, query_duckdb]
model = model.bind_tools(tools)

if __name__ == "__main__":
    logging.info("--- Demo 2: Introduction to Tools (No Agent) ---")

    # Documentation for Messages: https://reference.langchain.com/python/langchain/messages/
    system = SystemMessage(
        """You are a helpful assistant that interacts with a DuckDB SQL database.
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
            """
    )
    user = HumanMessage(
        "Which customers have the most orders? Provide their names and the number of orders."
    )

    messages = [system, user]

    for message in messages:
        logging.info(message)

    # Start Tool Calling Loop
    while True:
        logging.info(
            "*******************************************\nInvoking the model...\n*******************************************"
        )
        # Documentation: https://docs.langchain.com/oss/python/langchain/models#invoke
        ai_msg: AIMessage = model.invoke(messages)
        messages.append(ai_msg)
        logging.info(ai_msg)
        # logging.info("\nTool Calls:")
        # logging.info(ai_msg.tool_calls)
        # Check if user wants to stop using the console
        human_check: str = input("Type 'exit' to stop, or press Enter to continue: ")
        if human_check.lower() == "exit":
            break

        if ai_msg.tool_calls:
            tool_call: ToolCall
            for tool_call in ai_msg.tool_calls:
                # [
                #     {
                #         'name': 'list_duckdb_tables',
                #         'args': {},
                #         'id': 'call_1G3nkEiSVT1BV5RzPbCmjSPX',
                #         'type': 'tool_call'
                #     }
                # ]
                logging.info(
                    f"Invoking tool: {tool_call['name']} with args: {tool_call['args']}"
                )
                for tool in tools:
                    if tool.name == tool_call["name"]:
                        tool_output = tool.invoke(input=tool_call["args"])
                        logging.info(f"Tool output: {tool_output}")
                        messages.append(
                            ToolMessage(
                                content=str(tool_output), tool_call_id=tool_call["id"]
                            )
                        )
        else:
            logging.info("No tool calls. Ending interaction.")
            break
