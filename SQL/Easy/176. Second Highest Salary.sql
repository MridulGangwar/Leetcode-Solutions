# Write your MySQL query statement below

select max(Salary) as SecondHighestSalary from Employee t1
where t1.Salary < (select max(salary) from Employee)