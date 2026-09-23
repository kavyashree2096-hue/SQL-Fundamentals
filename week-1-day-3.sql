-- ==========================================
-- SQL AGGREGATIONS - WEEK 1 DAY 3
-- ==========================================

-- Delete old table
DROP TABLE IF EXISTS orders;


-- Create new Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    order_date DATE,
    region VARCHAR(50),
    category VARCHAR(50),
    product VARCHAR(50),
    quantity INT,
    order_amount DECIMAL(10,2)
);


-- Insert new data
INSERT INTO orders
(order_id, order_date, region, category, product, quantity, order_amount)
VALUES
(1, '2026-09-01', 'North', 'Electronics', 'Laptop', 2, 90000),
(2, '2026-09-02', 'South', 'Clothing', 'Shirt', 10, 15000),
(3, '2026-09-03', 'East', 'Electronics', 'Mobile', 5, 75000),
(4, '2026-09-05', 'West', 'Furniture', 'Chair', 8, 24000),
(5, '2026-09-07', 'North', 'Clothing', 'Jeans', 6, 18000),
(6, '2026-09-10', 'South', 'Electronics', 'Tablet', 4, 48000),
(7, '2026-09-12', 'East', 'Furniture', 'Table', 3, 21000),
(8, '2026-09-15', 'West', 'Electronics', 'Headphones', 10, 20000),
(9, '2026-09-18', 'North', 'Electronics', 'Monitor', 4, 60000),
(10, '2026-09-20', 'South', 'Clothing', 'Shoes', 5, 25000),
(11, '2026-09-22', 'East', 'Electronics', 'Keyboard', 8, 16000),
(12, '2026-09-25', 'West', 'Furniture', 'Desk', 2, 30000);


-- 1. COUNT
SELECT COUNT(*) AS total_orders
FROM orders;


-- 2. SUM
SELECT SUM(order_amount) AS total_revenue
FROM orders;


-- 3. AVG
SELECT AVG(order_amount) AS average_order_amount
FROM orders;


-- 4. MAX
SELECT MAX(order_amount) AS highest_order
FROM orders;


-- 5. MIN
SELECT MIN(order_amount) AS lowest_order
FROM orders;


-- 6. GROUP BY REGION
SELECT
    region,
    SUM(order_amount) AS total_sales
FROM orders
GROUP BY region;


-- 7. GROUP BY CATEGORY
SELECT
    category,
    SUM(order_amount) AS total_sales
FROM orders
GROUP BY category;


-- 8. GROUP BY MONTH
SELECT
    FORMAT(order_date, 'yyyy-MM') AS month,
    SUM(order_amount) AS total_sales
FROM orders
GROUP BY FORMAT(order_date, 'yyyy-MM')
ORDER BY month;


-- 9. HAVING
SELECT
    region,
    SUM(order_amount) AS total_sales
FROM orders
GROUP BY region
HAVING SUM(order_amount) > 50000;


-- 10. WINDOW FUNCTION
SELECT
    order_id,
    region,
    order_amount,
    SUM(order_amount) OVER(PARTITION BY region) AS region_total_sales
FROM orders;