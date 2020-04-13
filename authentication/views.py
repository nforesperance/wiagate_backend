from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404, render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Question, Quiz
from api.serializers import QuestionSerializer


class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloWorldView(APIView):

    def get(self, request, *args, **kwargs):
        pk= request.GET['pk']
        queryset = Question.objects.filter(quiz__pk=pk)
        obj = Quiz.objects.all()
        quiz = get_object_or_404(obj, pk=pk)
        serializer = QuestionSerializer(queryset, many=True)
        return Response({"quiz": serializer.data,
                         "max": quiz.number_of_question,
                         "name": quiz.name
                         })
    # def get(self, request, *args, **kwargs):
    #   id = kwargs.get('id', 'Default Value if not there')


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
