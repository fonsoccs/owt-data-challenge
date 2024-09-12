-- Active: 1726104604109@@0.0.0.0@5433@owt_data_challenge@public
-- departments
drop table if exists departments;
create table departments (
    id serial primary key,
    department varchar(100) not null
);

-- hired_employees
drop table if exists hired_employees;
create table hired_employees (
    id serial primary key,
    name varchar(100),
    datetime timestamp,
    department_id integer,
    job_id integer
);

-- jobs
drop table if exists jobs;
create table jobs (
    id serial primary key,
    job varchar(100) not null
);
