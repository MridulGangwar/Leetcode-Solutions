# Write your MySQL query statement below

select e.employee_id , t1.team_size from Employee e join
(select team_id, count(*) as team_size from Employee group by team_id)t1
on e.team_id = t1.team_id