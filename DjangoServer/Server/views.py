from django.shortcuts import render
from rest_framework import generics, status
import joblib
from sklearn.model_selection import train_test_split
import io, csv, pandas as pd

from .models import File
from .serializers import FileUploadSerializer, SaveFileSerializer

from rest_framework.response import Response

path_name = "/home/stein/PycharmProjects/BankFraudAnalysis/DjangoServer/Server/"

class UploadFileView(generics.CreateAPIView):
  serializer_class = FileUploadSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    print("====>", serializer.validated_data)
    file = serializer.validated_data['file']
    data = pd.read_csv(file)

    scaler = joblib.load(f"{path_name}ml/Scaler.pkl")
    xgb_classifier = joblib.load(f"{path_name}ml/XGB.pkl")

    total_transactions = len(data)
    normal = len(data[data.Class == 0])
    fraudulent = len(data[data.Class == 1])
    fraud_percentage = round(fraudulent / normal * 100, 2)

    data_details = {
      "total_transactions": total_transactions
    }

    amount = data['Amount'].values
    data['Amount'] = scaler.fit_transform(amount)
    data.drop(['Time'], axis=1, inplace=True)
    data.drop_duplicates(inplace=True)

    X = data.drop('Class', axis=1).values
    y = data['Class'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.99, random_state=1)
    yhat = xgb_classifier.predict(X_test)
    print(yhat == 1 / yhat == 0)
    # for _, row in reader.iterrows():
    #   new_file = File(
    #     id=row['id'],
    #     staff_name = row['Staff Name'],
    #     position = row['Designated Position'],
    #     age = row['Age'],
    #     year_joined = row['Year Joined'],
    #   )
    #   new_file.save()
    return Response({"status": "success", "Result": f"{len(yhat[yhat == 1]) / total_transactions}"}, status=status.HTTP_201_CREATED)


