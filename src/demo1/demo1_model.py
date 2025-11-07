"""Demo 1: Introduction to Models (No Agent)."""
import logging

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

logging.basicConfig(level=logging.INFO)

# Initialize the OpenAI model
# Ensure OPENAI_API_KEY is set in your .env file
# Documentation: https://reference.langchain.com/python/langchain/models/
model = ChatOpenAI(model="gpt-4o", temperature=0)

if __name__ == "__main__":
    logging.info("--- Demo 1: Introduction to Models (No Agent) ---")
    logging.info(
        "This demo shows how to use an LLM to generate SQL queries based on a schema."
    )
    logging.info("The queries are NOT executed.\n")

    # Documentation for Messages: https://reference.langchain.com/python/langchain/messages/
    system = SystemMessage(
        """
You are a helpful assistant that generates SQL queries based on user questions and a given database schema.
Do NOT execute the query. Only provide the SQL query.
Here is the database schema:
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
            """
    )
    user = HumanMessage(
        "Which customers have the most orders? Provide their names and the number of orders."
    )

    messages = [system, user]
    logging.info("System Message:")
    logging.info(system.content)
    logging.info("User Message:")
    logging.info(user.content)
    logging.info("\nInvoking the model to generate SQL query...\n")
    # Documentation: https://docs.langchain.com/oss/python/langchain/models#invoke
    response = model.invoke(messages)
    logging.info(f"Generated SQL Query:\n{response.content}")
    # Streaming response
    # for chunk in model.stream(messages):
    #     logging.info(chunk.text, end="|", flush=True)