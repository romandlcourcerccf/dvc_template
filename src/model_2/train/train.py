import os
import pickle

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from dotenv import load_dotenv
from yaml import load, Loader
from dvclive import Live

from pathlib import Path

load_dotenv()

def train():

    LOAD_DATA_PATH=os.environ.get("MODEL_2_LOAD_DATA_PATH")
    TRANSFORM_DATA_PATH=os.environ.get("MODEL_2_TRANSFORM_DATA_PATH")
    TRAIN_DATA_PATH=os.environ.get("MODEL_2_TRAIN_DATA_PATH")
    MODEL_DATA_PATH=os.environ.get("MODEL_2_MODEL_DATA_PATH")
    TRAIN_CONFIG_PATH=os.environ.get("MODEL_2_TRAIN_CONFIG_PATH")

    with open(TRAIN_CONFIG_PATH, "r") as conf:
        train_config = load(conf, Loader=Loader)["train_config"]

    dataset = pd.read_csv(str(Path(TRANSFORM_DATA_PATH) / 'prepared_data.csv' ))
    target = pd.read_csv(str(Path(LOAD_DATA_PATH) / "target.csv" ))  #Fix this later

    train_index, validation_index = train_test_split(dataset.index, 
                                                     test_size=train_config["validation_size"])

    train_index, test_index = train_test_split(train_index, 
                                               test_size=train_config["test_size"])

    model = LinearRegression()
    model.fit(dataset.loc[train_index], target.loc[train_index])

    train_MSE = mean_squared_error(target.loc[test_index], 
                                   model.predict(dataset.loc[test_index]))

    test_MSE = mean_squared_error(target.loc[train_index], 
                                  model.predict(dataset.loc[train_index]))

    validation_MSE = mean_squared_error(target.loc[validation_index], 
                                        model.predict(dataset.loc[validation_index]))
    

    with open(str(Path(TRAIN_DATA_PATH) / "linear_model.pickle"), "wb") as model_file:
        model_file.write(pickle.dumps(model))


if __name__ == "__main__":
    train()