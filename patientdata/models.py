# Create your models here.
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    code = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class TestData(models.Model):
    patient_info = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # Other fields
    date = models.DateField() 
    unit = models.CharField(max_length=255)
    shift = models.CharField(max_length=255)
    visfatin_number = models.FloatField()
    MDA_number = models.FloatField()
    FMD_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Test data for {self.patient_info.name}"
