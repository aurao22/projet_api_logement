from sklearn.datasets import fetch_california_housing
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts


california_housing = fetch_california_housing(as_frame=True)

X_train, X_test, y_train, y_test = train_test_split(california_housing.frame.drop(columns='MedHouseVal'), california_housing.frame['MedHouseVal'], test_size=0.33, random_state=42)


if __name__ == "__main__":
    X = X_train
    y = y_train
    lr =  LinearRegression()
    lr.fit(X, y)
    score = lr.score(X, y)
    print("Score: %s" % score)
    mlflow.log_metric("score", score)
    mlflow.sklearn.log_model(lr, "linearRegressionCalifornie")
    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)