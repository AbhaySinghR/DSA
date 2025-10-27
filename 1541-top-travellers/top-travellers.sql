# Write your MySQL query statement below

select name, travelled_distance
from
(
select 
u.id,u.name, coalesce(sum(distance),0) as travelled_distance
from users u
left join rides r on u.id=r.user_id 
group by 1,2
order by travelled_distance desc, u.name asc
) as n