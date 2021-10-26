from rest_framework import serializers

from .models import File


class FileUploadSerializer(serializers.Serializer):
  file = serializers.FileField()


class SaveFileSerializer(serializers.Serializer):
  class Meta:
    model = File
    fields = "__all__"
