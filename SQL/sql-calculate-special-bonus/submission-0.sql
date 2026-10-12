-- Write your query below
SELECT employee_id,
    CASE
        WHEN employee_id % 2 = 1 and not name LIKE 'M%' THEN salary
        ELSE 0
    END AS bonus
FROM employees 
GROUP BY employee_id;