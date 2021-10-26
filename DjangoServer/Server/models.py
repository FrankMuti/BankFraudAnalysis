from django.db import models


class File(models.Model):
  id = models.CharField(primary_key=True, max_length=6)
  staff_name = models.CharField(max_length=100)
  position = models.CharField(max_length=200)
  age = models.IntegerField()
  year_joined = models.CharField(max_length=4)

  def __str__(self):
    return self.staff_name

