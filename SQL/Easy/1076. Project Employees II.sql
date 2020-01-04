/* Write your PL/SQL query statement below */

select t2.project_id from 
(select project_id, rank() over (order by max_employee desc) as rank from
    (select project_id, count(employee_id) as max_employee from Project
     group by project_id) t1) t2
where t2.rank=1


# Write your MySQL query statement below
select t3.project_id from
(select project_id, count(employee_id) as max_employee from Project 
group by project_id) t3
join 
    (select max(max_employee) as max_employee from 
    (select project_id, count(employee_id) as max_employee from Project
     group by project_id)t1) t2
on t3.max_employee = t2.max_employee