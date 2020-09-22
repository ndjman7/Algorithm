-- Write your MySQL query statement below
SELECT ae.Name as Employee
FROM Employee ae
JOIN Employee be ON ae.ManagerId = be.Id
Where ae.ManagerId IN (
    SELECT ManagerId
    FROM Employee
    WHERE ManagerId is not null
) AND ae.Salary > be.Salary

