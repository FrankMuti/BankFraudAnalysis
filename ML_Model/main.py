#!/usr/bin/env python3
## Imports
import os
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from termcolor import colored as cl

import seaborn as sns
import matplotlib.pyplot as plt

plt.rc("font", size=14)
plt.rcParams['axes.grid'] = True
plt.figure(figsize = (6, 3))
plt.gray()
from matplotlib.backends.backend_pdf import PdfPages

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
from sklearn.impute import MissingIndicator, SimpleImputer

from sklearn.preprocessing import PolynomialFeatures, KBinsDiscretizer, FunctionTransformer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, LabelBinarizer, OrdinalEncoder

from sklearn.linear_model import LogisticRegression, LinearRegression, ElasticNet, Lasso, Ridge
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_graphviz
from sklearn.ensemble import BaggingClassifier, BaggingRegressor, RandomForestClassifier, RandomForestRegressor
from sklearn.ensemble import GradientBoostingClassifier,GradientBoostingRegressor, AdaBoostClassifier, AdaBoostRegressor
from sklearn.svm import LinearSVC, LinearSVR, SVC, SVR

from xgboost import XGBClassifier

from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def read_data(file_name):
  return pd.read_csv(file_name)


def dataframe_summary(df):
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
  sc = StandardScaler()
  amount = df['Amount'].values
  df['Amount'] = sc.fit_transform(amount.reshape(-1, 1))
  return df


def process_data(df):
  df = scale_data(df)
  