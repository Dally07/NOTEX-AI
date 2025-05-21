from django.shortcuts import render
import re
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializers
from .classifier import predict_category


# Create your views here.

def split_text_into_phrases(text):
    phrases = re.split(r'[.?!,]\s*', text.strip())
    return [p for p in phrases if p]

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-creat_at')
    serializer_class = NoteSerializers

    def perform_create(self, serializer):
        text = serializer.validated_data.get('phrase')
        category = predict_category(text)
        serializer.save(category=category)

class ClassifyTextApiView(APIView):
    def post(self, request, *args, **kwargs):
        phrase=request.data.get("phrase","")
        if not phrase.strip():
            return Response({"error": "le champ 'text' est requis."}, status=status.HTTP_400_BAD_REQUEST)

        lines = split_text_into_phrases(phrase)
        lines = [p for p in lines if p]
        result = []

        for line in lines:
            try:
                category = predict_category(line)
            except Exception:
                category = "Inconnu"
            result.append({
                "phrase" : line,
                "category" : category
            })

        return Response(result, status=status.HTTP_200_OK)
