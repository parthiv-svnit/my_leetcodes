SELECT name FROM Employee
WHERE id IN 
(
    SELECT managerId 
    FROM Employee 
    GROUP BY ManagerId HAVING count(*) > 4);