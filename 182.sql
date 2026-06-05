# Write your MySQL query statement below
SELECT DISTINCT e.email AS Email 
FROM Person e
WHERE (
    SELECT COUNT(*)
    FROM Person p
    WHERE p.email = e.email
) > 1;