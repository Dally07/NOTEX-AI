from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  NoteViewSet, ClassifyTextApiView

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
    path('classify-text/', ClassifyTextApiView.as_view(), name='classify-text'),
]