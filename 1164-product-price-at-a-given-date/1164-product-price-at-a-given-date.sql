# Write your MySQL query statement below
SELECT DISTINCT sub.product_id,
CASE
    WHEN sub.max_dates IS NULL THEN 10
    ELSE sub.new_price
END AS "price"
 FROM (
WITH 
filtered_products AS  (
    SELECT * FROM Products WHERE change_Date <= "2019-08-16"
)
SELECT p.product_id, p.new_price,p.change_date,
MAX(fp.change_date) OVER(PARTITION BY p.product_id) AS max_dates
FROM Products AS p
LEFT JOIN filtered_products AS fp
ON p.product_id = fp.product_id AND p.change_date = fp.change_date 
GROUP BY p.product_id,p.change_date
ORDER BY p.product_id ) AS sub
WHERE sub.change_date = sub.max_dates OR sub.max_dates IS NULL;
