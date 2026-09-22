Create DATABASE SQL_JOINS_DB;
GO

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
GO

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(100)
);
GO

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(100),
    amount INT
);
GO

INSERT INTO customers VALUES
(1, 'Kavya', 'Bengaluru'),
(2, 'Rahul', 'Mysuru'),
(3, 'Ananya', 'Chennai'),
(4, 'Priya', 'Hyderabad'),
(5, 'Arjun', 'Mumbai');
GO

INSERT INTO orders VALUES
(101, 1, 'Laptop', 50000),
(102, 1, 'Mouse', 1000),
(103, 2, 'Keyboard', 2000),
(104, 3, 'Monitor', 15000),
(105, 6, 'Headphones', 3000);
GO

-- INNER JOIN
SELECT
    c.customer_name,
    c.city,
    o.product,
    o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;
GO

-- LEFT JOIN
SELECT
    c.customer_name,
    c.city,
    o.product,
    o.amount
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;
GO

-- RIGHT JOIN
SELECT
    c.customer_name,
    c.city,
    o.product,
    o.amount
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;
GO

-- FULL OUTER JOIN
SELECT
    c.customer_name,
    c.city,
    o.product,
    o.amount
FROM customers c
FULL OUTER JOIN orders o
ON c.customer_id = o.customer_id;
GO

-- SELF JOIN
SELECT
    c1.customer_name AS customer1,
    c2.customer_name AS customer2,
    c1.city
FROM customers c1
JOIN customers c2
ON c1.city = c2.city
AND c1.customer_id < c2.customer_id;
GO

-- FIND CUSTOMERS WITHOUT ORDERS
SELECT
    c.customer_id,
    c.customer_name,
    c.city
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
GO

-- FIND ORDERS WITHOUT CUSTOMERS
SELECT
    o.order_id,
    o.product,
    o.amount
FROM orders o
LEFT JOIN customers c
ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
GO

-- TOTAL ORDERS AND AMOUNT PER CUSTOMER
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.amount), 0) AS total_amount
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name;
GO