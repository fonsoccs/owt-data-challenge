import pandas as pd
import re
from io import BytesIO
from fastapi import APIRouter, UploadFile, File, HTTPException
import psycopg2
import psycopg2.extras 
from app.config import entity_config, db_config


router = APIRouter()

def process_data(data: pd.DataFrame, entity: dict):
    """
    Take the given data and perform data insertion on the designed entity.

    Args:
        data (pd.DataFrame): The data to be processed.
        entity (str): The entity associated with the data.

    Returns:
        None
    """

    # Connect to PostgreSQL database
    try:
        conn = psycopg2.connect(
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"]
        )
        cursor = conn.cursor()
    except Exception as e:
        print(f"ERROR: {e}")
        return False

    # Example: Insert data into the corresponding table
    table_name = entity["table_name"].lower()
    columns = entity["columns"]

    #drop invalid rows
    data.dropna(inplace=True)

    run_status = True
    batch_size = 1000

    try:
        for start in range(0, len(data), batch_size):
            end = start + batch_size
            batch = data.iloc[start:end]
            values = [tuple(row[col] for col in columns) for _, row in batch.iterrows()]
            print(f"Loading batch: {start} to {end}")
            insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES %s"
            psycopg2.extras.execute_values(cursor, insert_query, values)
    except Exception as e:
        print(f"Error: {e}")
        #print(f"Batch values: {values}")
        run_status = False
    finally:
        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()
    
    return run_status

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
        #return {"ERROR": "Entity not found"}
        raise HTTPException(status_code=454, detail="Entity not found")

    file_pth = file.filename

    # validate the file received
    if not re.match(entity['file_regex'], file_pth):
        #return {"ERROR": f"The allowed file for entity {entity['filename']} is: {entity['filename']}"}
        raise HTTPException(status_code=450, detail=f"The allowed file for entity {entity['filename']} is: {entity['filename']}")

    # prepare the expected columns to validate file structure
    expected_columns = entity['columns']

    try: 
        # read the file contents to validate the columns and load the data
        contents = await file.read()
        df = pd.read_csv(BytesIO(contents))
    except Exception as e:
        print(f"Error: {e}")
        #return {"ERROR": "Error accessing the uploaded file"}
        raise HTTPException(status_code=451, detail="Error accessing the uploaded file")
    
    if df.columns.tolist() != expected_columns:
        #return {"ERROR": "Unexpected columns in the uploaded file"}
        raise HTTPException(status_code=452, detail="Unexpected columns in the uploaded file")

    # execute data loading
    if process_data(df, entity) == False:
        #return {"ERROR": f"Data insertion for '{entity_name}' failed"}
        raise HTTPException(status_code=453, detail=f"Data insertion for '{entity_name}' failed")
 
    return {"message": "File upload successful"}
