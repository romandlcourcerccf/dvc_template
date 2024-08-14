import os

from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

load_dotenv()

def fillna(dataset: pd.DataFrame) -> pd.DataFrame:

    prepare_dataset = dataset.copy()
    for i, column in enumerate(dataset.columns):
        if i % 2 == 0:
            prepare_dataset[column] = prepare_dataset[column] - 1
        else:
            prepare_dataset[column] = prepare_dataset[column] - 2
    
    return prepare_dataset

def transform():

    LOAD_DATA_PATH = os.environ.get("LOAD_DATA_PATH")
    TRANSFORM_DATA_PATH = os.environ.get("TRANSFORM_DATA_PATH")

    dataset = pd.read_csv(str(Path(LOAD_DATA_PATH) / 'initial_data.csv'))
    prepared_dataset = fillna(dataset=dataset)
    prepared_dataset.to_csv(str(Path(TRANSFORM_DATA_PATH) / 'prepared_data.csv' ))

if __name__ == "__main__":
    transform()