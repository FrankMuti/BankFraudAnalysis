import sys, getopt
import json
import pickle
import numpy as np
import pandas as pd


def read(filename):
  return pd.read_csv(filename)


def preprocess(data, scaler):
  if "Time" in data.columns:
    data.drop(['Time'], axis=1, inplace=True)

  if "Class" in data.columns:
    data.drop(['Class'], axis=1, inplace=True)

  amount = data['Amount'].values
  data['Amount'] = scaler.fit_transform(amount.reshape(-1, 1))
  data.drop_duplicates(inplace=True)
  return data.values


def run(df_path, sc_path, cl_path):
  ## Load data
  data = read(df_path)
  assert data is not None

  ## Load Scaler and classifier
  sc = pickle.load(open(sc_path, 'rb'))
  classifier = pickle.load(open(cl_path, 'rb'))

  ## Preprocess
  X_data = preprocess(data, sc)
  ## result
  y_hat = classifier.predict(X_data)
  ## 0 = good, 1 = fraud
  freq = np.bincount(y_hat)

  result = {
    "good": freq[0],
    "bad": freq[1]
  }
  return result


def json_file(data, file_name):
  json.dump(data, open(file_name, 'w'))
  print("Done")


def main(argv):
  def _help():
    print("python classify.py -d [data file] -j [json out file] -s [scaler file] -c [classifier file]")
    print("python classify.py --data=[data file] --json=[json out file] --scaler[scaler file] --class[classifier file]")
  data_set_path = ""
  json_out_file = ""
  scaler_file_path = ""
  classifier_path = ""

  try:
    option_names = ["data=", "json=", "scaler=", "class=", "ten="]
    opts, args = getopt.getopt(argv, "hd:j:s:c:t", option_names)
  except Exception as e:
    _help()
    print(e)
    sys.exit(2)

  if len(opts) < 4 or len(opts) > 5:
    _help()
    sys.exit(2)

  print(opts)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      _help()
    elif opt in ("-d", "--data"):
      data_set_path = arg
    elif opt in ("-j", "--json"):
      json_out_file = arg
    elif opt in ("-s", "--scaler"):
      scaler_file_path = arg
    elif opt in ("-c", "--class"):
      classifier_path = arg

  print("========== CLASSIFY =========")
  print("== GOOD JOB, IT WORKS     ===")
  print(data_set_path, json_out_file, scaler_file_path, classifier_path)
  print("=============================")
  ## Uncomment i production
  # result = run(data_set_path, scaler_file_path, classifier_path)
  # json_file(result, json_out_file)


if __name__ == "__main__":
  main(sys.argv[1:])
