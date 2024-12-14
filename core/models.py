from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    is_hospital = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


class Hospital(models.Model):
    user = models.OneToOneField('core.CustomUser', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField('core.CustomUser', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
    

class  Document(models.Model):
    file  = models.FileField(upload_to='patientDocuments/')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    


class PatientApproval(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Approval for {self.patient.name}: {'Approved' if self.is_approved else 'pending'}"

