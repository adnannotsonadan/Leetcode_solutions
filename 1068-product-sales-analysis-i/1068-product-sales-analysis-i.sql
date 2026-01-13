-- Write your PostgreSQL query statement below

SELECT p.product_name, year, price
FROM Sales
JOIN Product p
    USING (product_id);