-- departments
COPY departments(id, department)
FROM '/Users/fonsoccs/_project/data_challenge_files/departments.csv' DELIMITER ',' CSV HEADER;

select * from departments;

-- jobs
COPY jobs(id, job)
FROM '/Users/fonsoccs/_project/data_challenge_files/jobs.csv' DELIMITER ',' CSV HEADER;

select * from jobs;

-- hired_employees
COPY hired_employees(id, name, datetime, department_id, job_id)
FROM '/Users/fonsoccs/_project/data_challenge_files/hired_employees.csv' DELIMITER ',' CSV HEADER;

# NOTE: there are 56 rows with NULL values on key columns like name, department_id or job_id, these rows will be ignored on the results

select * from hired_employees;
