-- SQL SUBQUERIES & CTEs
-- Week 1 - Day 4

-- 1. Create table

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    region VARCHAR(50),
    product VARCHAR(50),
    sales_amount DECIMAL(10,2)
);


-- 2. Insert sample data

INSERT INTO sales
(sale_id, employee_name, region, product, sales_amount)
VALUES
(1, 'Kavya', 'South', 'Laptop', 65000),
(2, 'Rahul', 'South', 'Mobile', 45000),
(3, 'Ananya', 'North', 'Laptop', 75000),
(4, 'Arjun', 'North', 'Mobile', 50000),
(5, 'Sneha', 'East', 'Laptop', 85000),
(6, 'Ravi', 'East', 'Tablet', 40000),
(7, 'Priya', 'West', 'Laptop', 70000),
(8, 'Kiran', 'West', 'Mobile', 55000);


-- 3. Display all sales

SELECT *
FROM sales;


-- 4. Non-correlated subquery
-- Find sales above the average sales

SELECT *
FROM sales
WHERE sales_amount > (
    SELECT AVG(sales_amount)
    FROM sales
);


-- 5. Correlated subquery
-- Find the top performer in each region

SELECT s1.*
FROM sales s1
WHERE s1.sales_amount = (
    SELECT MAX(s2.sales_amount)
    FROM sales s2
    WHERE s2.region = s1.region
);


-- 6. Rewrite nested subquery using CTE
-- Find sales above average

WITH avg_sales AS (
    SELECT AVG(sales_amount) AS average_sales
    FROM sales
)
SELECT *
FROM sales
WHERE sales_amount > (
    SELECT average_sales
    FROM avg_sales
);


-- 7. Chain two CTEs
-- Find regions whose total sales are above
-- the average regional sales

WITH region_sales AS (
    SELECT
        region,
        SUM(sales_amount) AS total_sales
    FROM sales
    GROUP BY region
),
average_region_sales AS (
    SELECT
        AVG(total_sales) AS avg_sales
    FROM region_sales
)
SELECT *
FROM region_sales
WHERE total_sales > (
    SELECT avg_sales
    FROM average_region_sales
);