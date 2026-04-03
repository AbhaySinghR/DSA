# Write your MySQL query statement below


with cte 
as
(
select *, dense_rank() over (order by salary desc) as rnk
from Employee
)
select 
case when (select distinct salary from cte where rnk=2) is NULL then NULL
else (select distinct salary from cte where rnk=2) end SecondHighestSalary
