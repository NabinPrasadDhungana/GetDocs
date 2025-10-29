from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, NoteViewSet

router = DefaultRouter()
router.register('Categories', CategoryViewSet, basename='category')
router.register('Notes', NoteViewSet, basename='note')
urlpatterns = [
    
]

urlpatterns += router.urls
