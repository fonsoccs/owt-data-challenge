# Project Title: owt-data-challenge

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction
This is a simple project to demostrate how to load CSV files to a database using FastAPI framework.

## Requirements
Detailed explanation of the project requirements:
- Python 3.8+
- PostgreSQL database
- FastAPI framework

For additional python requierements refer to requirements.txt file on the root of the project

### Section 1: API
In the context of a DB migration with 3 different tables (departments, jobs, employees), create a local REST API that must:
1. Receive historical data from CSV files
2. Upload these files to the new DB
3. Be able to insert batch transactions (1 up to 1000 rows) with one request

### Section 2: SQL
You need to explore the data that was inserted in the previous section. The stakeholders ask for some specific metrics they need. You should create an end-point for each requirement.

## Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```
2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Start the FastAPI server:
    ```sh
    uvicorn app.main:app --reload
    ```
2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints
### Upload CSV File
- **URL:** `/api/{entity_name}/uploadcsv`
- **Method:** `POST`
- **Description:** Uploads a CSV file and inserts the data into the corresponding database table.
- **Parameters:**
  - `entity_name` (path): The name of the entity (e.g., `departments`, `jobs`, `employees`).
  - `file` (form-data): The CSV file to be uploaded.
- **Response:**
  - `200 OK`: File upload successful.
  - `450`: The provided file does not have the required name structure.
  - `451`: An error ocurred accessing the uploaded file message indicating the issue.
  - `452`: The columns of the provided file does not match the expected structure.
  - `453`: Error inserting data for the requested entity. Review logs to see additional information.
  - `454`: The requested entity does not exists.
  

## Testing
Instructions on how to run the tests. Pending.

## Contributing
Guidelines for contributing to the project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
Not applicable.