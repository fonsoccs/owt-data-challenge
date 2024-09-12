import pandas as pd
import re
from io import BytesIO
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

def process_data(data: pd.DataFrame, entity: str):
    """
    Take the given data and perform data insertion on the designed entity.

    Args:
        data (pd.DataFrame): The data to be processed.
        entity (str): The entity associated with the data.

    Returns:
        None
    """
    # process data
    print(data.head())
    print(entity)
    # TODO: Implement logic for data insertion, improve documentation
    pass

@router.post("/uploadcsv/")
async def post_upload_file(file: UploadFile):
    """
    Uploads a file and validates the name and the structure of the content (columns).
    If the file is valid, the data is processed and inserted into the database.

    Args:
        file (UploadFile): The file to be uploaded.

    Returns:
        dict: A dictionary containing either an error message or a success message.
    """

    file_pth = file.filename

    # validate the file received
    if not re.match(r'^(departments|jobs|hired_employees)\.csv$', file_pth):
        return {"error": "Allowed files are: departments.csv, jobs.csv, or hired_employees.csv"}

    # prepare the expected columns to validate file structure
    if re.match(r'^departments\.csv$', file_pth):
        expected_columns = {'id', 'department'}
    elif re.match(r'^jobs\.csv$', file_pth):
        expected_columns = {'id', 'job'}
    else: #hired_employees.csv
        expected_columns = {'id', 'name', 'datetime', 'department_id', 'job_id'}

    # read the file contents to validate the columns
    with open(file_pth, "wb") as F:
        contents = await file.read()
        df = pd.read_csv(BytesIO(contents))
        print(df.columns.tolist())

    if set(df.columns.tolist()) != expected_columns:
        return {"error": "Unexpected columns in the uploaded file"}

    # execute data insertion
    process_data(df, file_pth.replace('.csv', ''))

    return {"message": "File upload successful"}
