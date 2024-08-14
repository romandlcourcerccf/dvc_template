import os

from sklearn import datasets
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

load_dotenv()


def load():

    LOAD_DATA_PATH = os.environ.get("LOAD_DATA_PATH")

    dataset = datasets.load_diabetes()
    features = pd.DataFrame(data=dataset.data, 
                            columns=["feat%s" % x for x in range(dataset.data.shape[1])])
    target = pd.DataFrame(data=dataset.target, columns=["target"])

    features.to_csv(str(Path(LOAD_DATA_PATH) / 'initial_data.csv'))
    target.to_csv(str(Path(LOAD_DATA_PATH) / 'target.csv'))

    
if __name__ == "__main__":  
   
   load()