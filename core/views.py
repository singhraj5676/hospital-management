from rest_framework import viewsets
from .models import Hospital, Patient, Document, PatientApproval
from .serializers import HospitalSerializer, PatientSerializer, DocumentSerializer, PatientApprovalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status, viewsets
from rest_framework.response import Response
from core.models import CustomUser, Hospital, Patient
from core.serializers import CustomUserSerializer, HospitalSerializer, PatientSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
import logging
logger = logging.getLogger(__name__)

class RegisterViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]  # Allow anyone to access this ViewSet

    def create(self, request, *args, **kwargs):
        data = request.data
        logger.debug("Received registration data: %s", data)
        is_hospital = data.get('is_hospital', False)
        is_patient = data.get('is_patient', False)

        if is_hospital and is_patient:
            logger.debug("Validation failed: User cannot be both hospital and patient.")
            return Response({"error": "A user cannot be both a hospital and a patient."}, status=status.HTTP_400_BAD_REQUEST)

        if not is_hospital and not is_patient:
            logger.debug("Validation failed: User must be either hospital or patient.")
            return Response({"error": "A user must be either a hospital or a patient."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            logger.debug("User data is valid. Creating user.")
            user = serializer.save()

            if is_hospital:
                hospital_data = {"user": user.id, "name": data.get("name"), "address": data.get("address")}
                hospital_serializer = HospitalSerializer(data=hospital_data)
                hospital_serializer.is_valid(raise_exception=True)
                hospital_serializer.save()

            if is_patient:
                patient_data = {"user": user.id, "name": data.get("name")}
                patient_serializer = PatientSerializer(data=patient_data)
                patient_serializer.is_valid(raise_exception=True)
                patient_serializer.save()

            logger.debug("User registered successfully: %s", user)
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

        logger.debug("User registration failed. Errors: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class PatientApprovalViewSet(viewsets.ModelViewSet):
    queryset = PatientApproval.objects.all()
    serializer_class = PatientApprovalSerializer



