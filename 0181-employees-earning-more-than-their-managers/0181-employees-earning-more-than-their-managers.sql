# Write your MySQL query statement below
WITH emp AS (
    SELECT e.name AS employee, e.salary, m.salary AS manager_salary
    FROM Employee e
    JOIN Employee m ON e.managerId = m.id
)
SELECT employee
FROM emp
WHERE salary > manager_salary;