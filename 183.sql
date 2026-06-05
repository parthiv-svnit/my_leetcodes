# Write your MySQL query statement below
SELECT e.name AS Customers FROM Customers e
WHERE (
    SELECT COUNT(*) 
    FROM Orders p
    WHERE p.customerId = e.id
) = 0;