# this configure the information of the entities used by the endpoints
entity_config = {
    "departments": {
        "table_name": "departments",
        "columns": ["id", "department"],
        "filename": "departments.csv",
        "file_regex": r'^departments\.csv$'
    },
    "jobs": {
        "table_name": "jobs",
        "columns": ["id", "job"],
        "filename": "jobs.csv",
        "file_regex": r'^jobs\.csv$'
    },
    "employees": {
        "table_name": "hired_employees",
        "columns": ["id", "name", "datetime", "department_id", "job_id"],
        "filename": "hired_employees.csv",
        "file_regex": r'^hired_employees\.csv$'
    },
}

db_config = {
    "dbname": "owt_data_challenge",
    "user": "postgres",
    "password": "mysecretpassword",
    "host": "0.0.0.0",
    "port": "5433"
}


