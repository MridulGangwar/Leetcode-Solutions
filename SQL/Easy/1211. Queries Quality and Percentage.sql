# Write your MySQL query statement below
select t1.query_name, round(avg(qua),2) as quality, 
       COALESCE(round(sum(case when t1.rating<3 THEN 1 end)/count(*) * 100,2),0) as poor_query_percentage 
from
(select query_name, rating, rating/position as qua from Queries) t1
group by t1.query_name