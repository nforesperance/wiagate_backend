from django.contrib.auth.models import User
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question, Quiz
from django.http import HttpResponse
from .serializers import QuestionSerializer
from rest_framework import viewsets, permissions
from rest_framework import generics


def home(request):
    return render(request, 'api/index.html')
def index_view(request):
    return render(request,'api/home.html', context=None)


class QuestionViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Quizes.
    """

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.filter(quiz__pk=pk)
        obj = Quiz.objects.all()
        quiz = get_object_or_404(obj, pk=pk)
        serializer = QuestionSerializer(queryset, many=True)
        return Response({"quiz": serializer.data,
                         "max": quiz.number_of_question,
                         "name": quiz.name
                         })
