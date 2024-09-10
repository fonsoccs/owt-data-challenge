-- departments
drop table if exists departments;
create table departments (
    id serial primary key,
    department varchar(100) not null
);

COPY departments(id, department)
FROM '/Users/alfonsolicir/_project/de-code-challenge/data_challenge_files/departments.csv' DELIMITER ',' CSV HEADER;

select * from departments;

-- hired_employees
drop table if exists hired_employees;
create table hired_employees (
    id serial primary key,
    name varchar(100),
    datetime timestamp,
    department_id integer,
    job_id integer
);

COPY hired_employees(id, name, datetime, department_id, job_id)
FROM '/Users/alfonsolicir/_project/de-code-challenge/data_challenge_files/hired_employees.csv' DELIMITER ',' CSV HEADER;

# NOTE: there are 56 rows with NULL values on key columns like name, department_id or job_id, these rows will be ignored on the results

select * from hired_employees;

-- hired_employees
drop table if exists jobs;
create table jobs (
    id serial primary key,
    job varchar(100) not null
);

COPY jobs(id, job)
FROM '/Users/alfonsolicir/_project/de-code-challenge/data_challenge_files/jobs.csv' DELIMITER ',' CSV HEADER;
