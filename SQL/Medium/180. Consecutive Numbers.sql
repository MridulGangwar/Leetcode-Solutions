select distinct(t1.Num) as ConsecutiveNums from Logs t1, Logs t2, Logs t3
where t2.Id=t1.Id+1 and t3.Id=t1.Id+2
and t2.Num=t1.Num and t3.Num=t1.Num