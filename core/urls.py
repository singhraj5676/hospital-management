from rest_framework.routers import DefaultRouter
from core.views import (
    HospitalViewSet,
    PatientViewSet,
    DocumentViewSet,
    PatientApprovalViewSet,
    RegisterViewSet,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path 

router = DefaultRouter()
router.register('hospitals', HospitalViewSet)
router.register('patients', PatientViewSet)
router.register('documents', DocumentViewSet)
router.register('approvals', PatientApprovalViewSet)
router.register('register', RegisterViewSet, basename='register')

urlpatterns = [
    # JWT Authentication
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
    
# Add router-generated URLs to urlpatterns
urlpatterns += router.urls
