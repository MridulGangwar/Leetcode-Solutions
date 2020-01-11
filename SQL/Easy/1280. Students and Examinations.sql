# Write your MySQL query statement below
select t1.student_id, t1.student_name, t1.subject_name, COALESCE(t2.attended_exams,0) as attended_exams from
(select student_id, student_name, subject_name from students, Subjects) t1
left join
(select student_id, subject_name, count(*) as attended_exams from Examinations
group by 1,2) as t2
on t1.student_id = t2.student_id 
and t1.subject_name = t2.subject_name
order by student_id,subject_name