# Demo 1

--- Demo 1: Introduction to Models (No Agent) ---
This demo shows how to use an LLM to generate SQL queries based on a schema.
The queries are NOT executed.

System Message:

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
            
User Message:
Which customers have the most orders? Provide their names and the number of orders.

Invoking the model to generate SQL query...

Generated SQL Query:
```sql
SELECT c.name, COUNT(o.order_id) AS number_of_orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY number_of_orders DESC;
```
