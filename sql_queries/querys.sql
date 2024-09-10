-- report 1: Number of employees hired for each job and department 
-- in 2021 divided by quarter. 
-- The table must be ordered alphabetically by department and job.

with job_list as (
    select 
        departments.department as department,
        jobs.job as job,
        extract(quarter from hired_employees.datetime) as quarter,
        count(hired_employees.id) as number_of_employees
    from hired_employees
    left join departments on hired_employees.department_id = departments.id
    left join jobs on hired_employees.job_id = jobs.id
    where extract(year from hired_employees.datetime) = 2021
    and name is not null and department_id is not null and job_id is not null
    group by departments.department, jobs.job, quarter
)
select
    department, 
    job, 
    sum(case when quarter = 1 then number_of_employees else 0 end) as Q1,
    sum(case when quarter = 2 then number_of_employees else 0 end) as Q2,
    sum(case when quarter = 3 then number_of_employees else 0 end) as Q3,
    sum(case when quarter = 4 then number_of_employees else 0 end) as Q4
from job_list 
group by department, job
order by department, job;

