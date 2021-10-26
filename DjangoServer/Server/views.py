from django.shortcuts import render
from rest_framework import generics

import io, csv, pandas as pd

from .models import File
from .serializers import FileUploadSerializer, SaveFileSerializer

from rest_framework.response import Response

class UploadFileView(generics.CreateAPIView):
  serializer_class = FileUploadSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data = request.data)
    serialize.is_valid(raise_exception = True)
    file = serializer.validated_data['File']
    reader = pd.read_csv(file)
    for _, row in reader.iterrows():
      new_file = File(
        id=row['id'],
        staff_name = row['Staff Name']
        position = row['Designated Position']
        age = row['Age']
        year_joined = row['Year Joined']
      )
      new_file.save()
    return Response({"status": "success"}, status.HTTP_201_CREATED)


