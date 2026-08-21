SELECT x, y, z, 
    CASE
        WHEN x + y > z
        AND x + z > y
        AND y + z > X
        THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;