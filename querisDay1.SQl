CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    product VARCHAR(100),
    category VARCHAR(50),
    city VARCHAR(50),
    quantity INT,
    amount DECIMAL(10,2),
    sale_date DATE,
    salesperson VARCHAR(100)
);
INSERT INTO sales
(sale_id, customer_name, product, category, city, quantity, amount, sale_date, salesperson)
VALUES
(1, 'Kavya', 'Laptop', 'Electronics', 'Bengaluru', 1, 55000, '2026-01-10', 'Rahul'),
(2, 'Ananya', 'Mouse', 'Electronics', 'Mysuru', 2, 1200, '2026-01-12', 'Priya'),
(3, 'Rahul', 'Keyboard', 'Electronics', 'Bengaluru', 1, 2500, '2026-01-15', 'Arjun'),
(4, 'Sneha', 'Chair', 'Furniture', 'Chennai', 2, 8000, '2026-01-18', 'Priya'),
(5, 'Arjun', 'Desk', 'Furniture', 'Bengaluru', 1, 12000, '2026-01-20', 'Rahul'),
(6, 'Pooja', 'Monitor', 'Electronics', 'Hyderabad', 1, 15000, '2026-01-22', 'Arjun'),
(7, 'Riya', 'Headphones', 'Electronics', 'Mysuru', 3, 4500, '2026-01-25', 'Priya'),
(8, 'Vikram', 'Notebook', 'Stationery', 'Bengaluru', 5, 750, '2026-01-27', 'Rahul'),
(9, 'Megha', 'Pen', 'Stationery', 'Chennai', 10, 500, '2026-01-29', 'Arjun'),
(10, 'Aman', 'Printer', 'Electronics', 'Hyderabad', 1, 18000, '2026-02-02', 'Priya');
SELECT * FROM sales;
SELECT * FROM sales WHERE amount > 10000;
SELECT * FROM sales WHERE category = 'Electronics' AND city = 'Bengaluru';
SELECT *
FROM sales
WHERE city = 'Bengaluru'
OR city = 'Mysuru';
SELECT *
FROM sales
WHERE NOT city = 'Bengaluru';
SELECT *
FROM sales
WHERE customer_name LIKE 'A%';
SELECT *
FROM sales
WHERE city IN ('Bengaluru', 'Chennai', 'Hyderabad');
SELECT *
FROM sales
WHERE amount BETWEEN 5000 AND 20000;
UPDATE sales
SET salesperson = NULL
WHERE sale_id = 10;
SELECT *
FROM sales
WHERE salesperson IS NULL;
SELECT *
FROM sales
WHERE category = 'Electronics'
AND amount > 10000
AND city IN ('Bengaluru', 'Hyderabad');