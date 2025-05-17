from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializers
from .classifier import predict_category


# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-creat_at')
    serializer_class = NoteSerializers

    def perform_create(self, serializer):
        text = serializer.validated_data.get('phrase')
        category = predict_category(text)
        serializer.save(category=category)