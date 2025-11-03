
Run command: `uv run demo2_tools.py`

Example output:
```
--- Demo 2: Introduction to Tools (No Agent) ---
================================ System Message ================================


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
            
================================ Human Message =================================

Which customers have the most orders? Provide their names and the number of orders.
*******************************************
Invoking the model...
*******************************************
================================== Ai Message ==================================
Tool Calls:
  list_duckdb_tables (call_lCmdwtS7MYUxbTjWmjUaClww)
 Call ID: call_lCmdwtS7MYUxbTjWmjUaClww
  Args:
Type 'exit' to stop, or press Enter to continue: 
Invoking tool: list_duckdb_tables with args: {}
Tool output: ['customers', 'orders', 'products']
*******************************************
Invoking the model...
*******************************************
================================== Ai Message ==================================
Tool Calls:
  get_table_schema (call_MBdekzWwu3e51bOgUQDu6i4G)
 Call ID: call_MBdekzWwu3e51bOgUQDu6i4G
  Args:
    table_name: customers
Type 'exit' to stop, or press Enter to continue: 
Invoking tool: get_table_schema with args: {'table_name': 'customers'}
Tool output: customer_id INTEGER
name VARCHAR
email VARCHAR
*******************************************
Invoking the model...
*******************************************
================================== Ai Message ==================================
Tool Calls:
  get_table_schema (call_zlEdDahxKMpIFKGxunkRChHe)
 Call ID: call_zlEdDahxKMpIFKGxunkRChHe
  Args:
    table_name: orders
Type 'exit' to stop, or press Enter to continue: 
Invoking tool: get_table_schema with args: {'table_name': 'orders'}
Tool output: order_id INTEGER
customer_id INTEGER
product_id INTEGER
quantity INTEGER
order_date TIMESTAMP
*******************************************
Invoking the model...
*******************************************
================================== Ai Message ==================================
Tool Calls:
  get_table_schema (call_CmiVNxZt0RZ6NddNdm1tKs2y)
 Call ID: call_CmiVNxZt0RZ6NddNdm1tKs2y
  Args:
    table_name: products
Type 'exit' to stop, or press Enter to continue: 
Invoking tool: get_table_schema with args: {'table_name': 'products'}
Tool output: product_id INTEGER
name VARCHAR
price DOUBLE
*******************************************
Invoking the model...
*******************************************
================================== Ai Message ==================================
Tool Calls:
  query_duckdb (call_pzZLAlgZoYIMz62Fq4l02aEs)
 Call ID: call_pzZLAlgZoYIMz62Fq4l02aEs
  Args:
    query: SELECT c.name, COUNT(*) AS order_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name
ORDER BY order_count DESC, c.name
LIMIT 5;
Type 'exit' to stop, or press Enter to continue: 
Invoking tool: query_duckdb with args: {'query': 'SELECT c.name, COUNT(*) AS order_count\nFROM customers c\nJOIN orders o ON c.customer_id = o.customer_id\nGROUP BY c.name\nORDER BY order_count DESC, c.name\nLIMIT 5;'}
Tool output: [('Alice Johnson', 2), ('Bob Smith', 1), ('Carol Davis', 1), ('David Lee', 1), ('Eve Martinez', 1)]
*******************************************
Invoking the model...
*******************************************
================================== Ai Message ==================================

Here are the customers with the most orders (name and number of orders):

- Alice Johnson — 2 orders
- Bob Smith — 1 order
- Carol Davis — 1 order
- David Lee — 1 order
- Eve Martinez — 1 order

If you want all customers (not limited to 5) or customers tied for the top count only, I can run a different query.
Type 'exit' to stop, or press Enter to continue: 
No tool calls. Ending interaction.
```