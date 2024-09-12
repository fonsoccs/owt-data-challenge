import pandas as pd
import re
from io import BytesIO
from fastapi import APIRouter, UploadFile, File
from app.config import entity_config

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

@router.post("/{entity_name}/uploadcsv")
async def post_upload_file(file: UploadFile, entity_name: str):
    """
    Uploads a file and validates the name and the structure of the content (columns).
    If the file is valid, the data is processed and inserted into the database.

    Args:
        file (UploadFile): The file to be uploaded.

    Returns:
        dict: A dictionary containing either an error message or a success message.
    """

    if entity_name in entity_config:
        entity = entity_config[entity_name]
    else:
        return {"error": "Entity not found"}

    file_pth = file.filename

    # validate the file received
    if not re.match(entity['file_regex'], file_pth):
        return {"error": f"The allowed file for entity {entity['filename']} is: {entity['filename']}"}

    # prepare the expected columns to validate file structure
    expected_columns = entity['columns']
    # print(expected_columns)

    # read the file contents to validate the columns
    with open(file_pth, "wb") as F:
        contents = await file.read()
        df = pd.read_csv(BytesIO(contents))

    print(df.columns.tolist())
    if df.columns.tolist() != expected_columns:
        return {"error": "Unexpected columns in the uploaded file"}

    # execute data insertion
    process_data(df, entity['table_name'])

    return {"message": "File upload successful"}
