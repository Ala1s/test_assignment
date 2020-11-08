SELECT DISTINCT department
FROM employees
GROUP BY department
HAVING SUM(CASE WHEN position='Software Developer' THEN 1 ELSE 0 END) < 5
