SELECT DISTINCT(name)
FROM SalesPerson s 
LEFT JOIN Orders o
    ON s.sales_id = o.sales_id
WHERE s.sales_id NOT IN (
    SELECT o2.sales_id 
    FROM Orders o2
    WHERE o2.com_id IN (
        SELECT c.com_id 
        FROM Company c
        WHERE c.name = 'RED'
    )
);