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


-- report 2: List of ids, name and number of employees hired of each department 
-- that hired more employees than the mean of employees hired in 2021 for all the departments, 
-- ordered by the number of employees hired (descending).
-- Number of employees hired for each job and department

with hired_employees_by_department as (
    select 
        hired_employees.department_id, 
        departments.department as department,
        count(hired_employees.id) as number_of_employees
    from hired_employees
    left join departments on hired_employees.department_id = departments.id
    where extract(year from hired_employees.datetime) = 2021
    and name is not null and department_id is not null and job_id is not null
    group by hired_employees.department_id, departments.department
),
mean_hired_employee as (
    select avg(number_of_employees) as mean_hired_employees
    from hired_employees_by_department
)
select
    department_id as id,
    department,
    number_of_employees as hired
from hired_employees_by_department
join mean_hired_employee on true
where number_of_employees > mean_hired_employees
order by hired_employees_by_department.number_of_employees desc;