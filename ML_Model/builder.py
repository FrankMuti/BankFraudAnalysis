#!/usr/bin/env python3
import warnings

import pandas as pd
from pickle import dump

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from xgboost import XGBClassifier

from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

warnings.filterwarnings('ignore')


def read_data(file_name):
  print("Reading File....")
  return pd.read_csv(file_name)


def dataframe_summary(df):
  print("Data Frame Summary...")
  total_transactions = len(df)
  normal = len(df[df.Class == 0])
  fraudulent = len(df[df.Class == 1])
  fraud_percentage = round(fraudulent / normal * 100, 2)

  print(f"Transactions      : {total_transactions}")
  print(f"Normal            : {normal}")
  print(f"Fraudulent        : {fraudulent}")
  print(f"Fraudulent (%)    : {fraud_percentage}")
  print("Dataset Summary")
  print(df.info())


def scale_data(df):
  print("Scaling Data...")
  sc = StandardScaler()
  amount = df['Amount'].values
  df['Amount'] = sc.fit_transform(amount.reshape(-1, 1))
  return df


def process_data(df):
  print("Preprocessing....")
  df = scale_data(df)
  df.drop(['Time'], axis=1, inplace=True)
  df.drop_duplicates(inplace=True)
  return df


def X_and_y_data(df):
  print("Split data into X and y....")
  X = df.drop('Class', axis=1).values
  y = df['Class'].values
  return X, y


def split_data(X, y):
  print("Splitting data to test set and training set...")
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)
  return X_train, X_test, y_train, y_test


def score(y, yhat):
  print(f'Accuracy :{accuracy_score(y, yhat)}')
  print(f'F1 score :{f1_score(y, yhat)}')
  cm = confusion_matrix(y, yhat, labels=[0, 1])
  return cm


def build_model(data_file):
  print("Building Model")
  xgb_boost = XGBClassifier(max_depth=4)

  df = read_data(data_file)
  dataframe_summary(df)
  df = process_data(df)
  X, y = X_and_y_data(df)
  X_train, X_test, y_train,  y_test = split_data(X, y)

  print("Training model")
  xgb_boost.fit(X_train, y_train)
  print("Done. Testing...")
  yhat = xgb_boost.predict(X_test)
  print("Done")

  print("Metrics")
  score(y_test, yhat)
  print("Done")
  return xgb_boost


def main():
  file = "data/creditcard.csv"
  model = build_model(file)
  sc = StandardScaler()
  print("Generate Model binaries....")
  dump(sc, open("static/Scaler.pkl", 'wb'))
  dump(model, open("static/Model.pkl", 'wb'))
  print("Done")



if __name__ == "__main__":
  main()
