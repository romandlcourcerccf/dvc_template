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

    LOAD_DATA_PATH=os.environ.get("LOAD_DATA_PATH")
    TRANSFORM_DATA_PATH=os.environ.get("TRANSFORM_DATA_PATH")
    TRAIN_DATA_PATH=os.environ.get("TRAIN_DATA_PATH")
    MODEL_DATA_PATH=os.environ.get("MODEL_DATA_PATH")
    TRAIN_CONFIG_PATH=os.environ.get("TRAIN_CONFIG_PATH")

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

    # with Live(save_dvc_exp=True) as live:
    #     live.log_artifact("%s/linear_model.pickle" % os.environ.get("MODELS_PATH"))
    #     live.log_metric("train_MSE", train_MSE)
    #     live.log_metric("test_MSE", test_MSE)
    #     live.log_metric("validation_MSE", validation_MSE)

if __name__ == "__main__":
    train()