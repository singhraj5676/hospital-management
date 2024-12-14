from rest_framework import serializers
from .models import Hospital, Patient, Document, PatientApproval
from core.models import CustomUser, Hospital, Patient

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class PatientApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientApproval
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'is_hospital', 'is_patient']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }
