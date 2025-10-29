from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewset

router = DefaultRouter()
router.register('Accounts', UserProfileViewset, basename='account')

urlpatterns = [
    
]

urlpatterns += router.urls
