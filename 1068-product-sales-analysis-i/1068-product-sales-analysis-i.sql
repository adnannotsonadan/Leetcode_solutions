-- Write your PostgreSQL query statement below

-- SELECT p.product_name, year, price
-- FROM Sales
-- JOIN Product p
--     USING (product_id);

select Product.product_name,Sales.year,Sales.price
from Product
right join Sales
on Product.product_id=Sales.product_id;