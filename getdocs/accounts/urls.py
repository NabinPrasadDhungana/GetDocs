from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewset, CustomUserViewSet

router = DefaultRouter()
router.register('Profiles', UserProfileViewset, basename='account')
router.register('Users', CustomUserViewSet, basename='user')
urlpatterns = [
    
]

urlpatterns += router.urls
