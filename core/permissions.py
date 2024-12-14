from rest_framework.permissions import BasePermission

class IsHospitalUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_hospital and request.user.is_authenticated
    
class IsPatientUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_patient and request.user.is_authenticated
    

