import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

# Initialize the OpenAI model
# Ensure OPENAI_API_KEY is set in your .env file
model = ChatOpenAI(model="gpt-4o", temperature=0)

if __name__ == "__main__":
    print("--- Demo 1: Introduction to Models (No Agent) ---")
    print("This demo shows how to use an LLM to generate SQL queries based on a schema.")
    print("The queries are NOT executed.\n")

    system = SystemMessage(f"""
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
    print("\nInvoking the model to generate SQL query...\n")
    response = model.invoke(messages)
    print(f"Generated SQL Query:\n{response.content}")
